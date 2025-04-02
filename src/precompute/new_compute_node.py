#!/usr/bin/env python3
"""
Script to compute and update word counts and section counts for nodes and agencies.
Combines both calculations into a single tree traversal for efficiency.
"""
import logging
from typing import List, Dict, Any, Tuple
from src.database.connector import get_supabase_client

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Batch size for updates
BATCH_SIZE = 1000
node_updates = []

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
    result = client.table('nodes').select('id').ilike('id', f"{parent_id}/%").execute()
    return [node for node in result.data if get_parent_id(node['id']) == parent_id]

def is_section(node_id: str) -> bool:
    """Check if a node is a section by looking for 'section=' in its ID"""
    return 'section=' in node_id

def batch_update_nodes():
    """Update nodes in batches"""
    global node_updates
    if not node_updates:
        return
        
    client = get_supabase_client()
    batch = node_updates[:BATCH_SIZE]
    node_updates = node_updates[BATCH_SIZE:]
    
    for update in batch:
        client.table('nodes').update({'metadata': update['metadata']}).eq('id', update['id']).execute()
        logger.info(f"Updated counts for {update['id']}: {update['metadata']['word_count']} words, {update['metadata']['section_count']} sections")

def compute_node_counts(node_id: str) -> Tuple[int, int]:
    """
    Compute both word count and section count for a node.
    Returns (word_count, section_count).
    """
    global node_updates
    client = get_supabase_client()
    
    # Get current metadata
    result = client.table('nodes').select('metadata').eq('id', node_id).execute()
    if not result.data:
        logger.warning(f"Node {node_id} not found")
        return 0, 0
        
    metadata = result.data[0].get('metadata', {})
    
    # Get direct word count from metadata
    word_count = metadata.get('word_count', 0)
    
    # Initialize section count
    section_count = 1 if is_section(node_id) else 0
    
    # Add counts from children
    children = get_children(node_id)
    for child in children:
        child_words, child_sections = compute_node_counts(child['id'])
        word_count += child_words
        section_count += child_sections
    
    # Update metadata with both counts
    metadata['word_count'] = word_count
    metadata['section_count'] = section_count
    
    # Queue update
    node_updates.append({'id': node_id, 'metadata': metadata})
    
    # If we have enough updates, process them
    if len(node_updates) >= BATCH_SIZE:
        batch_update_nodes()
    
    return word_count, section_count

def update_agency_counts():
    """Update word and section counts for agencies based on their CFR relationships"""
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
    
    # Update counts for each agency
    for agency_id, node_ids in agency_nodes.items():
        # Get word and section counts for all nodes
        total_words = 0
        total_sections = 0
        
        # Get metadata for all nodes in one query
        node_ids_str = "','".join(node_ids)
        result = client.table('nodes').select('metadata').in_('id', node_ids).execute()
        
        for node_data in result.data:
            metadata = node_data.get('metadata', {})
            total_words += metadata.get('word_count', 0)
            total_sections += metadata.get('section_count', 0)
        
        # Update agency
        client.table('agencies').update({
            'num_words': total_words,
            'num_sections': total_sections
        }).eq('id', agency_id).execute()
        logger.info(f"Updated counts for agency {agency_id}: {total_words} words, {total_sections} sections")

def process_all_nodes():
    """Process all nodes to compute their counts"""
    global node_updates
    client = get_supabase_client()
    
    # Get all root nodes (us/federal/ecfr/title=X)
    result = client.table('nodes').select('id').like('id', 'us/federal/ecfr/title=%').execute()
    root_nodes = result.data
    
    # Process each root node and its subtree
    for node in root_nodes:
        node_id = node['id']
        logger.info(f"Processing root node {node_id}")
        compute_node_counts(node_id)
    
    # Process any remaining updates
    while node_updates:
        batch_update_nodes()

def main():
    """Main function to compute all counts"""
    # Process all nodes
    process_all_nodes()
    
    # Update agency counts
    update_agency_counts()

if __name__ == "__main__":
    main() 