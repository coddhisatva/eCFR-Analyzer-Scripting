import json
import os
from pathlib import Path

base_path = Path('src/localPush/json_tables')
output_path = base_path / 'combined'
output_path.mkdir(exist_ok=True)

# Combine nodes.json from all titles
all_nodes = []
all_chunks = []

for title_num in range(1, 51):
    if title_num == 35:  # Skip title 35
        continue
    
    title_dir = base_path / f'title_{title_num}'
    
    # Process nodes
    nodes_file = title_dir / 'nodes.json'
    if nodes_file.exists():
        with open(nodes_file) as f:
            title_nodes = json.load(f)
            if isinstance(title_nodes, list):
                all_nodes.extend(title_nodes)
            else:
                all_nodes.append(title_nodes)
    
    # Process content chunks
    chunks_file = title_dir / 'content_chunks.json'
    if chunks_file.exists():
        with open(chunks_file) as f:
            title_chunks = json.load(f)
            if isinstance(title_chunks, list):
                all_chunks.extend(title_chunks)
            else:
                all_chunks.append(title_chunks)

# Write combined files
with open(output_path / 'all_nodes.json', 'w') as f:
    json.dump(all_nodes, f)

with open(output_path / 'all_chunks.json', 'w') as f:
    json.dump(all_chunks, f)

print(f"Combined {len(all_nodes)} nodes into all_nodes.json")
print(f"Combined {len(all_chunks)} chunks into all_chunks.json") 