#!/usr/bin/env python
"""
Script to process agency data into database entities
"""
import os
import json
import logging
from datetime import datetime
from typing import List, Dict, Any, Optional
import argparse

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import models
from src.models.agency import Agency
from src.models.cfr_reference import CFRReference
from src.models.agency_node_mapping import AgencyNodeMapping
from src.database.connector import insert_agencies, insert_cfr_references, insert_agency_node_mappings

# Directory for raw and processed data
RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "raw")
PROCESSED_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "processed")

def ensure_directory_exists(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def clean_text(text: str) -> str:
    """Clean and normalize text."""
    if text is None:
        return ""
    return text.strip()

def process_agency_data(agency_data: Dict[str, Any], parent_id: Optional[str] = None, depth: int = 0) -> List[Agency]:
    """
    Process agency data recursively to create Agency entities
    
    Args:
        agency_data: Dictionary containing agency data
        parent_id: ID of parent agency (if any)
        depth: Current depth in the hierarchy
        
    Returns:
        List of Agency entities
    """
    agencies = []
    
    # Extract basic agency information
    agency_id = agency_data.get('id')
    if not agency_id:
        logger.warning("Skipping agency without ID")
        return []
    
    # Create agency entity
    agency = Agency(
        id=agency_id,
        name=clean_text(agency_data.get('name', '')),
        short_name=clean_text(agency_data.get('short_name', '')),
        display_name=clean_text(agency_data.get('display_name', '')),
        sortable_name=clean_text(agency_data.get('sortable_name', '')),
        parent_id=parent_id,
        depth=depth,
        agency_type=agency_data.get('agency_type', 'middle'),
        metadata={
            'description': clean_text(agency_data.get('description', '')),
            'website': clean_text(agency_data.get('website', '')),
            'contact_info': clean_text(agency_data.get('contact_info', '')),
            'last_updated': datetime.now().isoformat()
        },
        num_children=len(agency_data.get('children', [])),
        num_words=0,  # Will be calculated later
        num_sections=0,  # Will be calculated later
        num_corrections=0  # Will be calculated later
    )
    
    agencies.append(agency)
    
    # Process children recursively
    for child in agency_data.get('children', []):
        child_agencies = process_agency_data(child, agency_id, depth + 1)
        agencies.extend(child_agencies)
    
    return agencies

def process_cfr_references(agency_id: str, references_data: List[Dict[str, Any]]) -> List[CFRReference]:
    """
    Process CFR references for an agency
    
    Args:
        agency_id: ID of the agency
        references_data: List of reference data dictionaries
        
    Returns:
        List of CFRReference entities
    """
    references = []
    
    for i, ref_data in enumerate(references_data):
        reference = CFRReference(
            agency_id=agency_id,
            title=ref_data.get('title', ''),
            subheading=clean_text(ref_data.get('subheading', '')),
            is_primary=ref_data.get('is_primary', False),
            ordinal=i,
            node_id=ref_data.get('node_id')
        )
        references.append(reference)
    
    return references

def process_agency_node_mappings(agency_id: str, mappings_data: List[Dict[str, Any]]) -> List[AgencyNodeMapping]:
    """
    Process agency-node mappings
    
    Args:
        agency_id: ID of the agency
        mappings_data: List of mapping data dictionaries
        
    Returns:
        List of AgencyNodeMapping entities
    """
    mappings = []
    
    for mapping_data in mappings_data:
        mapping = AgencyNodeMapping(
            agency_id=agency_id,
            node_id=mapping_data.get('node_id'),
            is_primary=mapping_data.get('is_primary', False),
            is_direct_reference=mapping_data.get('is_direct_reference', True),
            relationship_type=mapping_data.get('relationship_type', 'regulates'),
            metadata={
                'notes': clean_text(mapping_data.get('notes', '')),
                'last_updated': datetime.now().isoformat()
            }
        )
        mappings.append(mapping)
    
    return mappings

def process_agency_file(file_path: str):
    """
    Process a single agency data file
    
    Args:
        file_path: Path to the agency data file
    """
    logger.info(f"Processing agency file: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Process agencies
        agencies = process_agency_data(data)
        if agencies:
            insert_agencies(agencies)
            logger.info(f"Inserted {len(agencies)} agencies")
        
        # Process CFR references
        references = process_cfr_references(data['id'], data.get('cfr_references', []))
        if references:
            insert_cfr_references(references)
            logger.info(f"Inserted {len(references)} CFR references")
        
        # Process agency-node mappings
        mappings = process_agency_node_mappings(data['id'], data.get('node_mappings', []))
        if mappings:
            insert_agency_node_mappings(mappings)
            logger.info(f"Inserted {len(mappings)} agency-node mappings")
        
    except Exception as e:
        logger.error(f"Error processing {file_path}: {e}")
        raise

def process_all_agencies(date=None):
    """
    Process all agency data files for a specific date
    
    Args:
        date: The date of the files to process (default: current date)
    """
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    
    input_dir = os.path.join(RAW_DATA_DIR, date)
    if not os.path.exists(input_dir):
        logger.error(f"No data found for date {date}")
        return
    
    for filename in os.listdir(input_dir):
        if not filename.endswith(".json") or not filename.startswith("agency-"):
            continue
        
        file_path = os.path.join(input_dir, filename)
        process_agency_file(file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process agency data files')
    parser.add_argument('file', nargs='?', help='Single agency file to process. If not provided, processes all files for latest date.')
    parser.add_argument('--date', help='Date of the files to process (YYYY-MM-DD)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    # Set logging level based on verbose flag
    if not args.verbose:
        logger.setLevel(logging.INFO)
    
    ensure_directory_exists(PROCESSED_DATA_DIR)
    
    if args.file:
        # Process single file
        process_agency_file(args.file)
    else:
        # Process all files for specified date
        process_all_agencies(args.date) 