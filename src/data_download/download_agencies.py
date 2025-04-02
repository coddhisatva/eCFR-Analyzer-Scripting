#!/usr/bin/env python
"""
Script to download agency data from eCFR API
"""
import os
import json
import logging
import requests
from datetime import datetime
from typing import Dict, Any, Optional
import argparse

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Directory for raw data
RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "raw")

def ensure_directory_exists(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def clean_text(text: str) -> str:
    """Clean and normalize text."""
    if text is None:
        return ""
    return text.strip()

def download_agency_data(agency_id: str) -> Optional[Dict[str, Any]]:
    """
    Download agency data from eCFR API
    
    Args:
        agency_id: ID of the agency to download
        
    Returns:
        Dictionary containing agency data, or None if download failed
    """
    # TODO: Replace with actual API endpoint
    url = f"https://api.ecfr.gov/v1/agencies/{agency_id}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Clean and normalize the data
        cleaned_data = {
            'id': agency_id,
            'name': clean_text(data.get('name', '')),
            'short_name': clean_text(data.get('short_name', '')),
            'display_name': clean_text(data.get('display_name', '')),
            'sortable_name': clean_text(data.get('sortable_name', '')),
            'description': clean_text(data.get('description', '')),
            'website': clean_text(data.get('website', '')),
            'contact_info': clean_text(data.get('contact_info', '')),
            'agency_type': data.get('agency_type', 'middle'),
            'children': [],
            'cfr_references': [],
            'node_mappings': []
        }
        
        # Process children recursively
        for child in data.get('children', []):
            child_data = download_agency_data(child['id'])
            if child_data:
                cleaned_data['children'].append(child_data)
        
        # Process CFR references
        for ref in data.get('cfr_references', []):
            cleaned_data['cfr_references'].append({
                'title': ref.get('title', ''),
                'subheading': clean_text(ref.get('subheading', '')),
                'is_primary': ref.get('is_primary', False),
                'node_id': ref.get('node_id')
            })
        
        # Process node mappings
        for mapping in data.get('node_mappings', []):
            cleaned_data['node_mappings'].append({
                'node_id': mapping.get('node_id'),
                'is_primary': mapping.get('is_primary', False),
                'is_direct_reference': mapping.get('is_direct_reference', True),
                'relationship_type': mapping.get('relationship_type', 'regulates'),
                'notes': clean_text(mapping.get('notes', ''))
            })
        
        return cleaned_data
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Error downloading agency {agency_id}: {e}")
        return None

def download_all_agencies(date: str):
    """
    Download all agency data for a specific date
    
    Args:
        date: The date to download data for (YYYY-MM-DD)
    """
    # Create directory for the date
    date_dir = os.path.join(RAW_DATA_DIR, date)
    ensure_directory_exists(date_dir)
    
    # TODO: Replace with actual list of agency IDs
    agency_ids = [
        "EPA",  # Environmental Protection Agency
        "FDA",  # Food and Drug Administration
        "FCC",  # Federal Communications Commission
        # Add more agency IDs as needed
    ]
    
    for agency_id in agency_ids:
        logger.info(f"Downloading data for agency: {agency_id}")
        
        # Download agency data
        data = download_agency_data(agency_id)
        if data:
            # Save to file
            file_path = os.path.join(date_dir, f"agency-{agency_id}.json")
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            logger.info(f"Saved agency data to {file_path}")
        else:
            logger.error(f"Failed to download data for agency: {agency_id}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download agency data from eCFR API')
    parser.add_argument('--date', help='Date to download data for (YYYY-MM-DD)', 
                       default=datetime.now().strftime("%Y-%m-%d"))
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    # Set logging level based on verbose flag
    if not args.verbose:
        logger.setLevel(logging.INFO)
    
    download_all_agencies(args.date) 