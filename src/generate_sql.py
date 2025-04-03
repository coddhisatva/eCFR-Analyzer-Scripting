import json
import os

def generate_agencies_sql():
    with open('src/localPush/json_tables/agencies.json', 'r') as f:
        agencies = json.load(f)
    
    # Only use columns that exist in our schema
    columns = ['id', 'name', 'description', 'parent_id', 'depth', 
              'num_children', 'num_cfr', 'num_words', 'num_sections', 
              'num_corrections', 'cfr_references']
    
    sql = ["TRUNCATE agencies CASCADE;\n\nINSERT INTO agencies ("]
    sql.append(", ".join(columns))
    sql.append(") VALUES\n")
    
    values = []
    for agency in agencies:
        value_list = []
        for col in columns:
            val = agency.get(col)
            if val is None:
                value_list.append('null')
            elif isinstance(val, str):
                # Escape single quotes and wrap in quotes
                value_list.append("'" + val.replace("'", "''") + "'")
            elif isinstance(val, (list, dict)):
                # Convert lists/dicts to JSON string
                if col == 'cfr_references':
                    # Handle array type
                    if not val:
                        value_list.append("'{}'::text[]")
                    else:
                        value_list.append("ARRAY['" + "','".join(str(x) for x in val) + "']::text[]")
                else:
                    value_list.append("'" + json.dumps(val) + "'::jsonb")
            else:
                value_list.append(str(val))
        values.append("(" + ", ".join(value_list) + ")")
    
    sql.append(",\n".join(values))
    sql.append(";\n")
    
    with open('src/load_agencies.sql', 'w') as f:
        f.write(''.join(sql))

def generate_nodes_sql():
    # Only use columns that exist in our schema
    columns = ['id', 'citation', 'link', 'node_type', 'level_type',
              'number', 'node_name', 'parent', 'top_level_title',
              'depth', 'display_order', 'reserved', 'metadata',
              'num_corrections', 'num_sections', 'num_words']
    
    sql = ["TRUNCATE nodes CASCADE;\n\n"]
    
    # Process each title directory
    base_path = 'src/localPush/json_tables'
    for title_dir in sorted(os.listdir(base_path)):
        if not title_dir.startswith('title_'):
            continue
            
        nodes_file = os.path.join(base_path, title_dir, 'nodes.json')
        if not os.path.exists(nodes_file):
            continue
            
        print(f"Processing {title_dir}...")
        
        with open(nodes_file, 'r') as f:
            nodes = json.load(f)
        
        if not nodes:  # Skip empty files
            continue
            
        sql.append(f"-- Loading {title_dir}\n")
        sql.append("INSERT INTO nodes (")
        sql.append(", ".join(columns))
        sql.append(") VALUES\n")
        
        values = []
        for node in nodes:
            value_list = []
            for col in columns:
                val = node.get(col)
                if val is None:
                    value_list.append('null')
                elif isinstance(val, str):
                    # Escape single quotes and wrap in quotes
                    value_list.append("'" + val.replace("'", "''") + "'")
                elif isinstance(val, (list, dict)):
                    # Convert lists/dicts to JSON string
                    value_list.append("'" + json.dumps(val) + "'::jsonb")
                else:
                    value_list.append(str(val))
            values.append("(" + ", ".join(value_list) + ")")
        
        sql.append(",\n".join(values))
        sql.append(";\n\n")
    
    with open('src/load_nodes.sql', 'w') as f:
        f.write(''.join(sql))

if __name__ == "__main__":
    print("Generating nodes SQL...")
    generate_nodes_sql()
    print("Generating agencies SQL...")
    generate_agencies_sql() 