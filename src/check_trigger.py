#!/usr/bin/env python
"""
Script to check if the content_tsvector trigger exists and is working
"""
from src.database.connector import get_supabase_client

def check_trigger():
    """Check if the content_tsvector trigger exists and is working"""
    client = get_supabase_client()
    
    # First, check if the trigger exists
    result = client.rpc('get_trigger_info', {'table_name': 'content_chunks'}).execute()
    print("Trigger info:", result.data)
    
    # Test the trigger by inserting a test row
    test_chunk = {
        'id': 'test_chunk_1',
        'section_id': 'test_section_1',
        'chunk_number': 1,
        'content': 'This is a test content for checking the tsvector trigger.'
    }
    
    try:
        # Insert the test chunk
        insert_result = client.table('content_chunks').insert(test_chunk).execute()
        print("Insert result:", insert_result.data)
        
        # Check if the tsvector was computed
        check_result = client.table('content_chunks').select('content_tsvector').eq('id', 'test_chunk_1').execute()
        print("Content tsvector:", check_result.data)
        
        # Clean up
        client.table('content_chunks').delete().eq('id', 'test_chunk_1').execute()
        
    except Exception as e:
        print(f"Error testing trigger: {e}")

if __name__ == "__main__":
    check_trigger() 