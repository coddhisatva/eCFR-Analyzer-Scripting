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
from src.models.agency import Agency
from src.models.cfr_reference import CFRReference
from src.models.agency_node_mapping import AgencyNodeMapping
from src.models.correction import Correction

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
    
    # Create client with increased timeout
    client = create_client(url, key)
    # Set timeout on the underlying HTTP client
    client.postgrest.session.timeout = 300  # 5 minutes
    return client

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
            'depth': node.depth,
            'metadata': node.metadata,
            'num_corrections': node.num_corrections,
            'display_order': node.display_order,
            'num_sections': node.num_sections,
            'num_words': node.num_words
        }
        unique_nodes.append(node_dict)
    
    # Insert nodes in batches to avoid request size limits
    batch_size = 1000
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
            'content': chunk.content
            # Don't include content_tsvector - it will be computed by the database
        }
        unique_chunks.append(chunk_dict)
    
    # Insert chunks in batches to avoid request size limits
    batch_size = 1000
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

def insert_agencies(agencies: List[Agency]):
    """
    Insert agencies into the database
    
    Args:
        agencies: List of agency entities to insert
        
    Returns:
        Result of the insert operation
    """
    client = get_supabase_client()
    
    # Track seen IDs to detect duplicates
    seen_ids = set()
    unique_agencies = []
    
    # Convert agencies to dictionaries for insertion
    for agency in agencies:
        if agency.id in seen_ids:
            print(f"WARNING: Skipping duplicate agency ID: {agency.id}")
            continue
        seen_ids.add(agency.id)
        
        agency_dict = {
            'id': agency.id,
            'name': agency.name,
            'short_name': agency.short_name,
            'display_name': agency.display_name,
            'sortable_name': agency.sortable_name,
            'parent_id': agency.parent_id,
            'depth': agency.depth,
            'agency_type': agency.agency_type,
            'metadata': agency.metadata,
            'num_children': agency.num_children,
            'num_words': agency.num_words,
            'num_sections': agency.num_sections,
            'num_corrections': agency.num_corrections
        }
        unique_agencies.append(agency_dict)
    
    # Insert agencies in batches
    batch_size = 1000
    for i in range(0, len(unique_agencies), batch_size):
        batch = unique_agencies[i:i + batch_size]
        try:
            result = client.table('agencies').upsert(batch).execute()
            print(f"Inserted/updated batch of {len(batch)} agencies")
        except Exception as e:
            print(f"Error inserting batch: {e}")
            print("First few agencies in problematic batch:")
            for agency in batch[:3]:
                print(f"ID: {agency['id']}, Name: {agency['name']}")
            raise

def insert_cfr_references(references: List[CFRReference]):
    """
    Insert CFR references into the database
    
    Args:
        references: List of CFR reference entities to insert
        
    Returns:
        Result of the insert operation
    """
    client = get_supabase_client()
    
    # Track seen combinations to avoid duplicates
    seen_refs = set()
    unique_refs = []
    
    # Convert references to dictionaries for insertion
    for ref in references:
        # Create a unique key for this reference
        ref_key = (ref.agency_id, ref.node_id)
        
        # Skip if we've seen this combination before
        if ref_key in seen_refs:
            print(f"WARNING: Skipping duplicate CFR reference: agency={ref.agency_id}, node={ref.node_id}")
            continue
        
        seen_refs.add(ref_key)
        ref_dict = {
            'id': ref.id,
            'agency_id': ref.agency_id,
            'title': ref.title,
            'subheading': ref.subheading,
            'ordinal': ref.ordinal,
            'node_id': ref.node_id
        }
        unique_refs.append(ref_dict)
    
    # Insert references in batches
    batch_size = 1000
    for i in range(0, len(unique_refs), batch_size):
        batch = unique_refs[i:i + batch_size]
        try:
            result = client.table('cfr_references').upsert(batch).execute()
            print(f"Inserted/updated batch of {len(batch)} CFR references")
        except Exception as e:
            print(f"Error inserting batch: {e}")
            print("First few references in problematic batch:")
            for ref in batch[:3]:
                print(f"Agency: {ref['agency_id']}, Title: {ref['title']}")
            raise

def insert_agency_node_mappings(mappings: List[AgencyNodeMapping]) -> None:
    """Insert agency-node mappings in batches"""
    client = get_supabase_client()
    
    # Convert mappings to dict format for insertion
    mapping_data = [
        {
            'id': mapping.id,
            'agency_id': mapping.agency_id,
            'node_id': mapping.node_id,
            'metadata': mapping.metadata
        }
        for mapping in mappings
    ]
    
    # Process in batches of 1000
    batch_size = 1000
    for i in range(0, len(mapping_data), batch_size):
        batch = mapping_data[i:i + batch_size]
        try:
            result = client.table('agency_node_mappings').upsert(batch).execute()
            print(f"Inserted/updated batch of {len(batch)} agency-node mappings")
        except Exception as e:
            print(f"Error inserting batch: {e}")
            print("First few mappings in problematic batch:")
            for mapping in batch[:3]:
                print(f"Agency: {mapping['agency_id']}, Node: {mapping['node_id']}")
            raise

def node_exists(node_id: str) -> bool:
    """
    Check if a node exists in the database
    
    Args:
        node_id: The ID of the node to check
        
    Returns:
        True if the node exists, False otherwise
    """
    client = get_supabase_client()
    try:
        result = client.table('nodes').select('id').eq('id', node_id).execute()
        return len(result.data) > 0
    except Exception as e:
        print(f"Error checking if node exists: {e}")
        return False

def insert_corrections(corrections: List[Correction]):
    """
    Insert corrections into the database
    
    Args:
        corrections: List of correction entities to insert
        
    Returns:
        Result of the insert operation
    """
    client = get_supabase_client()
    
    # Convert corrections to dictionaries for insertion, skipping missing nodes
    correction_dicts = []
    skipped_count = 0
    
    for correction in corrections:
        # Check if the node exists
        if not node_exists(correction.node_id):
            print(f"Skipping correction for missing node: {correction.node_id}")
            skipped_count += 1
            continue
            
        correction_dict = {
            'node_id': correction.node_id,
            'title': correction.title,
            'corrective_action': correction.corrective_action,
            'error_corrected': correction.error_corrected.isoformat() if correction.error_corrected else None,
            'error_occurred': correction.error_occurred.isoformat() if correction.error_occurred else None,
            'correction_duration': correction.correction_duration,
            'fr_citation': correction.fr_citation,
            'position': correction.position,
            'year': correction.year,
            'metadata': correction.metadata
        }
        correction_dicts.append(correction_dict)
    
    if skipped_count > 0:
        print(f"Skipped {skipped_count} corrections due to missing nodes")
    
    if not correction_dicts:
        print("No valid corrections to insert")
        return
    
    # Insert corrections in batches
    batch_size = 1000
    for i in range(0, len(correction_dicts), batch_size):
        batch = correction_dicts[i:i + batch_size]
        try:
            result = client.table('corrections').upsert(batch).execute()
            print(f"Inserted/updated batch of {len(batch)} corrections")
        except Exception as e:
            print(f"Error inserting batch: {e}")
            print("First few corrections in problematic batch:")
            for correction in batch[:3]:
                print(f"Node: {correction['node_id']}, Title: {correction['title']}")
            raise
