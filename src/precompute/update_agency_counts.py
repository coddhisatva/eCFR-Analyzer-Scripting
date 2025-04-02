#!/usr/bin/env python3
"""
Script to update agency num_cfr_refs and num_children counts from JSON data.
First zeros out all counts, then reads from JSON to set correct values.
"""
import logging
import json
from typing import Dict
from src.database.connector import get_supabase_client

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def zero_out_counts():
    """Set all agency counts to 0"""
    client = get_supabase_client()
    
    # Update all agencies to have 0 counts
    client.table('agencies').update({
        'num_children': 0,
        'num_cfr_refs': 0
    }).neq('id', '').execute()  # Update all rows where id is not empty
    logger.info("Reset all agency counts to 0")

def update_agency_counts():
    """Update num_cfr_refs and num_children for agencies based on JSON data"""
    client = get_supabase_client()
    
    # Read the JSON file
    with open('data/raw/agencies/2025-03-31/agencies.json', 'r') as f:
        agencies_data = json.load(f)
        agencies_list = agencies_data.get('agencies', [])  # Get the agencies list from the JSON
    
    # Process each agency
    for agency in agencies_list:
        slug = agency.get('slug')
        if not slug:
            logger.warning(f"Agency missing slug: {agency}")
            continue
        
        # Count children and CFR references from JSON
        num_children = len(agency.get('children', []))
        num_cfr_refs = len(agency.get('cfr_references', []))
        
        # Update agency in database
        result = client.table('agencies').update({
            'num_children': num_children,
            'num_cfr_refs': num_cfr_refs
        }).eq('id', slug).execute()
        
        if result.data:
            logger.info(f"Updated agency {slug}: {num_children} children, {num_cfr_refs} CFR refs")
        else:
            logger.warning(f"Could not find agency with id {slug}")

def main():
    """Main function to update agency counts"""
    # First zero out all counts
    zero_out_counts()
    
    # Then update with correct counts from JSON
    update_agency_counts()

if __name__ == "__main__":
    main() 