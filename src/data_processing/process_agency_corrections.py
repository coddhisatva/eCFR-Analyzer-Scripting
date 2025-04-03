#!/usr/bin/env python3
"""
Script to process agency corrections by:
1. Loading all corrections files across titles
2. Mapping corrections to agencies based on CFR references
3. Building a complete agency correction map
4. Propagating counts up the agency hierarchy
"""
import os
import json
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants
RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "raw")
JSON_TABLES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "localPush", "json_tables")

def load_agencies(date: str) -> List[Dict[str, Any]]:
    """
    Load agencies from JSON file
    
    Args:
        date: Date string in YYYY-MM-DD format
        
    Returns:
        List of agency dictionaries
    """
    agencies_file = os.path.join(RAW_DATA_DIR, "agencies", date, "agencies.json")
    with open(agencies_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get('agencies', [])

def flatten_agencies(agencies: List[Dict[str, Any]], parent_id: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Flatten nested agency structure into a list
    
    Args:
        agencies: List of agency dictionaries with nested children
        parent_id: ID of parent agency
        
    Returns:
        Flattened list of agency dictionaries
    """
    flattened = []
    for agency in agencies:
        # Add parent_id to agency
        agency['parent_id'] = parent_id
        
        # Add agency without children to flattened list
        agency_copy = agency.copy()
        children = agency_copy.pop('children', [])
        flattened.append(agency_copy)
        
        # Recursively process children
        if children:
            child_agencies = flatten_agencies(children, agency['slug'])
            flattened.extend(child_agencies)
    
    return flattened

def build_agency_cfr_map(agencies: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Build map of CFR references to agencies
    
    Args:
        agencies: List of agency dictionaries
        
    Returns:
        Dictionary mapping CFR references to agencies
    """
    cfr_map = {}  # (title, chapter) -> List[agency_ids]
    
    for agency in agencies:
        agency_id = agency['slug']
        for ref in agency.get('cfr_references', []):
            title = ref.get('title')
            chapter = ref.get('chapter')
            if title and chapter:
                key = (title, chapter)
                if key not in cfr_map:
                    cfr_map[key] = []
                cfr_map[key].append(agency_id)
    
    return cfr_map

def map_correction_to_agencies(correction: Dict[str, Any], cfr_map: Dict[str, List[str]]) -> List[str]:
    """
    Map a correction to agencies based on CFR references
    
    Args:
        correction: Correction dictionary
        cfr_map: Map of CFR references to agencies
        
    Returns:
        List of agency IDs
    """
    agency_ids = set()
    
    for ref in correction.get('cfr_references', []):
        hierarchy = ref.get('hierarchy', {})
        title = hierarchy.get('title')
        chapter = hierarchy.get('chapter')
        
        if title and chapter:
            key = (int(title), chapter)
            if key in cfr_map:
                agency_ids.update(cfr_map[key])
    
    return list(agency_ids)

def process_corrections_file(file_path: str, cfr_map: Dict[str, List[str]], agency_corrections: Dict[str, int]):
    """
    Process a single corrections file
    
    Args:
        file_path: Path to corrections file
        cfr_map: Map of CFR references to agencies
        agency_corrections: Dictionary to store agency correction counts
    """
    logger.info(f"Processing corrections file: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for correction in data.get('ecfr_corrections', []):
        # Map correction to agencies
        agency_ids = map_correction_to_agencies(correction, cfr_map)
        
        # Update agency correction counts
        for agency_id in agency_ids:
            agency_corrections[agency_id] = agency_corrections.get(agency_id, 0) + 1

def propagate_agency_counts(agency_corrections: Dict[str, int], agencies: List[Dict[str, Any]]):
    """
    Propagate correction counts up the agency hierarchy
    
    Args:
        agency_corrections: Dictionary of agency correction counts
        agencies: List of agency dictionaries
    """
    # Build parent map
    parent_map = {agency['slug']: agency['parent_id'] for agency in agencies}
    
    # Propagate counts up
    for agency_id in agency_corrections:
        current_id = parent_map.get(agency_id)
        count = agency_corrections[agency_id]
        
        while current_id:
            agency_corrections[current_id] = agency_corrections.get(current_id, 0) + count
            current_id = parent_map.get(current_id)

def save_agency_corrections(agency_corrections: Dict[str, int], date: str):
    """
    Save agency correction counts to JSON
    
    Args:
        agency_corrections: Dictionary of agency correction counts
        date: Date string in YYYY-MM-DD format
    """
    # Create output directory if it doesn't exist
    output_dir = os.path.join(JSON_TABLES_DIR, "agencies")
    os.makedirs(output_dir, exist_ok=True)
    
    # Save to JSON
    output_file = os.path.join(output_dir, "agency_corrections.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'agency_corrections': agency_corrections,
            'last_updated': datetime.now().isoformat()
        }, f, indent=2)
    
    logger.info(f"Saved agency corrections to {output_file}")

def process_agency_corrections(date: str):
    """
    Process all agency corrections
    
    Args:
        date: Date string in YYYY-MM-DD format
    """
    # Load and flatten agencies
    agencies = load_agencies(date)
    flattened_agencies = flatten_agencies(agencies)
    
    # Build CFR reference map
    cfr_map = build_agency_cfr_map(flattened_agencies)
    
    # Initialize agency corrections
    agency_corrections = {}
    
    # Process all corrections files
    corrections_dir = os.path.join(RAW_DATA_DIR, "corrections", date)
    for filename in os.listdir(corrections_dir):
        if filename.startswith("corrections-title-") and filename.endswith(".json"):
            file_path = os.path.join(corrections_dir, filename)
            process_corrections_file(file_path, cfr_map, agency_corrections)
    
    # Propagate counts up the hierarchy
    propagate_agency_counts(agency_corrections, flattened_agencies)
    
    # Save results
    save_agency_corrections(agency_corrections, date)

def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Process agency corrections')
    parser.add_argument('--date', type=str, default='2025-03-31',
                      help='Date in YYYY-MM-DD format')
    
    args = parser.parse_args()
    process_agency_corrections(args.date)

if __name__ == "__main__":
    main() 