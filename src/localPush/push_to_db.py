#!/usr/bin/env python
"""
Simple script to push local nodes and chunks data to the database in batches
"""
import logging
import csv
import os
from typing import List, Dict, Any
from src.database.connector import get_supabase_client, insert_nodes, insert_content_chunks
from src.models.node import Node
from src.models.content_chunk import ContentChunk

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BATCH_SIZE = 1000

def load_csv_file(file_path: str) -> List[Dict[str, Any]]:
    """Load data from a CSV file"""
    try:
        data = []
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        return data
    except Exception as e:
        logger.error(f"Error loading {file_path}: {e}")
        return []

def convert_to_nodes(data: List[Dict[str, Any]]) -> List[Node]:
    """Convert CSV data to Node objects"""
    nodes = []
    for row in data:
        try:
            # Convert string values to appropriate types
            metadata = row.get('metadata', '{}')
            if isinstance(metadata, str):
                if metadata.strip() == '':
                    metadata = {}
                else:
                    try:
                        metadata = eval(metadata)  # Safely evaluate string representation of dict
                    except:
                        metadata = {}
            
            # Handle float values for numeric fields
            def safe_int_convert(value):
                if isinstance(value, str):
                    try:
                        return int(float(value))
                    except (ValueError, TypeError):
                        return 0
                return int(value)
            
            node = Node(
                id=row['id'],
                citation=row['citation'],
                link=row['link'],
                node_type=row['node_type'],
                level_type=row['level_type'],
                number=row['number'],
                node_name=row['node_name'],
                parent=row.get('parent'),
                top_level_title=row['top_level_title'],
                metadata=metadata,
                depth=safe_int_convert(row['depth']),
                display_order=safe_int_convert(row['display_order']),
                num_corrections=safe_int_convert(row['num_corrections']),
                num_sections=safe_int_convert(row['num_sections']),
                num_words=safe_int_convert(row['num_words'])
            )
            nodes.append(node)
        except Exception as e:
            logger.error(f"Error converting row to Node: {e}")
            logger.error(f"Row data: {row}")
    return nodes

def convert_to_chunks(data: List[Dict[str, Any]]) -> List[ContentChunk]:
    """Convert CSV data to ContentChunk objects"""
    chunks = []
    for row in data:
        try:
            # Handle potential float values for chunk_number
            chunk_number = int(float(row['chunk_number'])) if isinstance(row['chunk_number'], str) else int(row['chunk_number'])
            
            chunk = ContentChunk(
                id=row['id'],
                section_id=row['section_id'],
                chunk_number=chunk_number,
                content=row['content']
            )
            chunks.append(chunk)
        except Exception as e:
            logger.error(f"Error converting row to ContentChunk: {e}")
            logger.error(f"Row data: {row}")
    return chunks

def process_in_batches(data: List[Dict[str, Any]], batch_size: int, convert_func, insert_func):
    """Process data in batches using the provided convert and insert functions"""
    total = len(data)
    for i in range(0, total, batch_size):
        batch = data[i:i + batch_size]
        try:
            # Convert batch to proper objects
            converted_batch = convert_func(batch)
            # Insert converted objects
            insert_func(converted_batch)
            logger.info(f"Processed batch {i//batch_size + 1} of {(total + batch_size - 1)//batch_size}")
        except Exception as e:
            logger.error(f"Error processing batch {i//batch_size + 1}: {e}")

def main():
    """Main function to push local data to database"""
    # Get the backup directory path (most recent backup)
    backup_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "processed_backup")
    backup_dirs = sorted([d for d in os.listdir(backup_dir) if os.path.isdir(os.path.join(backup_dir, d))])
    if not backup_dirs:
        logger.error("No backup directories found")
        return
        
    latest_backup = backup_dirs[-1]
    backup_path = os.path.join(backup_dir, latest_backup)
    logger.info(f"Using backup from: {latest_backup}")
    
    # Load nodes
    nodes_file = os.path.join(backup_path, "nodes.csv")
    nodes_data = load_csv_file(nodes_file)
    if nodes_data:
        logger.info(f"Found {len(nodes_data)} nodes to process")
        process_in_batches(nodes_data, BATCH_SIZE, convert_to_nodes, insert_nodes)
    
    # Load chunks
    chunks_file = os.path.join(backup_path, "content_chunks.csv")
    chunks_data = load_csv_file(chunks_file)
    if chunks_data:
        logger.info(f"Found {len(chunks_data)} chunks to process")
        process_in_batches(chunks_data, BATCH_SIZE, convert_to_chunks, insert_content_chunks)

if __name__ == "__main__":
    main() 