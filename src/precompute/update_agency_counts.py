#!/usr/bin/env python3
"""
Script to update agency num_cfr_refs and num_children counts directly from source data.
This is a simpler approach than traversing the node tree.
"""
import logging
from typing import Dict
import json
from src.database.connector import get_supabase_client

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def update_agency_counts():
    """Update num_cfr_refs and num_children for agencies based on source data"""
    client = get_supabase_client()
    
    # Get all agencies
    agencies_result = client.table('agencies').select('id', 'source_data').execute()
    
    for agency in agencies_result.data:
        agency_id = agency['id']
        source_data = agency['source_data']
        
        # Count number of children (direct relationships)
        num_children = len(source_data.get('relationships', []))
        
        # Count number of CFR references
        num_cfr_refs = len(source_data.get('cfr_refs', []))
        
        # Update agency with counts
        client.table('agencies').update({
            'num_children': num_children,
            'num_cfr_refs': num_cfr_refs
        }).eq('id', agency_id).execute()
        
        logger.info(f"Updated agency {agency_id}: {num_children} children, {num_cfr_refs} CFR refs")

def main():
    """Main function to update agency counts"""
    update_agency_counts()

if __name__ == "__main__":
    main() 