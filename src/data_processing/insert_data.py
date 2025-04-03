#!/usr/bin/env python
"""
Script to insert data using existing connector functions
"""
import os
import json
import logging
from typing import List, Dict, Any
from src.database.connector import insert_nodes, insert_content_chunks, insert_agencies, insert_cfr_references, insert_agency_node_mappings, insert_corrections
from src.models.node import Node
from src.models.content_chunk import ContentChunk

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Directory for JSON tables
JSON_TABLES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "src", "localPush", "json_tables")

def insert_all_data():
    """Insert all data using existing connector functions"""
    # Insert nodes and content chunks for each title
    for title_dir in os.listdir(JSON_TABLES_DIR):
        if not title_dir.startswith('title_'):
            continue
            
        title_num = title_dir.split('_')[1]
        logger.info(f"Processing title {title_num}...")
        
        # Insert nodes
        nodes_file = os.path.join(JSON_TABLES_DIR, title_dir, "nodes.json")
        if os.path.exists(nodes_file):
            with open(nodes_file, 'r', encoding='utf-8') as f:
                nodes_data = json.load(f)
                nodes = [Node(**node) for node in nodes_data]
                insert_nodes(nodes)
                logger.info(f"Inserted {len(nodes)} nodes for title {title_num}")
        
        # Insert content chunks
        chunks_file = os.path.join(JSON_TABLES_DIR, title_dir, "content_chunks.json")
        if os.path.exists(chunks_file):
            with open(chunks_file, 'r', encoding='utf-8') as f:
                chunks_data = json.load(f)
                chunks = [ContentChunk(**chunk) for chunk in chunks_data]
                insert_content_chunks(chunks)
                logger.info(f"Inserted {len(chunks)} content chunks for title {title_num}")
        
        # Insert corrections for this title
        corrections_file = os.path.join(JSON_TABLES_DIR, title_dir, "corrections.json")
        if os.path.exists(corrections_file):
            with open(corrections_file, 'r', encoding='utf-8') as f:
                corrections_data = json.load(f)
                insert_corrections(corrections_data)
                logger.info(f"Inserted {len(corrections_data)} corrections for title {title_num}")
    
    # Insert global data
    logger.info("Inserting global data...")
    
    # Insert agencies
    agencies_file = os.path.join(JSON_TABLES_DIR, "agencies.json")
    if os.path.exists(agencies_file):
        with open(agencies_file, 'r', encoding='utf-8') as f:
            agencies_data = json.load(f)
            insert_agencies(agencies_data)
            logger.info(f"Inserted {len(agencies_data)} agencies")
    
    # Insert CFR references
    refs_file = os.path.join(JSON_TABLES_DIR, "cfr_references.json")
    if os.path.exists(refs_file):
        with open(refs_file, 'r', encoding='utf-8') as f:
            refs_data = json.load(f)
            insert_cfr_references(refs_data)
            logger.info(f"Inserted {len(refs_data)} CFR references")
    
    # Insert agency-node mappings
    mappings_file = os.path.join(JSON_TABLES_DIR, "agency_node_mappings.json")
    if os.path.exists(mappings_file):
        with open(mappings_file, 'r', encoding='utf-8') as f:
            mappings_data = json.load(f)
            insert_agency_node_mappings(mappings_data)
            logger.info(f"Inserted {len(mappings_data)} agency-node mappings")

if __name__ == "__main__":
    insert_all_data() 