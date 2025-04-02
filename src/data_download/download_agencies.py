#!/usr/bin/env python
"""
Script to download agency data from eCFR API
"""
import os
import json
import logging
import requests
from datetime import datetime
from typing import Dict, Any, Optional, List
import argparse

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Directory for raw and processed data
RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "raw", "agencies")
PROCESSED_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "processed", "agencies")

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

def download_agencies(date=None):
    """
    Download agency data from the eCFR API.
    
    Args:
        date: The date to use for the data (default: current date)
    """
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    
    # Create date directory
    date_dir = os.path.join(RAW_DATA_DIR, date)
    ensure_directory_exists(date_dir)
    
    # Download agencies data
    url = "https://www.ecfr.gov/api/admin/v1/agencies.json"
    logger.info(f"Downloading agencies from: {url}")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Save raw data
        output_file = os.path.join(date_dir, "agencies.json")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(response.json(), f, indent=2)
        
        logger.info(f"Saved agency data to {output_file}")
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Error downloading agencies: {e}")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download agency data from eCFR API')
    parser.add_argument('--date', help='Date to download data for (YYYY-MM-DD)', 
                       default=datetime.now().strftime("%Y-%m-%d"))
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    # Set logging level based on verbose flag
    if not args.verbose:
        logger.setLevel(logging.INFO)
    
    download_agencies(args.date) 