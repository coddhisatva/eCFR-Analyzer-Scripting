#!/usr/bin/env python
"""
Script to process corrections data into CSV format
"""
import os
import json
import logging
import csv
from datetime import datetime
from typing import List, Dict, Any, Optional
import argparse

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import models
from src.models.correction import Correction

# Directory for raw and processed data
RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "raw", "corrections")
PROCESSED_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "processed_backup")

def ensure_directory_exists(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def clean_text(text: Any) -> str:
    """Clean and normalize text."""
    if text is None:
        return ""
    # Convert to string if not already
    return str(text).strip()

def parse_date(date_str: str) -> Optional[datetime]:
    """Parse date string into datetime object."""
    if not date_str:  # Handle empty strings and None
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        try:
            return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            logger.warning(f"Could not parse date: {date_str}")
            return None

def build_node_id(hierarchy: Dict[str, str]) -> str:
    """
    Build a node ID from the hierarchy data.
    Format: us/federal/ecfr/title=X/chapter=Y/subchap=Z/part=W/section=V
    """
    parts = ["us", "federal", "ecfr"]
    
    # Add title
    if 'title' in hierarchy:
        parts.append(f"title={hierarchy['title']}")
    
    # Add chapter
    if 'chapter' in hierarchy:
        parts.append(f"chapter={hierarchy['chapter']}")
    
    # Add subchapter (converted to subchap)
    if 'subchapter' in hierarchy:
        parts.append(f"subchap={hierarchy['subchapter']}")
    
    # Add part
    if 'part' in hierarchy:
        parts.append(f"part={hierarchy['part']}")
    elif 'section' in hierarchy:
        # If we have a section but no part, try to infer the part number
        section = hierarchy['section'].strip().strip('-').strip()
        if '.' in section:
            # Part number is everything before the dot
            part = section.split('.')[0]
            parts.append(f"part={part}")
    
    # Add subpart if present
    if 'subpart' in hierarchy:
        parts.append(f"subpart={hierarchy['subpart']}")
    
    # Add section
    if 'section' in hierarchy:
        # Clean up section number by removing whitespace and dashes
        section = hierarchy['section'].strip().strip('-').strip()
        parts.append(f"section={section}")
    
    return '/'.join(parts)

def find_matching_node_id(nodes_data: List[Dict], hierarchy: Dict[str, str]) -> Optional[str]:
    """
    Find a matching node ID from our local nodes data.
    
    Args:
        nodes_data: List of node dictionaries from our CSV
        hierarchy: Dictionary containing title, chapter, etc.
        
    Returns:
        Matching node ID if found, None otherwise
    """
    try:
        # Get title and chapter
        title = hierarchy.get('title')
        chapter = hierarchy.get('chapter')
        if not title or not chapter:
            return None
            
        # First try exact match with the full node_id
        node_id = build_node_id(hierarchy)
        exact_match = next((node['id'] for node in nodes_data if node['id'] == node_id), None)
        if exact_match:
            return exact_match
            
        # If no exact match, search for any node with this title and chapter
        for node in nodes_data:
            if f"/title={title}/" in node['id'] and f"/chapter={chapter}/" in node['id']:
                return node['id']
            
    except Exception as e:
        logger.warning(f"Error finding matching node: {e}")
        
    return None

def load_nodes_data() -> List[Dict]:
    """Load nodes data from CSV file."""
    nodes_data = []
    nodes_file = os.path.join(PROCESSED_DATA_DIR, "nodes.csv")
    try:
        with open(nodes_file, 'r') as f:
            reader = csv.DictReader(f)
            nodes_data = list(reader)
    except Exception as e:
        logger.error(f"Error loading nodes data: {e}")
    return nodes_data

def process_correction_data(correction_data: Dict[str, Any], nodes_data: List[Dict]) -> List[Correction]:
    """
    Process correction data into Correction entities
    
    Args:
        correction_data: Dictionary containing correction data
        nodes_data: List of node dictionaries from our CSV
        
    Returns:
        List of Correction entities (one for each CFR reference)
    """
    corrections = []
    
    # Extract common correction data
    error_corrected = parse_date(correction_data.get('error_corrected', ''))
    error_occurred = parse_date(correction_data.get('error_occurred', ''))
    correction_duration = (error_corrected - error_occurred).days if error_corrected and error_occurred else None
    
    # Process each CFR reference
    for i, cfr_ref in enumerate(correction_data.get('cfr_references', [])):
        # Try to find matching node using hierarchy
        hierarchy = cfr_ref.get('hierarchy', {})
        node_id = find_matching_node_id(nodes_data, hierarchy)
        if not node_id:
            logger.warning(f"Could not find matching node for title={hierarchy.get('title')}, chapter={hierarchy.get('chapter')}")
            continue
        
        # Generate a unique ID using a hash of the node_id and index
        unique_id = abs(hash(f"correction:{node_id}:{i}")) % (2**31)  # Ensure positive 32-bit integer
        
        # Create correction entity
        correction = Correction(
            id=unique_id,
            node_id=node_id,
            title=correction_data.get('title', ''),
            corrective_action=clean_text(correction_data.get('corrective_action', '')),
            error_corrected=error_corrected,
            error_occurred=error_occurred,
            correction_duration=correction_duration,
            fr_citation=clean_text(correction_data.get('fr_citation', '')),
            position=clean_text(correction_data.get('position', '')),
            year=correction_data.get('year'),
            metadata={
                'cfr_reference': clean_text(cfr_ref.get('cfr_reference', '')),
                'last_modified': correction_data.get('last_modified'),
                'display_in_toc': correction_data.get('display_in_toc'),
                'last_updated': datetime.now().isoformat()
            }
        )
        corrections.append(correction)
    
    return corrections

def write_corrections_to_csv(corrections: List[Correction], output_file: str):
    """Write corrections to CSV file."""
    if not corrections:
        return
        
    # Define CSV headers based on Correction model fields
    fieldnames = [
        'id', 'node_id', 'title', 'corrective_action', 'error_corrected',
        'error_occurred', 'correction_duration', 'fr_citation', 'position',
        'year', 'metadata'
    ]
    
    # Write to CSV
    mode = 'a' if os.path.exists(output_file) else 'w'
    with open(output_file, mode, newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if mode == 'w':
            writer.writeheader()
        
        for correction in corrections:
            # Convert correction object to dict
            correction_dict = {
                'id': correction.id,
                'node_id': correction.node_id,
                'title': correction.title,
                'corrective_action': correction.corrective_action,
                'error_corrected': correction.error_corrected.isoformat() if correction.error_corrected else None,
                'error_occurred': correction.error_occurred.isoformat() if correction.error_occurred else None,
                'correction_duration': correction.correction_duration,
                'fr_citation': correction.fr_citation,
                'position': correction.position,
                'year': correction.year,
                'metadata': json.dumps(correction.metadata)
            }
            writer.writerow(correction_dict)

def process_corrections_file(file_path: str, nodes_data: List[Dict]):
    """
    Process a single corrections data file
    
    Args:
        file_path: Path to the corrections data file
        nodes_data: List of node dictionaries from our CSV
    """
    logger.info(f"Processing corrections file: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Process corrections
        all_corrections = []
        for correction_data in data.get('ecfr_corrections', []):
            corrections = process_correction_data(correction_data, nodes_data)
            all_corrections.extend(corrections)
        
        if all_corrections:
            output_file = os.path.join(PROCESSED_DATA_DIR, "corrections.csv")
            write_corrections_to_csv(all_corrections, output_file)
            logger.info(f"Wrote {len(all_corrections)} corrections to CSV")
        
    except Exception as e:
        logger.error(f"Error processing {file_path}: {e}")
        raise

def process_all_corrections(date=None):
    """
    Process all corrections data files for a specific date
    
    Args:
        date: The date of the files to process (default: current date)
    """
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    
    input_dir = os.path.join(RAW_DATA_DIR, date)
    if not os.path.exists(input_dir):
        logger.error(f"No data found for date {date}")
        return
    
    # Load nodes data once
    nodes_data = load_nodes_data()
    if not nodes_data:
        logger.error("Failed to load nodes data")
        return
    
    for filename in os.listdir(input_dir):
        if not filename.endswith(".json") or not filename.startswith("corrections-"):
            continue
        
        file_path = os.path.join(input_dir, filename)
        process_corrections_file(file_path, nodes_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process corrections data files into CSV')
    parser.add_argument('file', nargs='?', help='Single corrections file to process. If not provided, processes all files for latest date.')
    parser.add_argument('--date', help='Date of the files to process (YYYY-MM-DD)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    # Set logging level based on verbose flag
    if not args.verbose:
        logger.setLevel(logging.INFO)
    
    ensure_directory_exists(PROCESSED_DATA_DIR)
    
    # Load nodes data
    nodes_data = load_nodes_data()
    if not nodes_data:
        logger.error("Failed to load nodes data")
        exit(1)
    
    if args.file:
        # Process single file
        process_corrections_file(args.file, nodes_data)
    else:
        # Process all files for specified date
        process_all_corrections(args.date) 