#!/usr/bin/env python3
"""
Script to compute and update word counts and section counts for nodes and agencies.
Uses bulk operations and minimal memory footprint for efficiency.
"""
import os
import sys
import logging
from typing import Dict, List, Any, Tuple
from collections import defaultdict
import time

# Add src directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.database.connector import get_supabase_client
from src.utils.node_utils import is_section

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_total_counts():
    """Get total number of nodes and agencies for progress tracking"""
    client = get_supabase_client()
    
    # Get total nodes
    result = client.table('nodes').select('count', count='exact').execute()
    total_nodes = result.count
    
    # Get total agencies
    result = client.table('agencies').select('count', count='exact').execute()
    total_agencies = result.count
    
    return total_nodes, total_agencies

def reset_aggregated_counts():
    """Reset only aggregated counts (section_count and non-section word_counts)"""
    client = get_supabase_client()
    logger.info("Resetting aggregated counts...")
    
    # Get total for progress tracking
    total_nodes, _ = get_total_counts()
    
    # Reset counts in batches, preserving section-level word counts
    batch_size = 1000
    offset = 0
    start_time = time.time()
    
    while True:
        result = client.table('nodes').select('id', 'metadata').range(offset, offset + batch_size - 1).execute()
        if not result.data:
            break
            
        updates = []
        for node in result.data:
            node_id = node['id']
            metadata = node.get('metadata') or {}
            
            # If it's a section, preserve word_count but reset section_count
            if is_section(node_id):
                metadata['section_count'] = 0
            else:
                # For non-sections, reset both counts
                metadata['word_count'] = 0
                metadata['section_count'] = 0
                
            updates.append({
                'id': node_id,
                'metadata': metadata
            })
        
        client.table('nodes').upsert(updates).execute()
        offset += batch_size
        
        # Progress tracking
        progress = min(100, (offset / total_nodes) * 100)
        elapsed = time.time() - start_time
        rate = offset / elapsed if elapsed > 0 else 0
        eta = (total_nodes - offset) / rate if rate > 0 else 0
        
        logger.info(f"Reset progress: {progress:.1f}% ({offset}/{total_nodes}) - ETA: {eta:.1f}s")
    
    # Reset agency counts
    client.table('agencies').update({
        'num_words': 0,
        'num_sections': 0
    }).neq('id', '').execute()
    logger.info("Reset all agency counts")

def process_level(level_prefix: str = 'us/federal/ecfr/title=', batch_size: int = 1000):
    """Process nodes at a specific level, avoiding tree building"""
    client = get_supabase_client()
    
    # Get all nodes at this level
    result = client.table('nodes').select('id', 'metadata').like('id', f"{level_prefix}%").execute()
    nodes = result.data
    total_nodes = len(nodes)
    
    # Sort by ID length (shortest first) to ensure parents are processed before children
    nodes.sort(key=lambda x: len(x['id']))
    
    updates = []
    start_time = time.time()
    
    for idx, node in enumerate(nodes, 1):
        node_id = node['id']
        metadata = node.get('metadata') or {}
        
        # For sections, use existing word count
        if is_section(node_id):
            word_count = metadata.get('word_count', 0)
            section_count = 1
        else:
            # For non-sections, aggregate from children
            word_count = 0
            section_count = 0
            
            # Get immediate children's counts
            child_result = client.table('nodes').select('metadata').like('id', f"{node_id}/%").execute()
            for child in child_result.data:
                child_metadata = child.get('metadata') or {}
                word_count += child_metadata.get('word_count', 0)
                section_count += child_metadata.get('section_count', 0)
        
        # Prepare update
        metadata['word_count'] = word_count
        metadata['section_count'] = section_count
        updates.append({
            'id': node_id,
            'metadata': metadata
        })
        
        # Progress tracking
        if idx % 100 == 0:
            progress = (idx / total_nodes) * 100
            elapsed = time.time() - start_time
            rate = idx / elapsed if elapsed > 0 else 0
            eta = (total_nodes - idx) / rate if rate > 0 else 0
            logger.info(f"Processing progress: {progress:.1f}% ({idx}/{total_nodes}) - ETA: {eta:.1f}s")
        
        # Batch update when we reach batch_size
        if len(updates) >= batch_size:
            client.table('nodes').upsert(updates).execute()
            updates = []
    
    # Update remaining nodes
    if updates:
        client.table('nodes').upsert(updates).execute()

def update_agency_counts_bulk():
    """Update agency counts in bulk with minimal memory usage"""
    client = get_supabase_client()
    
    # Get total mappings for progress tracking
    result = client.table('agency_node_mappings').select('count', count='exact').execute()
    total_mappings = result.count
    
    # Process agency counts in batches
    batch_size = 1000
    offset = 0
    agency_counts = defaultdict(lambda: {'words': 0, 'sections': 0})
    start_time = time.time()
    
    while True:
        result = client.table('agency_node_mappings').select(
            'agency_id',
            'node_id',
            'nodes(metadata)'
        ).range(offset, offset + batch_size - 1).execute()
        
        if not result.data:
            break
            
        for mapping in result.data:
            agency_id = mapping['agency_id']
            metadata = mapping['nodes'].get('metadata') or {}
            
            agency_counts[agency_id]['words'] += metadata.get('word_count', 0)
            agency_counts[agency_id]['sections'] += metadata.get('section_count', 0)
        
        offset += batch_size
        
        # Progress tracking
        progress = min(100, (offset / total_mappings) * 100)
        elapsed = time.time() - start_time
        rate = offset / elapsed if elapsed > 0 else 0
        eta = (total_mappings - offset) / rate if rate > 0 else 0
        logger.info(f"Agency mapping progress: {progress:.1f}% ({offset}/{total_mappings}) - ETA: {eta:.1f}s")
    
    # Bulk update agencies
    updates = [
        {
            'id': agency_id,
            'num_words': counts['words'],
            'num_sections': counts['sections']
        }
        for agency_id, counts in agency_counts.items()
    ]
    
    if updates:
        client.table('agencies').upsert(updates).execute()
        logger.info(f"Updated counts for {len(updates)} agencies")

def main():
    """Main function to compute all counts"""
    start_time = time.time()
    total_nodes, total_agencies = get_total_counts()
    logger.info(f"Starting processing of {total_nodes} nodes and {total_agencies} agencies")
    
    # First, reset only aggregated counts
    reset_aggregated_counts()
    
    # Process nodes level by level
    logger.info("Processing nodes...")
    process_level()  # This will handle all levels due to sorting by ID length
    
    # Update agency counts
    logger.info("Updating agency counts...")
    update_agency_counts_bulk()
    
    elapsed_time = time.time() - start_time
    logger.info(f"All done! Total time: {elapsed_time:.1f} seconds")

if __name__ == "__main__":
    main() 