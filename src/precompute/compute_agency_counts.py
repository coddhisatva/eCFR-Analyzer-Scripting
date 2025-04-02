#!/usr/bin/env python3
"""
Script to compute and update word and section counts for agencies based on their node references.
Processes in batches to avoid timeouts.
"""
import logging
from typing import List, Dict, Any
from src.database.connector import get_supabase_client

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Batch size for updates
BATCH_SIZE = 1000

def get_agency_node_mappings():
    """Get all agency-node mappings"""
    client = get_supabase_client()
    
    result = client.table('agency_node_mappings').select('agency_id', 'node_id').execute()
    return result.data

def get_node_counts(node_ids: List[str]) -> Dict[str, Dict[str, int]]:
    """Get word and section counts for a list of nodes"""
    client = get_supabase_client()
    
    # Split into batches to avoid too many IN clauses
    node_counts = {}
    for i in range(0, len(node_ids), BATCH_SIZE):
        batch = node_ids[i:i + BATCH_SIZE]
        result = client.table('nodes').select('id', 'num_words', 'num_sections').in_('id', batch).execute()
        for node in result.data:
            node_counts[node['id']] = {
                'num_words': node.get('num_words', 0),
                'num_sections': node.get('num_sections', 0)
            }
    
    return node_counts

def compute_agency_counts():
    """Compute and update word and section counts for all agencies"""
    client = get_supabase_client()
    
    # Get all agency-node mappings
    mappings = get_agency_node_mappings()
    logger.info(f"Found {len(mappings)} agency-node mappings")
    
    # Group by agency
    agency_nodes: Dict[str, List[str]] = {}
    for mapping in mappings:
        agency_id = mapping['agency_id']
        node_id = mapping['node_id']
        agency_nodes.setdefault(agency_id, []).append(node_id)
    
    # Process agencies in batches
    updates = []
    for agency_id, node_ids in agency_nodes.items():
        # Get counts for all nodes
        node_counts = get_node_counts(node_ids)
        
        # Sum counts
        total_words = sum(counts['num_words'] for counts in node_counts.values())
        total_sections = sum(counts['num_sections'] for counts in node_counts.values())
        
        updates.append({
            'id': agency_id,
            'num_words': total_words,
            'num_sections': total_sections
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
    
    logger.info("Finished computing agency counts")

def main():
    """Main function to compute all agency counts"""
    compute_agency_counts()

if __name__ == "__main__":
    main() 