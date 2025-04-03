import json
import psycopg2
from psycopg2.extras import execute_values
import psutil
import sys
from tqdm import tqdm
import time

# Database connection parameters
DB_PARAMS = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'Fj@4P@j5aQ3iJtT',
    'host': 'db.ybootrcxmjgokgzbozgv.supabase.co',
    'port': '5432'
}

BATCH_SIZE = 1000
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds
BASE_PATH = 'src/localPush/json_tables/to_load'

def get_memory_usage():
    process = psutil.Process()
    return process.memory_info().rss / 1024 / 1024  # Convert to MB

def load_json_file(filename):
    print(f"\nLoading {BASE_PATH}/{filename}...")
    with open(f"{BASE_PATH}/{filename}", 'r') as f:
        data = json.load(f)
    return data

def bulk_insert_with_progress(conn, cur, table_name, data, columns, value_template, on_conflict=None, start_batch=0):
    try:
        print(f"\nProcessing {table_name}...")
        if start_batch == 0:
            cur.execute(f'TRUNCATE {table_name} CASCADE')
            conn.commit()  # Commit the truncate immediately
        
        total_batches = (len(data) + BATCH_SIZE - 1) // BATCH_SIZE
        successful_inserts = 0
        
        for i in tqdm(range(start_batch * BATCH_SIZE, len(data), BATCH_SIZE), 
                     desc=f"Inserting {table_name}", 
                     total=total_batches - start_batch,
                     initial=start_batch):
            batch = data[i:i + BATCH_SIZE]
            values = [value_template(item) for item in batch]
            
            sql = f"""
                INSERT INTO {table_name} ({', '.join(columns)})
                VALUES %s
                {on_conflict if on_conflict else ''}
            """
            
            retries = 0
            while retries < MAX_RETRIES:
                try:
                    execute_values(cur, sql, values, page_size=BATCH_SIZE)
                    conn.commit()  # Commit each batch
                    successful_inserts += len(batch)
                    print(f"Memory usage: {get_memory_usage():.1f} MB")
                    break
                except (psycopg2.OperationalError, psycopg2.InterfaceError) as e:
                    retries += 1
                    if retries == MAX_RETRIES:
                        print(f"\nError in batch starting at index {i} after {MAX_RETRIES} retries: {e}")
                        print("Continuing with next batch...")
                        conn.rollback()  # Rollback just this batch
                        # Re-establish connection
                        conn = psycopg2.connect(**DB_PARAMS)
                        cur = conn.cursor()
                    else:
                        print(f"\nRetry {retries}/{MAX_RETRIES} for batch starting at index {i}: {e}")
                        time.sleep(RETRY_DELAY)
                        # Re-establish connection
                        conn = psycopg2.connect(**DB_PARAMS)
                        cur = conn.cursor()
        
        print(f"✓ {table_name} loaded - {successful_inserts}/{len(data)} records inserted successfully")
        return True
    except Exception as e:
        print(f"\n❌ Error loading {table_name}: {e}")
        conn.rollback()  # Rollback any uncommitted changes
        return False

def main(resume_table=None, resume_batch=0):
    print("Connecting to database...")
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    
    tables_loaded = []
    tables_failed = []
    
    # Define the loading sequence
    loading_sequence = [
        ('nodes', 'all_nodes.json', ['id', 'citation', 'link', 'node_type', 'level_type', 'number',
             'node_name', 'parent', 'top_level_title', 'depth', 'display_order',
             'reserved', 'metadata', 'num_corrections', 'num_sections', 'num_words'],
         lambda n: (
             n['id'], n['citation'], n['link'], n['node_type'],
             n['level_type'], n['number'], n['node_name'], n['parent'],
             n['top_level_title'], n['depth'], n['display_order'],
             n['reserved'], json.dumps(n['metadata']) if n['metadata'] else None,
             n.get('num_corrections', 0), n.get('num_sections', 0),
             n.get('num_words', 0)
         ), None),
        
        ('content_chunks', 'all_chunks.json', ['id', 'section_id', 'chunk_number', 'content'],
         lambda c: (
             c['id'], c['section_id'], c['chunk_number'], c['content']
         ), None),
        
        ('agencies', 'agencies.json', ['id', 'name', 'description', 'parent_id', 'depth', 'num_children', 
             'num_cfr', 'num_words', 'num_sections', 'num_corrections', 'cfr_references'],
         lambda a: (
             a['id'], a['name'], a.get('description'), a.get('parent_id'),
             a.get('depth', 0), a.get('num_children', 0), a.get('num_cfr', 0),
             a.get('num_words', 0), a.get('num_sections', 0),
             a.get('num_corrections', 0), a.get('cfr_references', [])
         ), None),
        
        ('agency_node_mappings', 'agency_node_mappings.json', ['agency_id', 'node_id', 'metadata'],
         lambda m: (
             m['agency_id'], m['node_id'],
             json.dumps(m['metadata']) if m.get('metadata') else None
         ), "ON CONFLICT (agency_id, node_id) DO NOTHING"),
        
        ('cfr_references', 'cfr_references.json', ['agency_id', 'title', 'subheading', 'ordinal', 'node_id'],
         lambda r: (
             r['agency_id'], r['title'], r.get('subheading'),
             r.get('ordinal'), r.get('node_id')
         ), "ON CONFLICT (agency_id, node_id) DO NOTHING"),
        
        ('corrections', 'all_corrections.json', ['node_id', 'agency_id', 'title', 'corrective_action', 'error_corrected',
             'error_occurred', 'correction_duration', 'fr_citation', 'position', 'year', 'metadata'],
         lambda c: (
             c['node_id'], c.get('agency_id'), c['title'],
             c.get('corrective_action'), c.get('error_corrected'),
             c.get('error_occurred'), c.get('correction_duration'),
             c.get('fr_citation'), c.get('position'), c.get('year'),
             json.dumps(c['metadata']) if c.get('metadata') else None
         ), None)
    ]
    
    try:
        # Find the starting point in the sequence
        start_index = 0
        if resume_table:
            for i, (table_name, _, _, _, _) in enumerate(loading_sequence):
                if table_name == resume_table:
                    start_index = i
                    break
        
        # Process each table in sequence
        for i, (table_name, filename, columns, value_template, on_conflict) in enumerate(loading_sequence[start_index:], start=start_index):
            if i == start_index and resume_batch > 0:
                # For the first table, use the resume_batch
                start_batch = resume_batch
            else:
                start_batch = 0
                
            data = load_json_file(filename)
            if bulk_insert_with_progress(
                conn, cur, table_name,
                data, columns, value_template,
                on_conflict=on_conflict,
                start_batch=start_batch
            ):
                tables_loaded.append(table_name)
            else:
                tables_failed.append(table_name)
        
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
    # Check for resume parameters
    resume_table = None
    resume_batch = 0
    if len(sys.argv) > 1:
        resume_table = sys.argv[1]
        if len(sys.argv) > 2:
            resume_batch = int(sys.argv[2])
    
    main(resume_table, resume_batch) 