#!/usr/bin/env python
"""
Main script for eCFR Analyzer
"""
import os
import argparse
import sys
from datetime import datetime

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.data_collection.download_xml import download_all_titles
from src.data_processing.process_xml import process_all_titles, process_title_xml

def main():
    """
    Main entry point for the eCFR Analyzer
    """
    parser = argparse.ArgumentParser(description="eCFR Analyzer")
    parser.add_argument("--download", action="store_true", help="Download XML files")
    parser.add_argument("--process", action="store_true", help="Process XML files")
    parser.add_argument("--date", type=str, default=None, help="Date to process (YYYY-MM-DD)")
    parser.add_argument("--title", type=int, default=None, help="Specific title to process")
    
    args = parser.parse_args()
    
    # Set default date
    if args.date is None:
        args.date = datetime.now().strftime("%Y-%m-%d")
    
    # Download XML files
    if args.download:
        if args.title:
            from src.data_collection.download_xml import download_title_xml
            download_title_xml(args.title, args.date)
        else:
            download_all_titles(args.date)
    
    # Process XML files
    if args.process:
        if args.title:
            # Process specific title
            xml_file = os.path.join("data", "raw", args.date, f"title-{args.title}.xml")
            if os.path.exists(xml_file):
                nodes = process_title_xml(xml_file)
                if nodes:
                    from src.database.connector import insert_nodes
                    insert_nodes(nodes)
                    print(f"Successfully processed and inserted nodes for Title {args.title}")
            else:
                print(f"Error: XML file for Title {args.title} not found at {xml_file}")
        else:
            process_all_titles(args.date)
    
    # If no action specified, show help
    if not args.download and not args.process:
        parser.print_help()

if __name__ == "__main__":
    main()