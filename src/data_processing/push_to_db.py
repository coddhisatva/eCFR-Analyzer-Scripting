#!/usr/bin/env python
"""
Script to push nodes and content chunks to the database
"""
import os
import json
import logging
from typing import List, Dict, Any
from src.database.connector import insert_nodes, insert_content_chunks
from src.models.node import Node
from src.models.content_chunk import ContentChunk

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Directory for JSON tables
JSON_TABLES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "src", "localPush", "json_tables")

def push_title_to_db(title_num: str):
    """Push nodes and content chunks for a single title to the database"""
    title_dir = os.path.join(JSON_TABLES_DIR, f"title_{title_num}")
    
    # Push nodes
    nodes_file = os.path.join(title_dir, "nodes.json")
    if os.path.exists(nodes_file):
        with open(nodes_file, 'r', encoding='utf-8') as f:
            nodes_data = json.load(f)
            nodes = [Node(**node) for node in nodes_data]
            insert_nodes(nodes)
            logger.info(f"Pushed {len(nodes)} nodes for title {title_num}")
    
    # Push content chunks
    chunks_file = os.path.join(title_dir, "content_chunks.json")
    if os.path.exists(chunks_file):
        with open(chunks_file, 'r', encoding='utf-8') as f:
            chunks_data = json.load(f)
            chunks = [ContentChunk(**chunk) for chunk in chunks_data]
            insert_content_chunks(chunks)
            logger.info(f"Pushed {len(chunks)} content chunks for title {title_num}")

def main():
    """Push all titles to the database"""
    # Get all title directories
    title_dirs = [d for d in os.listdir(JSON_TABLES_DIR) if d.startswith("title_")]
    
    for title_dir in title_dirs:
        title_num = title_dir.split('_')[1]  # Extract title number
        logger.info(f"Processing title {title_num}...")
        push_title_to_db(title_num)

if __name__ == "__main__":
    main() 