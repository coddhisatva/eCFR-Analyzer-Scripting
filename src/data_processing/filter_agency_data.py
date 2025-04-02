#!/usr/bin/env python
"""
Script to filter agency data for a specific title
"""
import os
import json
import logging
from datetime import datetime
import argparse

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Directory for raw data
RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "raw", "agencies")

def ensure_directory_exists(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def filter_agency(agency: dict, title: int) -> dict:
    """
    Recursively filter an agency and its subagencies to only include references to a specific title.
    
    Args:
        agency: Agency dictionary to filter
        title: Title number to filter for
        
    Returns:
        Filtered agency dictionary or None if no references to the title exist
    """
    # Filter CFR references for the specified title
    filtered_refs = [
        ref for ref in agency.get('cfr_references', [])
        if ref.get('title') == title
    ]
    
    # Filter subagencies recursively
    filtered_children = []
    for child in agency.get('children', []):
        filtered_child = filter_agency(child, title)
        if filtered_child:
            filtered_children.append(filtered_child)
    
    # If this agency has no references to the title and no filtered children, return None
    if not filtered_refs and not filtered_children:
        return None
    
    # Create a copy of the agency with filtered references and children
    filtered_agency = agency.copy()
    filtered_agency['cfr_references'] = filtered_refs
    filtered_agency['children'] = filtered_children
    
    return filtered_agency

def filter_agency_data(input_file: str, title: int, output_file: str = None):
    """
    Filter agency data to only include references to a specific title.
    
    Args:
        input_file: Path to the input agency JSON file
        title: The title number to filter for
        output_file: Path to save the filtered data (default: agency-title-{title}.json)
    """
    if output_file is None:
        output_file = f"agency-title-{title}.json"
    
    logger.info(f"Reading agency data from {input_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Filter agencies recursively
    filtered_agencies = []
    for agency in data.get('agencies', []):
        filtered_agency = filter_agency(agency, title)
        if filtered_agency:
            filtered_agencies.append(filtered_agency)
    
    # Create filtered data structure
    filtered_data = {
        'agencies': filtered_agencies,
        'metadata': {
            'filtered_for_title': title,
            'original_file': input_file,
            'filtered_at': datetime.now().isoformat()
        }
    }
    
    # Save filtered data
    output_path = os.path.join(os.path.dirname(input_file), output_file)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(filtered_data, f, indent=2)
    
    logger.info(f"Filtered data saved to {output_path}")
    logger.info(f"Found {len(filtered_agencies)} agencies with references to title {title}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Filter agency data for a specific title')
    parser.add_argument('--input', required=True, help='Input agency JSON file')
    parser.add_argument('--title', type=int, required=True, help='Title number to filter for')
    parser.add_argument('--output', help='Output file name (default: agency-title-{title}.json)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    # Set logging level based on verbose flag
    if not args.verbose:
        logger.setLevel(logging.INFO)
    
    filter_agency_data(args.input, args.title, args.output) 