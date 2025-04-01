#!/usr/bin/env python
"""
Database connector for Supabase
"""
import os
from dotenv import load_dotenv
from supabase import create_client, Client
from typing import List
from src.models.node import Node

# Load environment variables
load_dotenv()

def get_supabase_client() -> Client:
    """
    Get a Supabase client
    
    Returns:
        Supabase client
    """
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    
    if not url or not key:
        raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set in .env file")
    
    return create_client(url, key)

def insert_nodes(nodes: List[Node]):
    """
    Insert nodes into the database
    
    Args:
        nodes: List of node entities to insert
        
    Returns:
        Result of the insert operation
    """
    client = get_supabase_client()
    
    # Convert nodes to dictionaries for insertion
    node_dicts = []
    for node in nodes:
        node_dict = {
            'id': node.id,
            'citation': node.citation,
            'link': node.link,
            'node_type': node.node_type,
            'level_type': node.level_type,
            'number': node.number,
            'node_name': node.node_name,
            'parent': node.parent,
            'top_level_title': node.top_level_title,
            'reserved': node.reserved,
            'content': node.content,
            'metadata': node.metadata
        }
        node_dicts.append(node_dict)
    
    # Insert nodes in batches to avoid request size limits
    batch_size = 100
    for i in range(0, len(node_dicts), batch_size):
        batch = node_dicts[i:i + batch_size]
        try:
            # Use upsert to handle duplicates
            result = client.table('nodes').upsert(batch).execute()
            print(f"Inserted/updated batch of {len(batch)} nodes")
        except Exception as e:
            print(f"Error inserting batch: {e}")
            raise