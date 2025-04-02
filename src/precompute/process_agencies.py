#!/usr/bin/env python3
"""
Script to process agencies from XML files and update the database.
"""
import logging
import os
from typing import Dict, List, Any
from src.database.connector import get_supabase_client
from src.models.agency import Agency
from src.models.node import Node
from src.precompute.compute_agency_counts import get_node_counts

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Batch size for updates
BATCH_SIZE = 1000

def get_agency_nodes(agency_id: str) -> List[str]:
    """Get all nodes associated with an agency"""
    client = get_supabase_client()
    result = client.table('agency_node_mappings').select('node_id').eq('agency_id', agency_id).execute()
    return [mapping['node_id'] for mapping in result.data]

def compute_agency_metrics(agency_id: str) -> Dict[str, int]:
    """Compute metrics for an agency based on its nodes"""
    node_ids = get_agency_nodes(agency_id)
    if not node_ids:
        return {'num_words': 0, 'num_sections': 0, 'num_children': 0, 'num_cfr': 0}
    
    # Get node counts
    node_counts = get_node_counts(node_ids)
    
    # Sum counts
    total_words = sum(counts['num_words'] for counts in node_counts.values())
    total_sections = sum(counts['num_sections'] for counts in node_counts.values())
    
    # Count unique CFR references
    client = get_supabase_client()
    result = client.table('nodes').select('cfr_references').in_('id', node_ids).execute()
    cfr_refs = set()
    for node in result.data:
        if node.get('cfr_references'):
            cfr_refs.update(node['cfr_references'])
    
    return {
        'num_words': total_words,
        'num_sections': total_sections,
        'num_children': len(node_ids),
        'num_cfr': len(cfr_refs)
    }

def calculate_agency_depth(agency_id: str, depth_cache: Dict[str, int] = None) -> int:
    """Calculate depth of an agency by traversing up the parent chain"""
    if depth_cache is None:
        depth_cache = {}
    
    if agency_id in depth_cache:
        return depth_cache[agency_id]
    
    client = get_supabase_client()
    result = client.table('agencies').select('parent_id').eq('id', agency_id).execute()
    parent_id = result.data[0].get('parent_id') if result.data else None
    
    if not parent_id:
        depth_cache[agency_id] = 0
        return 0
    
    depth = calculate_agency_depth(parent_id, depth_cache) + 1
    depth_cache[agency_id] = depth
    return depth

def process_agencies():
    """Process all agencies and update their metrics"""
    client = get_supabase_client()
    
    # Get all agencies
    result = client.table('agencies').select('id', 'parent_id').execute()
    agencies = result.data
    logger.info(f"Found {len(agencies)} agencies to process")
    
    # Calculate depths for all agencies
    depth_cache = {}
    for agency in agencies:
        agency_id = agency['id']
        depth = calculate_agency_depth(agency_id, depth_cache)
        agency['depth'] = depth
    
    # Process in batches
    updates = []
    for agency in agencies:
        agency_id = agency['id']
        metrics = compute_agency_metrics(agency_id)
        
        updates.append({
            'id': agency_id,
            'depth': agency['depth'],
            **metrics
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
    
    logger.info("Finished processing agencies")

def main():
    """Main function to process all agencies"""
    process_agencies()

if __name__ == "__main__":
    main() 