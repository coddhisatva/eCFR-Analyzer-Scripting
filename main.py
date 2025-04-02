#!/usr/bin/env python
"""
Main script for eCFR Analyzer
"""
import os
import argparse
import sys
import logging
from datetime import datetime

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.data_collection.download_xml import download_all_titles
from src.data_processing.unified_processor import process_all_data

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description='Process eCFR data')
    parser.add_argument('--download', action='store_true', help='Download XML files')
    parser.add_argument('--process', action='store_true', help='Process downloaded files')
    parser.add_argument('--date', type=str, help='Date to process (YYYY-MM-DD)')
    
    args = parser.parse_args()
    
    # Set default date
    if args.date is None:
        args.date = datetime.now().strftime("%Y-%m-%d")
    
    # Download data if requested
    if args.download:
        logger.info("Downloading files...")
        download_all_titles(args.date)
    
    # Process data if requested
    if args.process:
        logger.info("Processing downloaded files...")
        process_all_data(args.date)

if __name__ == "__main__":
    main() 