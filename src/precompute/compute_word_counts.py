#!/usr/bin/env python3
"""
Script to compute and update word counts for all nodes in the hierarchy.
Works bottom-up, starting from leaf nodes and computing parent word counts
as the sum of their children's word counts.
"""
import logging
from typing import List, Dict, Any
from src.database.connector import get_supabase_client

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_leaf_nodes():
    """Get all leaf nodes (nodes with word_count in metadata but no children)"""
    client = get_supabase_client()
    
    # Get nodes that have word_count in metadata
    result = client.table('nodes').select('id', 'metadata').not_.is_('metadata->>word_count', 'null').execute()
    return result.data

def get_parent_id(node_id: str) -> str:
    """Get the parent ID of a node by removing the last path component"""
    parts = node_id.split('/')
    if len(parts) <= 1:
        return None
    return '/'.join(parts[:-1])

def get_children(parent_id: str):
    """Get all immediate children of a node"""
    client = get_supabase_client()
    
    # Use LIKE to match immediate children (one level down)
    result = client.table('nodes').select('id', 'metadata').ilike('id', f"{parent_id}/%").execute()
    return [node for node in result.data if get_parent_id(node['id']) == parent_id]

def compute_node_word_count(node_id: str) -> int:
    """
    Compute word count for a node by summing its children's word counts.
    Returns 0 if no children have word counts.
    """
    children = get_children(node_id)
    total_words = 0
    
    for child in children:
        # Get word count from metadata
        child_count = child.get('metadata', {}).get('word_count', 0)
        if isinstance(child_count, str):
            child_count = int(child_count)
        total_words += child_count
    
    return total_words

def update_node_word_count(node_id: str, word_count: int):
    """Update a node's word count in its metadata"""
    client = get_supabase_client()
    
    # Get current metadata
    result = client.table('nodes').select('metadata').eq('id', node_id).execute()
    if not result.data:
        logger.warning(f"Node {node_id} not found")
        return
        
    metadata = result.data[0].get('metadata', {})
    metadata['word_count'] = word_count
    
    # Update metadata
    client.table('nodes').update({'metadata': metadata}).eq('id', node_id).execute()
    logger.info(f"Updated word count for {node_id}: {word_count}")

def process_level(node_ids: List[str]):
    """Process a level of nodes, computing and updating their word counts"""
    # Group nodes by parent
    parent_groups: Dict[str, List[str]] = {}
    for node_id in node_ids:
        parent_id = get_parent_id(node_id)
        if parent_id:
            parent_groups.setdefault(parent_id, []).append(node_id)
    
    # Process each parent
    processed_parents = []
    for parent_id in parent_groups:
        word_count = compute_node_word_count(parent_id)
        if word_count > 0:
            update_node_word_count(parent_id, word_count)
            processed_parents.append(parent_id)
    
    return processed_parents

def compute_agency_word_counts():
    """Compute and update word counts for agencies based on their CFR relationships"""
    client = get_supabase_client()
    
    # Get all agency-node mappings
    result = client.table('agency_node_mappings').select('agency_id', 'node_id').execute()
    mappings = result.data
    
    # Group by agency
    agency_nodes: Dict[str, List[str]] = {}
    for mapping in mappings:
        agency_id = mapping['agency_id']
        node_id = mapping['node_id']
        agency_nodes.setdefault(agency_id, []).append(node_id)
    
    # Compute and update word counts for each agency
    for agency_id, node_ids in agency_nodes.items():
        total_words = 0
        
        # Get word counts for all nodes
        nodes_result = client.table('nodes').select('metadata').in_('id', node_ids).execute()
        for node in nodes_result.data:
            word_count = node.get('metadata', {}).get('word_count', 0)
            if isinstance(word_count, str):
                word_count = int(word_count)
            total_words += word_count
        
        # Update agency
        client.table('agencies').update({'num_words': total_words}).eq('id', agency_id).execute()
        logger.info(f"Updated word count for agency {agency_id}: {total_words}")

def main():
    """Main function to compute all word counts"""
    # Start with leaf nodes
    leaf_nodes = get_leaf_nodes()
    current_level = [node['id'] for node in leaf_nodes]
    
    # Process each level up the tree until no more parents
    while current_level:
        logger.info(f"Processing {len(current_level)} nodes")
        current_level = process_level(current_level)
    
    # Update agency word counts
    compute_agency_word_counts()

if __name__ == "__main__":
    main() 