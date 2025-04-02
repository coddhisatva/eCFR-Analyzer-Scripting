from src.database.connector import get_supabase_client

def get_parent_id(node_id: str) -> str:
    """Get the parent ID of a node"""
    parts = node_id.split('/')
    if len(parts) <= 1:
        return None
    return '/'.join(parts[:-1])

def get_children(parent_id: str):
    """Get all immediate children of a node"""
    client = get_supabase_client()
    
    # Use LIKE to match immediate children (one level down)
    result = client.table('nodes').select('id').ilike('id', f"{parent_id}/%").execute()
    return [node for node in result.data if get_parent_id(node['id']) == parent_id]

def is_section(node_id: str) -> bool:
    """Check if a node is a section by looking for 'section=' in its ID"""
    return 'section=' in node_id 