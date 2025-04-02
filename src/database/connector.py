#!/usr/bin/env python
"""
Database connector for Supabase
"""
import os
from dotenv import load_dotenv
from supabase import create_client, Client
from typing import List
from src.models.node import Node
from src.models.content_chunk import ContentChunk

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
    
    # Track seen IDs to detect duplicates
    seen_ids = set()
    unique_nodes = []
    
    # Convert nodes to dictionaries for insertion, filtering out duplicates
    for node in nodes:
        if node.id in seen_ids:
            print(f"WARNING: Skipping duplicate node ID: {node.id}")
            print(f"Node details: type={node.node_type}, level={node.level_type}, number={node.number}")
            continue
        seen_ids.add(node.id)
        
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
            'depth': node.depth,  # <-- Added depth here
            'metadata': node.metadata
        }
        unique_nodes.append(node_dict)
    
    # Insert nodes in batches to avoid request size limits
    batch_size = 100
    for i in range(0, len(unique_nodes), batch_size):
        batch = unique_nodes[i:i + batch_size]
        try:
            # Use upsert to handle duplicates
            result = client.table('nodes').upsert(batch).execute()
            print(f"Inserted/updated batch of {len(batch)} nodes")
        except Exception as e:
            print(f"Error inserting batch: {e}")
            # Print the first few nodes in the problematic batch
            print("First few nodes in problematic batch:")
            for node in batch[:3]:
                print(f"ID: {node['id']}, Type: {node['node_type']}, Level: {node['level_type']}")
            raise

def insert_content_chunks(chunks: List[ContentChunk]):
    """
    Insert content chunks into the database
    
    Args:
        chunks: List of content chunk entities to insert
        
    Returns:
        Result of the insert operation
    """
    client = get_supabase_client()
    
    # Track seen IDs to detect duplicates
    seen_ids = set()
    unique_chunks = []
    
    # Convert chunks to dictionaries for insertion, filtering out duplicates
    for chunk in chunks:
        if chunk.id in seen_ids:
            print(f"WARNING: Skipping duplicate chunk ID: {chunk.id}")
            continue
        seen_ids.add(chunk.id)
        
        chunk_dict = {
            'id': chunk.id,
            'section_id': chunk.section_id,
            'chunk_number': chunk.chunk_number,
            'content': chunk.content,
            'content_tsvector': chunk.content_tsvector
        }
        unique_chunks.append(chunk_dict)
    
    # Insert chunks in batches to avoid request size limits
    batch_size = 100
    for i in range(0, len(unique_chunks), batch_size):
        batch = unique_chunks[i:i + batch_size]
        try:
            # Use upsert to handle duplicates
            result = client.table('content_chunks').upsert(batch).execute()
            print(f"Inserted/updated batch of {len(batch)} chunks")
        except Exception as e:
            print(f"Error inserting batch: {e}")
            # Print the first few chunks in the problematic batch
            print("First few chunks in problematic batch:")
            for chunk in batch[:3]:
                print(f"ID: {chunk['id']}, Section: {chunk['section_id']}, Number: {chunk['chunk_number']}")
            raise
