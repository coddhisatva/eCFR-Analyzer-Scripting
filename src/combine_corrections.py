import json
import glob
import os

def combine_corrections():
    all_corrections = []
    base_dir = 'src/localPush/json_tables'
    
    # Get all title directories
    title_dirs = sorted(glob.glob(os.path.join(base_dir, 'title_*')))
    
    print(f"Found {len(title_dirs)} title directories")
    
    # Process each title's corrections
    for title_dir in title_dirs:
        corrections_file = os.path.join(title_dir, 'corrections.json')
        if os.path.exists(corrections_file):
            print(f"Processing {corrections_file}")
            with open(corrections_file, 'r') as f:
                corrections = json.load(f)
                all_corrections.extend(corrections)
    
    print(f"Total corrections found: {len(all_corrections)}")
    
    # Save combined corrections
    output_file = os.path.join(base_dir, 'to_load', 'all_corrections.json')
    with open(output_file, 'w') as f:
        json.dump(all_corrections, f, indent=2)
    print(f"Saved combined corrections to {output_file}")

if __name__ == '__main__':
    combine_corrections() 