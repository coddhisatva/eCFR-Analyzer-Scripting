#!/usr/bin/env python3
"""
Script to compute and update correction counts for nodes and agencies.
For nodes: Counts exact matches only.
For agencies: Uses agency_node_mappings_node_idx to count all corrections.
"""
import logging
from typing import List, Dict, Any
from src.database.connector import get_supabase_client

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_node_correction_count(node_id: str) -> int:
    """Get the number of corrections for a specific node (exact matches only)"""
    client = get_supabase_client()
    
    result = client.table('corrections').select('id').eq('node_id', node_id).execute()
    return len(result.data)

def update_node_correction_count(node_id: str, count: int):
    """Update a node's correction count in its metadata"""
    client = get_supabase_client()
    
    # Get current metadata
    result = client.table('nodes').select('metadata').eq('id', node_id).execute()
    if not result.data:
        logger.warning(f"Node {node_id} not found")
        return
        
    metadata = result.data[0].get('metadata', {})
    metadata['correction_count'] = count
    
    # Update metadata
    client.table('nodes').update({'metadata': metadata}).eq('id', node_id).execute()
    logger.info(f"Updated correction count for {node_id}: {count}")

def compute_agency_correction_counts():
    """Compute and update correction counts for agencies using the index"""
    client = get_supabase_client()
    
    # Get all corrections
    corrections_result = client.table('corrections').select('node_id').execute()
    
    # Initialize agency counts
    agency_counts: Dict[str, int] = {}
    
    # For each correction, find related agencies using the index
    for correction in corrections_result.data:
        node_id = correction['node_id']
        
        # Use the index to find agency mappings
        mappings_result = client.table('agency_node_mappings').select('agency_id').eq('node_id', node_id).execute()
        
        # Increment count for each related agency
        for mapping in mappings_result.data:
            agency_id = mapping['agency_id']
            agency_counts[agency_id] = agency_counts.get(agency_id, 0) + 1
    
    # Update agencies with their counts
    for agency_id, count in agency_counts.items():
        client.table('agencies').update({'num_corrections': count}).eq('id', agency_id).execute()
        logger.info(f"Updated correction count for agency {agency_id}: {count}")

def process_all_nodes():
    """Process all nodes to compute their correction counts"""
    client = get_supabase_client()
    
    # Get all nodes
    result = client.table('nodes').select('id').execute()
    nodes = result.data
    
    # Process each node
    for node in nodes:
        node_id = node['id']
        count = get_node_correction_count(node_id)
        update_node_correction_count(node_id, count)

def main():
    """Main function to compute all correction counts"""
    # Process all nodes
    process_all_nodes()
    
    # Update agency correction counts
    compute_agency_correction_counts()

if __name__ == "__main__":
    main() 