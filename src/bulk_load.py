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

def bulk_insert_with_progress(conn, cur, table_name, data, columns, value_template, on_conflict=None):
    try:
        print(f"\nProcessing {table_name}...")
        cur.execute(f'TRUNCATE {table_name} CASCADE')
        conn.commit()  # Commit the truncate immediately
        
        total_batches = (len(data) + BATCH_SIZE - 1) // BATCH_SIZE
        successful_inserts = 0
        
        for i in tqdm(range(0, len(data), BATCH_SIZE), desc=f"Inserting {table_name}", total=total_batches):
            try:
                batch = data[i:i + BATCH_SIZE]
                values = [value_template(item) for item in batch]
                
                sql = f"""
                    INSERT INTO {table_name} ({', '.join(columns)})
                    VALUES %s
                    {on_conflict if on_conflict else ''}
                """
                
                execute_values(cur, sql, values, page_size=BATCH_SIZE)
                conn.commit()  # Commit each batch
                successful_inserts += len(batch)
                print(f"Memory usage: {get_memory_usage():.1f} MB")
            except Exception as batch_error:
                print(f"\nError in batch starting at index {i}: {batch_error}")
                print("Continuing with next batch...")
                conn.rollback()  # Rollback just this batch
                continue
        
        print(f"✓ {table_name} loaded - {successful_inserts}/{len(data)} records inserted successfully")
        return True
    except Exception as e:
        print(f"\n❌ Error loading {table_name}: {e}")
        conn.rollback()  # Rollback any uncommitted changes
        return False

def main():
    print("Connecting to database...")
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    
    tables_loaded = []
    tables_failed = []
    
    try:
        # 1. Load agencies
        agencies = load_json_file('agencies.json')
        if bulk_insert_with_progress(
            conn, cur, 'agencies',
            agencies,
            ['id', 'name', 'description', 'parent_id', 'depth', 'num_children', 
             'num_cfr', 'num_words', 'num_sections', 'num_corrections', 'cfr_references'],
            lambda a: (
                a['id'], a['name'], a.get('description'), a.get('parent_id'),
                a.get('depth', 0), a.get('num_children', 0), a.get('num_cfr', 0),
                a.get('num_words', 0), a.get('num_sections', 0),
                a.get('num_corrections', 0), a.get('cfr_references', [])
            )
        ):
            tables_loaded.append('agencies')
        else:
            tables_failed.append('agencies')
        
        # 2. Load nodes
        nodes = load_json_file('all_nodes.json')
        if bulk_insert_with_progress(
            conn, cur, 'nodes',
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
        ):
            tables_loaded.append('nodes')
        else:
            tables_failed.append('nodes')
        
        # 3. Load chunks
        chunks = load_json_file('all_chunks.json')
        if bulk_insert_with_progress(
            conn, cur, 'content_chunks',
            chunks,
            ['id', 'section_id', 'chunk_number', 'content'],
            lambda c: (
                c['id'], c['section_id'], c['chunk_number'], c['content']
            )
        ):
            tables_loaded.append('content_chunks')
        else:
            tables_failed.append('content_chunks')
        
        # 4. Load agency mappings with ON CONFLICT DO NOTHING
        mappings = load_json_file('agency_node_mappings.json')
        if bulk_insert_with_progress(
            conn, cur, 'agency_node_mappings',
            mappings,
            ['agency_id', 'node_id', 'metadata'],
            lambda m: (
                m['agency_id'], m['node_id'],
                json.dumps(m['metadata']) if m.get('metadata') else None
            ),
            on_conflict="ON CONFLICT (agency_id, node_id) DO NOTHING"
        ):
            tables_loaded.append('agency_node_mappings')
        else:
            tables_failed.append('agency_node_mappings')
        
        # 5. Load CFR references
        references = load_json_file('cfr_references.json')
        if bulk_insert_with_progress(
            conn, cur, 'cfr_references',
            references,
            ['agency_id', 'title', 'subheading', 'ordinal', 'node_id'],
            lambda r: (
                r['agency_id'], r['title'], r.get('subheading'),
                r.get('ordinal'), r.get('node_id')
            ),
            on_conflict="ON CONFLICT (agency_id, node_id) DO NOTHING"
        ):
            tables_loaded.append('cfr_references')
        else:
            tables_failed.append('cfr_references')

        # 6. Load corrections
        corrections = load_json_file('all_corrections.json')
        if bulk_insert_with_progress(
            conn, cur, 'corrections',
            corrections,
            ['node_id', 'agency_id', 'title', 'corrective_action', 'error_corrected',
             'error_occurred', 'correction_duration', 'fr_citation', 'position', 'year', 'metadata'],
            lambda c: (
                c['node_id'], c.get('agency_id'), c['title'],
                c.get('corrective_action'), c.get('error_corrected'),
                c.get('error_occurred'), c.get('correction_duration'),
                c.get('fr_citation'), c.get('position'), c.get('year'),
                json.dumps(c['metadata']) if c.get('metadata') else None
            )
        ):
            tables_loaded.append('corrections')
        else:
            tables_failed.append('corrections')
        
        print("\n=== LOAD SUMMARY ===")
        if tables_loaded:
            print("✓ Successfully loaded tables:")
            for table in tables_loaded:
                print(f"  - {table}")
        if tables_failed:
            print("\n❌ Failed to load tables:")
            for table in tables_failed:
                print(f"  - {table}")
        
    except Exception as e:
        print(f"\nUnexpected error: {e}")
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    main() 