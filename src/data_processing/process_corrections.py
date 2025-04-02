#!/usr/bin/env python
"""
Script to process corrections data into database entities
"""
import os
import json
import logging
from datetime import datetime
from typing import List, Dict, Any
import argparse

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import models
from src.models.correction import Correction
from src.database.connector import insert_corrections

# Directory for raw and processed data
RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "raw", "corrections")
PROCESSED_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "processed", "corrections")

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

def parse_date(date_str: str) -> datetime:
    """Parse date string into datetime object."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        try:
            return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            logger.warning(f"Could not parse date: {date_str}")
            return datetime.now()

def build_node_id(hierarchy: Dict[str, str]) -> str:
    """
    Build a node ID from the hierarchy data.
    Format: title-X/chapter-Y/subchap-Z/part-W/section-V
    """
    parts = []
    
    # Add title
    if 'title' in hierarchy:
        parts.append(f"title-{hierarchy['title']}")
    
    # Add chapter
    if 'chapter' in hierarchy:
        parts.append(f"chapter-{hierarchy['chapter']}")
    
    # Add subchapter (converted to subchap)
    if 'subchapter' in hierarchy:
        parts.append(f"subchap-{hierarchy['subchapter']}")
    
    # Add part
    if 'part' in hierarchy:
        parts.append(f"part-{hierarchy['part']}")
    
    # Add subpart if present
    if 'subpart' in hierarchy:
        parts.append(f"subpart-{hierarchy['subpart']}")
    
    # Add section
    if 'section' in hierarchy:
        parts.append(f"section-{hierarchy['section']}")
    
    return '/'.join(parts)

def process_correction_data(correction_data: Dict[str, Any]) -> List[Correction]:
    """
    Process correction data into Correction entities
    
    Args:
        correction_data: Dictionary containing correction data
        
    Returns:
        List of Correction entities (one for each CFR reference)
    """
    corrections = []
    
    # Extract common correction data
    error_corrected = parse_date(correction_data.get('error_corrected', ''))
    error_occurred = parse_date(correction_data.get('error_occurred', ''))
    correction_duration = (error_corrected - error_occurred).days if error_corrected and error_occurred else None
    
    # Process each CFR reference
    for cfr_ref in correction_data.get('cfr_references', []):
        # Build node_id from hierarchy
        hierarchy = cfr_ref.get('hierarchy', {})
        node_id = build_node_id(hierarchy)
        
        # Create correction entity
        correction = Correction(
            id=correction_data.get('id'),  # Get ID from input data
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

def process_corrections_file(file_path: str):
    """
    Process a single corrections data file
    
    Args:
        file_path: Path to the corrections data file
    """
    logger.info(f"Processing corrections file: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Process corrections
        all_corrections = []
        for correction_data in data.get('ecfr_corrections', []):
            corrections = process_correction_data(correction_data)
            all_corrections.extend(corrections)
        
        if all_corrections:
            insert_corrections(all_corrections)
            logger.info(f"Inserted {len(all_corrections)} corrections")
        
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
    
    for filename in os.listdir(input_dir):
        if not filename.endswith(".json") or not filename.startswith("corrections-"):
            continue
        
        file_path = os.path.join(input_dir, filename)
        process_corrections_file(file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process corrections data files')
    parser.add_argument('file', nargs='?', help='Single corrections file to process. If not provided, processes all files for latest date.')
    parser.add_argument('--date', help='Date of the files to process (YYYY-MM-DD)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    # Set logging level based on verbose flag
    if not args.verbose:
        logger.setLevel(logging.INFO)
    
    ensure_directory_exists(PROCESSED_DATA_DIR)
    
    if args.file:
        # Process single file
        process_corrections_file(args.file)
    else:
        # Process all files for specified date
        process_all_corrections(args.date) 