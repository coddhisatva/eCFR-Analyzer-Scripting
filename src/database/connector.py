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
            'depth': node.depth,
            'metadata': node.metadata,
            'num_corrections': node.num_corrections
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
    batch_size = 100
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
    
    # Convert references to dictionaries for insertion
    reference_dicts = []
    for ref in references:
        ref_dict = {
            'agency_id': ref.agency_id,
            'title': ref.title,
            'subheading': ref.subheading,
            'is_primary': ref.is_primary,
            'ordinal': ref.ordinal,
            'node_id': ref.node_id
        }
        reference_dicts.append(ref_dict)
    
    # Insert references in batches
    batch_size = 100
    for i in range(0, len(reference_dicts), batch_size):
        batch = reference_dicts[i:i + batch_size]
        try:
            result = client.table('cfr_references').upsert(batch).execute()
            print(f"Inserted/updated batch of {len(batch)} CFR references")
        except Exception as e:
            print(f"Error inserting batch: {e}")
            print("First few references in problematic batch:")
            for ref in batch[:3]:
                print(f"Agency: {ref['agency_id']}, Title: {ref['title']}")
            raise

def insert_agency_node_mappings(mappings: List[AgencyNodeMapping]):
    """
    Insert agency-node mappings into the database
    
    Args:
        mappings: List of agency-node mapping entities to insert
        
    Returns:
        Result of the insert operation
    """
    client = get_supabase_client()
    
    # Convert mappings to dictionaries for insertion
    mapping_dicts = []
    for mapping in mappings:
        mapping_dict = {
            'agency_id': mapping.agency_id,
            'node_id': mapping.node_id,
            'is_primary': mapping.is_primary,
            'is_direct_reference': mapping.is_direct_reference,
            'relationship_type': mapping.relationship_type,
            'metadata': mapping.metadata
        }
        mapping_dicts.append(mapping_dict)
    
    # Insert mappings in batches
    batch_size = 100
    for i in range(0, len(mapping_dicts), batch_size):
        batch = mapping_dicts[i:i + batch_size]
        try:
            result = client.table('agency_node_mappings').upsert(batch).execute()
            print(f"Inserted/updated batch of {len(batch)} agency-node mappings")
        except Exception as e:
            print(f"Error inserting batch: {e}")
            print("First few mappings in problematic batch:")
            for mapping in batch[:3]:
                print(f"Agency: {mapping['agency_id']}, Node: {mapping['node_id']}")
            raise

def insert_corrections(corrections: List[Correction]):
    """
    Insert corrections into the database
    
    Args:
        corrections: List of correction entities to insert
        
    Returns:
        Result of the insert operation
    """
    client = get_supabase_client()
    
    # Convert corrections to dictionaries for insertion
    correction_dicts = []
    for correction in corrections:
        correction_dict = {
            'node_id': correction.node_id,
            'title': correction.title,
            'corrective_action': correction.corrective_action,
            'error_corrected': correction.error_corrected.isoformat(),
            'error_occurred': correction.error_occurred.isoformat(),
            'correction_duration': correction.correction_duration,
            'fr_citation': correction.fr_citation,
            'position': correction.position,
            'year': correction.year,
            'metadata': correction.metadata
        }
        correction_dicts.append(correction_dict)
    
    # Insert corrections in batches
    batch_size = 100
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
