import json
import psycopg2
import os

# Database connection parameters
DB_HOST = "db.ybootrcxmjgokgzbozgv.supabase.co"
DB_PORT = "5432"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "Fj@4P@j5aQ3iJtT"

def connect_db():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

def load_agencies():
    with open('src/localPush/json_tables/agencies.json', 'r') as f:
        agencies = json.load(f)
    
    conn = connect_db()
    cur = conn.cursor()
    
    # Clear existing data
    cur.execute("TRUNCATE agencies CASCADE;")
    
    # Insert agencies
    for agency in agencies:
        cur.execute("""
            INSERT INTO agencies (id, name, description, parent_id, depth, num_children, 
                                num_cfr, num_words, num_sections, num_corrections, cfr_references)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            agency['id'],
            agency['name'],
            agency.get('description'),
            agency.get('parent_id'),
            agency.get('depth', 0),
            agency.get('num_children', 0),
            agency.get('num_cfr', 0),
            agency.get('num_words', 0),
            agency.get('num_sections', 0),
            agency.get('num_corrections', 0),
            agency.get('cfr_references', [])
        ))
    
    conn.commit()
    print(f"Loaded {len(agencies)} agencies")
    
    cur.close()
    conn.close()

if __name__ == "__main__":
    load_agencies() 