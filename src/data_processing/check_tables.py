#!/usr/bin/env python
"""
Script to check database tables and their relationships
"""
import os
import logging
from typing import Dict, List, Any
from datetime import datetime

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import database connector
from src.database.connector import get_supabase_client

def check_table_exists(client, table_name: str) -> bool:
    """Check if a table exists in the database."""
    try:
        result = client.table(table_name).select("id").limit(1).execute()
        return True
    except Exception as e:
        logger.error(f"Table {table_name} does not exist: {e}")
        return False

def check_table_count(client, table_name: str) -> int:
    """Get the count of records in a table."""
    try:
        result = client.table(table_name).select("id", count="exact").execute()
        return result.count
    except Exception as e:
        logger.error(f"Error getting count for {table_name}: {e}")
        return 0

def check_foreign_key_relationships(client, table_name: str, foreign_keys: List[str]) -> Dict[str, Any]:
    """Check foreign key relationships in a table."""
    results = {}
    for fk in foreign_keys:
        try:
            # Get count of records with NULL foreign keys
            null_count = client.table(table_name).select("id", count="exact").is_(fk, "null").execute()
            results[f"{fk}_null_count"] = null_count.count
            
            # Get count of records with invalid foreign keys
            invalid_count = client.table(table_name).select("id", count="exact").not_.is_(fk, "null").execute()
            results[f"{fk}_invalid_count"] = invalid_count.count
        except Exception as e:
            logger.error(f"Error checking foreign key {fk} in {table_name}: {e}")
            results[f"{fk}_error"] = str(e)
    return results

def check_required_fields(client, table_name: str, required_fields: List[str]) -> Dict[str, Any]:
    """Check if required fields are populated."""
    results = {}
    for field in required_fields:
        try:
            # Get count of records with NULL values
            null_count = client.table(table_name).select("id", count="exact").is_(field, "null").execute()
            results[f"{field}_null_count"] = null_count.count
        except Exception as e:
            logger.error(f"Error checking required field {field} in {table_name}: {e}")
            results[f"{field}_error"] = str(e)
    return results

def check_table_data():
    """Check all tables and their relationships."""
    client = get_supabase_client()
    
    # Define tables and their relationships
    tables = {
        'nodes': {
            'foreign_keys': ['parent'],
            'required_fields': ['id', 'citation', 'node_type', 'level_type', 'number', 'node_name']
        },
        'content_chunks': {
            'foreign_keys': ['section_id'],
            'required_fields': ['id', 'section_id', 'chunk_number', 'content']
        },
        'agencies': {
            'foreign_keys': ['parent_id'],
            'required_fields': ['id', 'name']
        },
        'cfr_references': {
            'foreign_keys': ['agency_id', 'node_id'],
            'required_fields': ['id', 'agency_id', 'title']
        },
        'agency_node_mappings': {
            'foreign_keys': ['agency_id', 'node_id'],
            'required_fields': ['id', 'agency_id', 'node_id']
        },
        'corrections': {
            'foreign_keys': ['node_id'],
            'required_fields': ['id', 'node_id', 'title', 'corrective_action', 'error_corrected', 'error_occurred']
        }
    }
    
    results = {}
    
    # Check each table
    for table_name, config in tables.items():
        logger.info(f"\nChecking table: {table_name}")
        
        # Check if table exists
        if not check_table_exists(client, table_name):
            results[table_name] = {'error': 'Table does not exist'}
            continue
        
        # Get record count
        count = check_table_count(client, table_name)
        logger.info(f"Total records: {count}")
        
        # Check foreign key relationships
        fk_results = check_foreign_key_relationships(client, table_name, config['foreign_keys'])
        for fk, result in fk_results.items():
            logger.info(f"{fk}: {result}")
        
        # Check required fields
        field_results = check_required_fields(client, table_name, config['required_fields'])
        for field, result in field_results.items():
            logger.info(f"{field}: {result}")
        
        results[table_name] = {
            'count': count,
            'foreign_keys': fk_results,
            'required_fields': field_results
        }
    
    return results

if __name__ == "__main__":
    logger.info("Starting database table checks...")
    results = check_table_data()
    
    # Print summary
    logger.info("\nSummary:")
    for table_name, result in results.items():
        logger.info(f"\n{table_name}:")
        if 'error' in result:
            logger.error(f"Error: {result['error']}")
        else:
            logger.info(f"Total records: {result['count']}")
            logger.info("Foreign key issues:")
            for fk, count in result['foreign_keys'].items():
                if count > 0:
                    logger.warning(f"  {fk}: {count}")
            logger.info("Required field issues:")
            for field, count in result['required_fields'].items():
                if count > 0:
                    logger.warning(f"  {field}: {count}") 