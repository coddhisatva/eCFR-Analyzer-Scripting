#!/usr/bin/env python3
"""
Script to push nodes and content chunks to the database using SQL functions
"""
import os
import json
import logging
from typing import List, Dict, Any
from src.database.connector import get_supabase_client

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Directory for JSON tables
JSON_TABLES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "src", "localPush", "json_tables")

def push_nodes_to_db():
    """Push all nodes from JSON files to database"""
    client = get_supabase_client()
    
    # Get all title directories
    title_dirs = [d for d in os.listdir(JSON_TABLES_DIR) if d.startswith("title_")]
    
    for title_dir in title_dirs:
        nodes_file = os.path.join(JSON_TABLES_DIR, title_dir, "nodes.json")
        if not os.path.exists(nodes_file):
            logger.warning(f"No nodes.json found in {title_dir}")
            continue
            
        try:
            with open(nodes_file, 'r', encoding='utf-8') as f:
                nodes = json.load(f)
            
            if not nodes:
                logger.warning(f"No nodes found in {nodes_file}")
                continue
                
            # Convert nodes to JSONB for SQL function
            nodes_json = json.dumps(nodes)
            
            # Call the bulk insert function
            result = client.rpc('bulk_insert_nodes', {'nodes_json': nodes_json}).execute()
            
            if result.error:
                logger.error(f"Error inserting nodes for {title_dir}: {result.error}")
            else:
                logger.info(f"Successfully inserted {len(nodes)} nodes for {title_dir}")
                
        except Exception as e:
            logger.error(f"Error processing {nodes_file}: {e}")
            continue

def push_content_chunks_to_db():
    """Push all content chunks from JSON files to database"""
    client = get_supabase_client()
    
    # Get all title directories
    title_dirs = [d for d in os.listdir(JSON_TABLES_DIR) if d.startswith("title_")]
    
    for title_dir in title_dirs:
        chunks_file = os.path.join(JSON_TABLES_DIR, title_dir, "content_chunks.json")
        if not os.path.exists(chunks_file):
            logger.warning(f"No content_chunks.json found in {title_dir}")
            continue
            
        try:
            with open(chunks_file, 'r', encoding='utf-8') as f:
                chunks = json.load(f)
            
            if not chunks:
                logger.warning(f"No chunks found in {chunks_file}")
                continue
                
            # Convert chunks to JSONB for SQL function
            chunks_json = json.dumps(chunks)
            
            # Call the bulk insert function
            result = client.rpc('bulk_insert_content_chunks', {'chunks_json': chunks_json}).execute()
            
            if result.error:
                logger.error(f"Error inserting chunks for {title_dir}: {result.error}")
            else:
                logger.info(f"Successfully inserted {len(chunks)} chunks for {title_dir}")
                
        except Exception as e:
            logger.error(f"Error processing {chunks_file}: {e}")
            continue

def main():
    """Main function to push data to database"""
    logger.info("Starting database push...")
    
    # Push nodes first (since content_chunks references nodes)
    logger.info("Pushing nodes to database...")
    push_nodes_to_db()
    
    # Then push content chunks
    logger.info("Pushing content chunks to database...")
    push_content_chunks_to_db()
    
    logger.info("Finished database push")

if __name__ == "__main__":
    main() 