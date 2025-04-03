import json
import csv
import os
from pathlib import Path

def convert_json_to_csv(json_path, csv_path):
    print(f"Converting {json_path} to {csv_path}")
    
    # Read JSON file
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    # Get fieldnames from first item
    if isinstance(data, list) and len(data) > 0:
        fieldnames = list(data[0].keys())
    else:
        fieldnames = list(data.keys())
    
    # Write CSV file
    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        if isinstance(data, list):
            writer.writerows(data)
        else:
            writer.writerow(data)

def main():
    # Base paths
    json_dir = Path("src/localPush/json_tables/to_load")
    csv_dir = Path("src/localPush/csv_output")
    
    # Ensure CSV directory exists
    csv_dir.mkdir(exist_ok=True)
    
    # Files to convert
    files_to_convert = [
        "all_nodes.json",
        "all_chunks.json",
        "agencies.json",
        "agency_node_mappings.json",
        "cfr_references.json",
        "all_corrections.json"
    ]
    
    # Convert each file
    for json_file in files_to_convert:
        json_path = json_dir / json_file
        csv_file = json_file.replace('.json', '.csv')
        csv_path = csv_dir / csv_file
        
        if json_path.exists():
            convert_json_to_csv(json_path, csv_path)
        else:
            print(f"Warning: {json_path} does not exist")

if __name__ == "__main__":
    main() 