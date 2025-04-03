import json
import psycopg2
from psycopg2.extras import execute_values
import psutil
import sys
from tqdm import tqdm

# Database connection parameters
DB_PARAMS = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'Fj@4P@j5aQ3iJtT',
    'host': 'db.ybootrcxmjgokgzbozgv.supabase.co',
    'port': '5432'
}

BATCH_SIZE = 1000
BASE_PATH = 'src/localPush/json_tables/to_load'

def get_memory_usage():
    process = psutil.Process()
    return process.memory_info().rss / 1024 / 1024  # Convert to MB

def load_json_file(filename):
    full_path = f"{BASE_PATH}/{filename}"
    print(f"\nLoading {full_path}...")
    print(f"Memory before loading: {get_memory_usage():.1f} MB")
    with open(full_path, 'r') as f:
        data = json.load(f)
    print(f"Memory after loading: {get_memory_usage():.1f} MB")
    print(f"File contains {len(data)} records")
    return data

def bulk_insert_with_progress(cur, table_name, data, columns, value_template):
    print(f"\nProcessing {table_name}...")
    cur.execute(f'TRUNCATE {table_name} CASCADE')
    
    total_batches = (len(data) + BATCH_SIZE - 1) // BATCH_SIZE
    
    for i in tqdm(range(0, len(data), BATCH_SIZE), desc=f"Inserting {table_name}", total=total_batches):
        batch = data[i:i + BATCH_SIZE]
        values = [value_template(item) for item in batch]
        
        execute_values(cur,
            f"""
            INSERT INTO {table_name} ({', '.join(columns)})
            VALUES %s
            """,
            values,
            page_size=BATCH_SIZE
        )
        print(f"Memory usage: {get_memory_usage():.1f} MB")

def main():
    print("Connecting to database...")
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    
    try:
        # 1. Load agencies
        agencies = load_json_file('agencies.json')
        bulk_insert_with_progress(
            cur, 'agencies',
            agencies,
            ['id', 'name', 'description', 'parent_id', 'depth', 'num_children', 
             'num_cfr', 'num_words', 'num_sections', 'num_corrections', 'cfr_references'],
            lambda a: (
                a['id'], a['name'], a.get('description'), a.get('parent_id'),
                a.get('depth', 0), a.get('num_children', 0), a.get('num_cfr', 0),
                a.get('num_words', 0), a.get('num_sections', 0),
                a.get('num_corrections', 0), a.get('cfr_references', [])
            )
        )
        
        # 2. Load nodes
        nodes = load_json_file('all_nodes.json')
        bulk_insert_with_progress(
            cur, 'nodes',
            nodes,
            ['id', 'citation', 'link', 'node_type', 'level_type', 'number',
             'node_name', 'parent', 'top_level_title', 'depth', 'display_order',
             'reserved', 'metadata', 'num_corrections', 'num_sections', 'num_words'],
            lambda n: (
                n['id'], n['citation'], n['link'], n['node_type'],
                n['level_type'], n['number'], n['node_name'], n['parent'],
                n['top_level_title'], n['depth'], n['display_order'],
                n['reserved'], json.dumps(n['metadata']) if n['metadata'] else None,
                n.get('num_corrections', 0), n.get('num_sections', 0),
                n.get('num_words', 0)
            )
        )
        
        # 3. Load chunks
        chunks = load_json_file('all_chunks.json')
        bulk_insert_with_progress(
            cur, 'content_chunks',
            chunks,
            ['id', 'section_id', 'chunk_number', 'content'],
            lambda c: (
                c['id'], c['section_id'], c['chunk_number'], c['content']
            )
        )
        
        # 4. Load agency mappings
        mappings = load_json_file('agency_node_mappings.json')
        bulk_insert_with_progress(
            cur, 'agency_node_mappings',
            mappings,
            ['agency_id', 'node_id', 'metadata'],
            lambda m: (
                m['agency_id'], m['node_id'],
                json.dumps(m['metadata']) if m.get('metadata') else None
            )
        )
        
        # 5. Load CFR references
        references = load_json_file('cfr_references.json')
        bulk_insert_with_progress(
            cur, 'cfr_references',
            references,
            ['agency_id', 'title', 'subheading', 'ordinal', 'node_id'],
            lambda r: (
                r['agency_id'], r['title'], r.get('subheading'),
                r.get('ordinal'), r.get('node_id')
            )
        )
        
        # Commit all changes
        print("\nCommitting changes...")
        conn.commit()
        print("✓ All data loaded successfully!")
        
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
        raise
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    main() 