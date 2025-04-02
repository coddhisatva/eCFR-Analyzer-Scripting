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

# Directory for raw data
RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "raw")

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

def download_all_agencies(date: str):
    """
    Download all agency data for a specific date
    
    Args:
        date: The date to download data for (YYYY-MM-DD)
    """
    # Create directory for the date
    date_dir = os.path.join(RAW_DATA_DIR, date)
    ensure_directory_exists(date_dir)
    
    # Download from the agencies endpoint
    url = f"{API_BASE_URL}/agencies.json"
    logger.info(f"Downloading agencies from: {url}")
    
    try:
        response = requests.get(url, headers={"accept": "application/json"})
        response.raise_for_status()
        data = response.json()
        
        # Save the complete agency data
        file_path = os.path.join(date_dir, "agencies.json")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        logger.info(f"Saved agency data to {file_path}")
        
        # Also save individual agency files for easier processing
        for agency in data.get('agencies', []):
            agency_id = agency.get('id')
            if agency_id:
                agency_file = os.path.join(date_dir, f"agency-{agency_id}.json")
                with open(agency_file, 'w', encoding='utf-8') as f:
                    json.dump(agency, f, indent=2, ensure_ascii=False)
                logger.info(f"Saved individual agency data to {agency_file}")
            
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
    
    download_all_agencies(args.date) 