#!/usr/bin/env python
"""
Local version of CFR XML processing that stores data in JSON format
"""
import os
import json
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
from datetime import datetime

# Set up basic logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Directory structure for storing JSON data
BASE_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "local")
NODES_DIR = os.path.join(BASE_DATA_DIR, "nodes")
CHUNKS_DIR = os.path.join(BASE_DATA_DIR, "chunks")

@dataclass
class Node:
    """Represents a node in the CFR hierarchy"""
    id: str
    citation: str
    link: str
    node_type: str  # "structure" or "content"
    level_type: str
    number: str
    node_name: str
    parent: Optional[str] = None
    top_level_title: Optional[int] = None  # Changed to int to match schema
    depth: int = 0
    display_order: int = 0
    reserved: Optional[str] = None  # Added to match schema
    metadata: Optional[Dict[str, Any]] = None
    num_corrections: int = 0
    num_sections: int = 0
    num_words: int = 0

@dataclass
class ContentChunk:
    """Represents a chunk of content from a section"""
    id: str
    section_id: str
    chunk_number: int
    content: str
    # Note: content_tsvector is not stored in JSON as it's computed in DB

def ensure_directory_exists(directory: str) -> None:
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_nodes(nodes: List[Node], title_num: str) -> None:
    """
    Save nodes to JSON files organized by title.
    
    Args:
        nodes: List of Node objects to save
        title_num: The title number these nodes belong to
    """
    ensure_directory_exists(NODES_DIR)
    
    # Create a directory for this title
    title_dir = os.path.join(NODES_DIR, f"title_{title_num}")
    ensure_directory_exists(title_dir)
    
    # Save each node to a separate file
    for node in nodes:
        node_file = os.path.join(title_dir, f"node_{node.id}.json")
        with open(node_file, 'w', encoding='utf-8') as f:
            json.dump(asdict(node), f, indent=2, ensure_ascii=False)
    
    # Save a summary file with all node IDs for this title
    summary_file = os.path.join(title_dir, "summary.json")
    summary = {
        "title": title_num,
        "node_ids": [node.id for node in nodes],
        "last_updated": datetime.now().isoformat()
    }
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

def save_chunks(chunks: List[ContentChunk], title_num: str) -> None:
    """
    Save content chunks to JSON files organized by title.
    
    Args:
        chunks: List of ContentChunk objects to save
        title_num: The title number these chunks belong to
    """
    ensure_directory_exists(CHUNKS_DIR)
    
    # Create a directory for this title
    title_dir = os.path.join(CHUNKS_DIR, f"title_{title_num}")
    ensure_directory_exists(title_dir)
    
    # Save each chunk to a separate file
    for chunk in chunks:
        chunk_file = os.path.join(title_dir, f"chunk_{chunk.id}.json")
        with open(chunk_file, 'w', encoding='utf-8') as f:
            json.dump(asdict(chunk), f, indent=2, ensure_ascii=False)
    
    # Save a summary file with all chunk IDs for this title
    summary_file = os.path.join(title_dir, "summary.json")
    summary = {
        "title": title_num,
        "chunk_ids": [chunk.id for chunk in chunks],
        "last_updated": datetime.now().isoformat()
    }
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

def load_nodes(title_num: str) -> List[Node]:
    """
    Load all nodes for a specific title.
    
    Args:
        title_num: The title number to load nodes for
        
    Returns:
        List of Node objects
    """
    title_dir = os.path.join(NODES_DIR, f"title_{title_num}")
    if not os.path.exists(title_dir):
        return []
    
    # Load the summary file to get all node IDs
    summary_file = os.path.join(title_dir, "summary.json")
    if not os.path.exists(summary_file):
        return []
    
    with open(summary_file, 'r', encoding='utf-8') as f:
        summary = json.load(f)
    
    # Load each node file
    nodes = []
    for node_id in summary["node_ids"]:
        node_file = os.path.join(title_dir, f"node_{node_id}.json")
        if os.path.exists(node_file):
            with open(node_file, 'r', encoding='utf-8') as f:
                node_data = json.load(f)
                nodes.append(Node(**node_data))
    
    return nodes

def load_chunks(title_num: str) -> List[ContentChunk]:
    """
    Load all chunks for a specific title.
    
    Args:
        title_num: The title number to load chunks for
        
    Returns:
        List of ContentChunk objects
    """
    title_dir = os.path.join(CHUNKS_DIR, f"title_{title_num}")
    if not os.path.exists(title_dir):
        return []
    
    # Load the summary file to get all chunk IDs
    summary_file = os.path.join(title_dir, "summary.json")
    if not os.path.exists(summary_file):
        return []
    
    with open(summary_file, 'r', encoding='utf-8') as f:
        summary = json.load(f)
    
    # Load each chunk file
    chunks = []
    for chunk_id in summary["chunk_ids"]:
        chunk_file = os.path.join(title_dir, f"chunk_{chunk_id}.json")
        if os.path.exists(chunk_file):
            with open(chunk_file, 'r', encoding='utf-8') as f:
                chunk_data = json.load(f)
                chunks.append(ContentChunk(**chunk_data))
    
    return chunks
