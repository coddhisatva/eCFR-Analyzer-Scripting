#!/usr/bin/env python3
"""
Script to compute and update correction counts for agencies.
Processes in batches to avoid timeouts.
"""
import logging
from typing import Dict, List, Any
from src.database.connector import get_supabase_client

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Batch size for updates
BATCH_SIZE = 1000

def get_agency_corrections(agency_id: str) -> List[Dict[str, Any]]:
    """Get all corrections for an agency"""
    client = get_supabase_client()
    result = client.table('corrections').select('*').eq('agency_id', agency_id).execute()
    return result.data

def compute_agency_corrections():
    """Compute and update correction counts for all agencies"""
    client = get_supabase_client()
    
    # Get all agencies
    result = client.table('agencies').select('id').execute()
    agencies = result.data
    logger.info(f"Found {len(agencies)} agencies to process")
    
    # Process in batches
    updates = []
    for agency in agencies:
        agency_id = agency['id']
        corrections = get_agency_corrections(agency_id)
        
        updates.append({
            'id': agency_id,
            'num_corrections': len(corrections)
        })
        
        # Process batch if we have enough updates
        if len(updates) >= BATCH_SIZE:
            client.table('agencies').upsert(updates).execute()
            logger.info(f"Updated {len(updates)} agencies")
            updates = []
    
    # Process remaining updates
    if updates:
        client.table('agencies').upsert(updates).execute()
        logger.info(f"Updated {len(updates)} agencies")
    
    logger.info("Finished computing agency correction counts")

def main():
    """Main function to compute all agency correction counts"""
    compute_agency_corrections()

if __name__ == "__main__":
    main() 