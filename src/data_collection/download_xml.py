#!/usr/bin/env python
"""
Script to download CFR XML files from the eCFR API
"""
import os
import requests
from datetime import datetime
import time
from tqdm import tqdm

# Directory to store downloaded XML files
RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "raw")

def ensure_directory_exists(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def download_title_xml(title_number, date=None):
    """
    Download the XML for a specific CFR title
    
    Args:
        title_number: The CFR title number
        date: The point-in-time date (default: 2024-03-28)
    
    Returns:
        Path to the downloaded XML file
    """
    if date is None:
        # Use most recent available date
        date = "2024-03-28"
    
    # Create the URL
    url = f"https://www.ecfr.gov/api/versioner/v1/full/{date}/title-{title_number}.xml"
    
    # Create the output file path
    output_dir = os.path.join(RAW_DATA_DIR, date)
    ensure_directory_exists(output_dir)
    output_file = os.path.join(output_dir, f"title-{title_number}.xml")
    
    # Download the file
    try:
        response = requests.get(url)
        if response.status_code == 404:
            print(f"Title {title_number} not found for date {date}. The API might not have data for this date.")
            return None
        response.raise_for_status()  # Raise exception for other HTTP errors
        
        with open(output_file, "wb") as f:
            f.write(response.content)
        
        print(f"Downloaded Title {title_number} XML to {output_file}")
        return output_file
    except requests.exceptions.RequestException as e:
        print(f"Error downloading Title {title_number}: {e}")
        return None

def download_all_titles(date=None, excluded_titles=[35]):
    """
    Download XML for all CFR titles, excluding the specified ones
    
    Args:
        date: The point-in-time date (default: 2024-03-28)
        excluded_titles: List of title numbers to exclude
    
    Returns:
        List of paths to downloaded XML files
    """
    if date is None:
        date = "2024-03-28"
    
    downloaded_files = []
    
    for title_number in tqdm(range(1, 51)):
        if title_number in excluded_titles:
            print(f"Skipping excluded Title {title_number}")
            continue
        
        file_path = download_title_xml(title_number, date)
        if file_path:
            downloaded_files.append(file_path)
        
        # Add a small delay to avoid overwhelming the API
        time.sleep(1)
    
    return downloaded_files

if __name__ == "__main__":
    ensure_directory_exists(RAW_DATA_DIR)
    download_all_titles()