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

# Directory for raw and processed data
RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "raw", "corrections")
PROCESSED_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "processed", "corrections")

# API Base URL
API_BASE_URL = "https://www.ecfr.gov/api/admin/v1"

def ensure_directory_exists(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def clean_text(text: str) -> str:
    """Clean and normalize text."""
    if text is None:
        return ""
    return text.strip()

def download_corrections_for_title(title: str) -> Optional[Dict[str, Any]]:
    """
    Download corrections data for a specific title from eCFR API
    
    Args:
        title: Title number to download corrections for
        
    Returns:
        Dictionary containing corrections data, or None if download failed
    """
    url = f"{API_BASE_URL}/corrections/title/{title}.json"
    logger.info(f"Downloading corrections from: {url}")
    
    try:
        response = requests.get(url, headers={"accept": "application/json"})
        response.raise_for_status()
        return response.json()
        
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
    
    # List of titles to download (1-50 excluding skipped titles)
    skip_titles = {0}  # Add any titles to skip
    titles = [str(i) for i in range(1, 51) if i not in skip_titles]
    
    for title in titles:
        logger.info(f"Downloading corrections for title: {title}")
        
        # Download corrections data
        data = download_corrections_for_title(title)
        if data:
            # Save to file
            file_path = os.path.join(date_dir, f"corrections-title-{title}.json")
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            logger.info(f"Saved corrections data to {file_path}")
            
            # Log number of corrections found
            num_corrections = len(data.get('ecfr_corrections', []))
            logger.info(f"Found {num_corrections} corrections for title {title}")
        else:
            logger.warning(f"No corrections data retrieved for title {title}")

def download_corrections(title: int, date=None):
    """
    Download corrections data for a specific title from the eCFR API.
    
    Args:
        title: The CFR title number to download corrections for
        date: The date to use for the data (default: current date)
    """
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    
    # Create date directory
    date_dir = os.path.join(RAW_DATA_DIR, date)
    ensure_directory_exists(date_dir)
    
    # Download corrections data
    url = f"https://www.ecfr.gov/api/admin/v1/corrections/title/{title}.json"
    logger.info(f"Downloading corrections for title {title} from: {url}")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Save raw data
        output_file = os.path.join(date_dir, f"corrections-title-{title}.json")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(response.json(), f, indent=2)
        
        logger.info(f"Saved corrections data to {output_file}")
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Error downloading corrections for title {title}: {e}")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download corrections data from eCFR API')
    parser.add_argument('--date', help='Date to download data for (YYYY-MM-DD)', 
                       default=datetime.now().strftime("%Y-%m-%d"))
    parser.add_argument('--title', help='Specific title to download (optional)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    # Set logging level based on verbose flag
    if not args.verbose:
        logger.setLevel(logging.INFO)
    
    ensure_directory_exists(RAW_DATA_DIR)
    ensure_directory_exists(PROCESSED_DATA_DIR)
    
    if args.title:
        # Download single title
        logger.info(f"Downloading corrections for title {args.title}")
        data = download_corrections_for_title(args.title)
        if data:
            file_path = os.path.join(RAW_DATA_DIR, args.date, f"corrections-title-{args.title}.json")
            ensure_directory_exists(os.path.dirname(file_path))
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            logger.info(f"Saved corrections data to {file_path}")
    else:
        # Download all titles
        download_all_corrections(args.date) 