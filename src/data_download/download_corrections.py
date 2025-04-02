#!/usr/bin/env python
"""
Script to download corrections data from eCFR API
"""
import os
import json
import logging
import requests
from datetime import datetime
from typing import Dict, Any, List, Optional
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

def download_corrections_for_title(title: str, date: str) -> Optional[List[Dict[str, Any]]]:
    """
    Download corrections data for a specific title from eCFR API
    
    Args:
        title: Title number to download corrections for
        date: Date to download corrections for (YYYY-MM-DD)
        
    Returns:
        List of correction data dictionaries, or None if download failed
    """
    # TODO: Replace with actual API endpoint
    url = f"https://api.ecfr.gov/v1/corrections/title/{title}"
    
    try:
        response = requests.get(url, params={'date': date})
        response.raise_for_status()
        data = response.json()
        
        # Clean and normalize the corrections
        cleaned_corrections = []
        for correction in data.get('corrections', []):
            cleaned_correction = {
                'node_id': correction.get('node_id'),
                'title': title,
                'corrective_action': clean_text(correction.get('corrective_action', '')),
                'error_corrected': correction.get('error_corrected', ''),
                'error_occurred': correction.get('error_occurred', ''),
                'fr_citation': clean_text(correction.get('fr_citation', '')),
                'position': clean_text(correction.get('position', '')),
                'year': correction.get('year'),
                'notes': clean_text(correction.get('notes', ''))
            }
            cleaned_corrections.append(cleaned_correction)
        
        return cleaned_corrections
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Error downloading corrections for title {title}: {e}")
        return None

def download_all_corrections(date: str):
    """
    Download all corrections data for a specific date
    
    Args:
        date: The date to download data for (YYYY-MM-DD)
    """
    # Create directory for the date
    date_dir = os.path.join(RAW_DATA_DIR, date)
    ensure_directory_exists(date_dir)
    
    # TODO: Replace with actual list of titles
    titles = [
        "1", "2", "3", "4", "5",  # Example titles
        # Add more titles as needed
    ]
    
    for title in titles:
        logger.info(f"Downloading corrections for title: {title}")
        
        # Download corrections data
        corrections = download_corrections_for_title(title, date)
        if corrections:
            # Save to file
            file_path = os.path.join(date_dir, f"corrections-title-{title}.json")
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump({'corrections': corrections}, f, indent=2, ensure_ascii=False)
            logger.info(f"Saved corrections data to {file_path}")
        else:
            logger.error(f"Failed to download corrections for title: {title}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download corrections data from eCFR API')
    parser.add_argument('--date', help='Date to download data for (YYYY-MM-DD)', 
                       default=datetime.now().strftime("%Y-%m-%d"))
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    # Set logging level based on verbose flag
    if not args.verbose:
        logger.setLevel(logging.INFO)
    
    download_all_corrections(args.date) 