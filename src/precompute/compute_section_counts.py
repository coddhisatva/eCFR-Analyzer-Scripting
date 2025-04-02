#!/usr/bin/env python3
"""
Script to compute and update section counts for all nodes in the hierarchy.
Works bottom-up, starting from sections and computing parent section counts
as the sum of their children's section counts.
"""
import logging
from typing import List, Dict, Any, Optional
from src.database.connector import get_supabase_client

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Batch size for updates
BATCH_SIZE = 1000

def get_section_nodes():
    """Get all section nodes (nodes with level_type = 'section')"""
    client = get_supabase_client()
    
    # Get nodes that are sections
    result = client.table('nodes').select('id', 'num_sections').eq('level_type', 'section').execute()
    return result.data

def get_children(node_id: str) -> List[Dict[str, Any]]:
    """Get all children of a node"""
    client = get_supabase_client()
    
    result = client.table('nodes').select('id', 'num_sections').eq('parent', node_id).execute()
    return result.data

def get_parent_id(node_id: str) -> Optional[str]:
    """Get the parent ID of a node"""
    client = get_supabase_client()
    
    result = client.table('nodes').select('parent').eq('id', node_id).execute()
    return result.data[0]['parent'] if result.data else None

def compute_node_section_count(node_id: str) -> int:
    """
    Compute section count for a node by summing its children's section counts.
    Returns 0 if no children have section counts.
    """
    children = get_children(node_id)
    total_sections = 0
    
    for child in children:
        total_sections += child.get('num_sections', 0)
    
    return total_sections

def process_level(node_ids: List[str]):
    """Process a level of nodes, computing and updating their section counts"""
    # Group nodes by parent
    parent_groups: Dict[str, List[str]] = {}
    for node_id in node_ids:
        parent_id = get_parent_id(node_id)
        if parent_id:
            parent_groups.setdefault(parent_id, []).append(node_id)
    
    # Process each parent
    updates = []
    for parent_id in parent_groups:
        section_count = compute_node_section_count(parent_id)
        if section_count > 0:
            updates.append({
                'id': parent_id,
                'num_sections': section_count
            })
        
        # Process batch if we have enough updates
        if len(updates) >= BATCH_SIZE:
            client = get_supabase_client()
            client.table('nodes').upsert(updates).execute()
            logger.info(f"Updated {len(updates)} nodes")
            updates = []
    
    # Process remaining updates
    if updates:
        client = get_supabase_client()
        client.table('nodes').upsert(updates).execute()
        logger.info(f"Updated {len(updates)} nodes")
    
    return list(parent_groups.keys())

def main():
    """Main function to compute all section counts"""
    # Start with section nodes
    section_nodes = get_section_nodes()
    current_level = [node['id'] for node in section_nodes]
    logger.info(f"Starting with {len(current_level)} section nodes")
    
    # Process each level up the tree until no more parents
    level = 1
    while current_level:
        logger.info(f"Processing level {level}: {len(current_level)} nodes")
        current_level = process_level(current_level)
        level += 1
    
    logger.info("Finished computing section counts")

if __name__ == "__main__":
    main() 