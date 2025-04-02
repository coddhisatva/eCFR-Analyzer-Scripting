#!/usr/bin/env python
"""
Main script for eCFR data processing
"""
import os
import argparse
from datetime import datetime
import logging
from src.data_download.download_xml import download_title_xml
from src.data_download.download_agencies import download_all_agencies
from src.data_download.download_corrections import download_all_corrections
from src.data_processing.process_xml import process_all_titles
from src.data_processing.process_agencies import process_all_agencies
from src.data_processing.process_corrections import process_all_corrections

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description='Process eCFR data')
    parser.add_argument('--download', action='store_true', help='Download XML files')
    parser.add_argument('--download-agencies', action='store_true', help='Download agency data')
    parser.add_argument('--download-corrections', action='store_true', help='Download corrections data')
    parser.add_argument('--process', action='store_true', help='Process downloaded files')
    parser.add_argument('--date', help='Date to process (YYYY-MM-DD)', 
                       default=datetime.now().strftime("%Y-%m-%d"))
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    # Set logging level based on verbose flag
    if not args.verbose:
        logger.setLevel(logging.INFO)
    
    # Download data if requested
    if args.download:
        logger.info("Downloading XML files...")
        download_title_xml(args.date)
    
    if args.download_agencies:
        logger.info("Downloading agency data...")
        download_all_agencies(args.date)
    
    if args.download_corrections:
        logger.info("Downloading corrections data...")
        download_all_corrections(args.date)
    
    # Process data if requested
    if args.process:
        logger.info("Processing downloaded files...")
        
        # Process XML files
        logger.info("Processing XML files...")
        process_all_titles(args.date)
        
        # Process agency data
        logger.info("Processing agency data...")
        process_all_agencies(args.date)
        
        # Process corrections data
        logger.info("Processing corrections data...")
        process_all_corrections(args.date)

if __name__ == "__main__":
    main() 