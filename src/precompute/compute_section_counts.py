#!/usr/bin/env python3
"""
Script to compute and update section counts for nodes and agencies.
For nodes: Counts sections at each level and propagates up the tree.
For agencies: Counts sections for all related nodes.
"""
import logging
from typing import List, Dict, Any
from src.database.connector import get_supabase_client

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

def compute_node_section_count(node_id: str) -> int:
    """
    Compute section count for a node by counting sections in its subtree.
    A node is a section if it has 'section=' in its ID.
    """
    # Count this node if it's a section
    total_sections = 1 if is_section(node_id) else 0
    
    # Add sections from children
    children = get_children(node_id)
    for child in children:
        child_count = compute_node_section_count(child['id'])
        total_sections += child_count
    
    return total_sections

def update_node_section_count(node_id: str, count: int):
    """Update a node's section count in its metadata"""
    client = get_supabase_client()
    
    # Get current metadata
    result = client.table('nodes').select('metadata').eq('id', node_id).execute()
    if not result.data:
        logger.warning(f"Node {node_id} not found")
        return
        
    metadata = result.data[0].get('metadata', {})
    metadata['section_count'] = count
    
    # Update metadata
    client.table('nodes').update({'metadata': metadata}).eq('id', node_id).execute()
    logger.info(f"Updated section count for {node_id}: {count}")

def compute_agency_section_counts():
    """Compute and update section counts for agencies based on their CFR relationships"""
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
    
    # Compute and update section counts for each agency
    for agency_id, node_ids in agency_nodes.items():
        total_sections = 0
        
        # For each node, get its section count from metadata
        nodes_result = client.table('nodes').select('metadata').in_('id', node_ids).execute()
        for node in nodes_result.data:
            section_count = node.get('metadata', {}).get('section_count', 0)
            if isinstance(section_count, str):
                section_count = int(section_count)
            total_sections += section_count
        
        # Update agency
        client.table('agencies').update({'num_sections': total_sections}).eq('id', agency_id).execute()
        logger.info(f"Updated section count for agency {agency_id}: {total_sections}")

def process_all_nodes():
    """Process all nodes to compute their section counts"""
    client = get_supabase_client()
    
    # Get all root nodes (us/federal/ecfr/title=X)
    result = client.table('nodes').select('id').like('id', 'us/federal/ecfr/title=%').execute()
    root_nodes = result.data
    
    # Process each root node and its subtree
    for node in root_nodes:
        node_id = node['id']
        logger.info(f"Processing root node {node_id}")
        count = compute_node_section_count(node_id)
        update_node_section_count(node_id, count)

def main():
    """Main function to compute all section counts"""
    # Process all nodes
    process_all_nodes()
    
    # Update agency section counts
    compute_agency_section_counts()

if __name__ == "__main__":
    main() 