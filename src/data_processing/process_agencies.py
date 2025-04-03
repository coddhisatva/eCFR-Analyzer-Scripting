#!/usr/bin/env python
"""
Script to process agency data into database entities or local JSON storage
"""
import os
import json
import logging
from datetime import datetime
from typing import List, Dict, Any, Optional
import argparse
from dataclasses import asdict

# Set up basic logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import models
from src.models.agency import Agency
from src.models.cfr_reference import CFRReference
from src.models.agency_node_mapping import AgencyNodeMapping
from src.database.connector import insert_agencies, insert_cfr_references, insert_agency_node_mappings, get_supabase_client

# Directory for raw and processed data
RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "raw")
PROCESSED_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "processed")
JSON_TABLES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "src", "localPush", "json_tables")

def ensure_directory_exists(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def clean_text(text: str) -> str:
    """Clean and normalize text."""
    if text is None:
        return ""
    return text.strip()

def roman_to_arabic(roman: str) -> int:
    """Convert Roman numeral to Arabic numeral."""
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    result = 0
    prev_value = 0
    
    for char in reversed(roman.upper()):
        curr_value = roman_values[char]
        if curr_value >= prev_value:
            result += curr_value
        else:
            result -= curr_value
        prev_value = curr_value
    
    return result

def build_node_id(title: int, subheading: str, subchapter: str = None) -> str:
    """
    Build a node ID from title and subheading.
    Handles different subheading types and formats.
    """
    # Convert subheading type to node format
    subheading = subheading.upper()
    
    # Handle chapter format
    if subheading.startswith('CHAPTER'):
        parts = subheading.split(' ', 1)
        if len(parts) > 1:
            number = parts[1]
    else:
        number = subheading
    
    # Create components list like XML processing
    components = [("title", str(title)), ("chapter", number)]
    
    # Add subchapter if present
    if subchapter:
        components.append(("subchap", subchapter))
    
    # Build hierarchical ID
    parts = ["us", "federal", "ecfr"]
    for level, num in components:
        parts.append(f"{level}={num}")
    
    return "/".join(parts)

def determine_agency_type(agency_data: Dict[str, Any], is_root: bool) -> str:
    """
    Determine agency type based on hierarchy and children.
    """
    if is_root:
        return 'root'
    elif agency_data.get('children'):
        return 'middle'
    else:
        return 'zed'

def find_matching_node_id(client, title: str, subheading: str) -> Optional[str]:
    """
    Find a matching node ID for a given title and subheading.
    Handles different subheading types (chapter, subtitle, subchapter) interchangeably.
    
    Args:
        client: Supabase client
        title: Title number
        subheading: Subheading identifier (e.g., "chapter=A" or "subtitle=A")
        
    Returns:
        Matching node ID if found, None otherwise
    """
    try:
        # First try exact match
        node_id = f"us/federal/ecfr/title={title}/{subheading}"
        exact_match = client.table('nodes').select('id').eq('id', node_id).execute()
        if exact_match.data:
            return exact_match.data[0]['id']
            
        # If no exact match, try different subheading types
        subheading_types = ['chapter', 'subtitle', 'subchapter']
        subheading_value = subheading.split('=')[1]  # Get the value (e.g., "A")
        
        for heading_type in subheading_types:
            if heading_type not in subheading:  # Skip if it's the same type we already tried
                test_id = f"us/federal/ecfr/title={title}/{heading_type}={subheading_value}"
                match = client.table('nodes').select('id').eq('id', test_id).execute()
                if match.data:
                    return match.data[0]['id']
        
        # If still no match, try at title level
        title_id = f"us/federal/ecfr/title={title}"
        title_match = client.table('nodes').select('id').eq('id', title_id).execute()
        if title_match.data:
            return title_match.data[0]['id']
            
    except Exception as e:
        logger.warning(f"Error finding matching node: {e}")
        
    return None

def process_agency_data(agency_data: Dict[str, Any], parent_id: Optional[str] = None, depth: int = 0, use_local_storage: bool = False) -> List[Agency]:
    """
    Process agency data recursively to create Agency entities
    
    Args:
        agency_data: Dictionary containing agency data
        parent_id: ID of parent agency (if any)
        depth: Current depth in the hierarchy
        use_local_storage: Whether to use local storage instead of database
        
    Returns:
        List of Agency entities
    """
    agencies = []
    
    # Extract basic agency information
    agency_id = agency_data.get('slug')
    if not agency_id:
        logger.warning(f"Skipping agency without slug: {agency_data.get('name', 'Unknown')}")
        return []
    
    logger.info(f"Processing agency: {agency_id} at depth {depth}")
    
    # Determine if this is a root agency
    is_root = parent_id is None
    
    # Get CFR references for this agency
    cfr_refs = []
    
    # Only get client if not using local storage
    client = None if use_local_storage else get_supabase_client()
    
    for ref in agency_data.get('cfr_references', []):
        # Get title number
        title = ref.get('title')
        if not title:
            continue
            
        # Build node_id from title and subheading
        subheading = ref.get('chapter') or ref.get('subchapter') or ref.get('subtitle') or ref.get('part')
        if not subheading:
            continue
            
        if use_local_storage:
            # In local mode, just build the node ID directly
            node_id = build_node_id(title, subheading)
        else:
            # In database mode, try to find the matching node
            node_id = find_matching_node_id(client, title, f"chapter={subheading}")
            if not node_id:
                logger.warning(f"Could not find matching node for title={title}, chapter={subheading}")
                continue
        
        cfr_refs.append(node_id)
    
    logger.info(f"Found {len(cfr_refs)} CFR references for agency {agency_id}")
    
    # Create agency entity with metrics
    agency = Agency(
        id=agency_id,
        name=clean_text(agency_data.get('name', '')),
        short_name=clean_text(agency_data.get('short_name', '')),
        display_name=clean_text(agency_data.get('display_name', '')),
        sortable_name=clean_text(agency_data.get('sortable_name', '')),
        parent_id=parent_id,
        depth=depth,
        agency_type=determine_agency_type(agency_data, is_root),
        metadata={
            'description': clean_text(agency_data.get('description', '')),
            'website': clean_text(agency_data.get('website', '')),
            'contact_info': clean_text(agency_data.get('contact_info', '')),
            'last_updated': datetime.now().isoformat()
        },
        num_children=len(agency_data.get('children', [])),
        num_cfr=len(cfr_refs),
        num_words=0,  # Will be calculated later
        num_sections=0,  # Will be calculated later
        num_corrections=0,  # Will be calculated later
        cfr_references=cfr_refs  # Store node IDs
    )
    
    agencies.append(agency)
    
    # Process children recursively with incremented depth
    for child in agency_data.get('children', []):
        child_agencies = process_agency_data(child, agency_id, depth + 1, use_local_storage)
        agencies.extend(child_agencies)
        
        # Propagate child's CFR references up to parent
        if child_agencies:
            for child_agency in child_agencies:
                agency.cfr_references.extend(child_agency.cfr_references)
                agency.num_cfr = len(agency.cfr_references)  # Update count
    
    return agencies

def save_to_json(agencies: List[Agency], cfr_references: List[CFRReference], agency_node_mappings: List[AgencyNodeMapping]) -> None:
    """
    Save processed data to JSON files
    
    Args:
        agencies: List of Agency entities
        cfr_references: List of CFRReference entities
        agency_node_mappings: List of AgencyNodeMapping entities
    """
    logger.info("Saving data to JSON files...")
    
    # Create directories if they don't exist
    ensure_directory_exists(JSON_TABLES_DIR)
    
    # Save agencies
    agencies_file = os.path.join(JSON_TABLES_DIR, "agencies.json")
    with open(agencies_file, 'w', encoding='utf-8') as f:
        json.dump([asdict(a) for a in agencies], f, indent=2, ensure_ascii=False)
    logger.info(f"Saved {len(agencies)} agencies to {agencies_file}")
    
    # Save CFR references
    cfr_file = os.path.join(JSON_TABLES_DIR, "cfr_references.json")
    with open(cfr_file, 'w', encoding='utf-8') as f:
        json.dump([asdict(r) for r in cfr_references], f, indent=2, ensure_ascii=False)
    logger.info(f"Saved {len(cfr_references)} CFR references to {cfr_file}")
    
    # Save agency node mappings
    mappings_file = os.path.join(JSON_TABLES_DIR, "agency_node_mappings.json")
    with open(mappings_file, 'w', encoding='utf-8') as f:
        json.dump([asdict(m) for m in agency_node_mappings], f, indent=2, ensure_ascii=False)
    logger.info(f"Saved {len(agency_node_mappings)} agency node mappings to {mappings_file}")
    
    # Save summary
    summary = {
        "total_agencies": len(agencies),
        "total_cfr_references": len(cfr_references),
        "total_mappings": len(agency_node_mappings),
        "last_updated": datetime.now().isoformat()
    }
    summary_file = os.path.join(JSON_TABLES_DIR, "agencies_summary.json")
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    logger.info(f"Saved summary to {summary_file}")

def process_agencies_file(file_path: str, use_local_storage: bool = False):
    """
    Process a single agencies data file
    
    Args:
        file_path: Path to the agencies data file
        use_local_storage: Whether to store data locally instead of in database
    """
    logger.info(f"Processing agencies file: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        agencies_data = data.get('agencies', [])
        if not agencies_data:
            logger.error(f"No agencies found in {file_path}")
            return
        
        # Process agencies
        all_agencies = []
        all_cfr_references = []
        all_agency_node_mappings = []
        
        for agency_data in agencies_data:
            agencies = process_agency_data(agency_data, use_local_storage=use_local_storage)
            all_agencies.extend(agencies)
            
            # Create CFR references and mappings
            for agency in agencies:
                for node_id in agency.cfr_references:
                    # Create CFR reference
                    cfr_ref = CFRReference(
                        agency_id=agency.id,
                        node_id=node_id,
                        title=int(node_id.split('/')[3].split('=')[1])  # Extract title from node_id
                    )
                    all_cfr_references.append(cfr_ref)
                    
                    # Create agency node mapping
                    mapping = AgencyNodeMapping(
                        agency_id=agency.id,
                        node_id=node_id,
                        metadata={
                            'last_updated': datetime.now().isoformat()
                        }
                    )
                    all_agency_node_mappings.append(mapping)
        
        if use_local_storage:
            save_to_json(all_agencies, all_cfr_references, all_agency_node_mappings)
        else:
            # Insert into database
            insert_agencies(all_agencies)
            insert_cfr_references(all_cfr_references)
            insert_agency_node_mappings(all_agency_node_mappings)
            logger.info(f"Inserted {len(all_agencies)} agencies, {len(all_cfr_references)} CFR references, and {len(all_agency_node_mappings)} mappings into database")
        
    except Exception as e:
        logger.error(f"Error processing {file_path}: {e}")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process agencies data files')
    parser.add_argument('file', nargs='?', help='Single agencies file to process. If not provided, processes all files for latest date.')
    parser.add_argument('--date', help='Date of the files to process (YYYY-MM-DD)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    parser.add_argument('--local', '-l', action='store_true', help='Store data locally in JSON format instead of database')
    
    args = parser.parse_args()
    
    # Set logging level based on verbose flag
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    ensure_directory_exists(PROCESSED_DATA_DIR)
    
    if args.file:
        # Process single file
        process_agencies_file(args.file, args.local)
    else:
        # Process all files for specified date
        if args.date is None:
            args.date = datetime.now().strftime("%Y-%m-%d")
        
        input_dir = os.path.join(RAW_DATA_DIR, "agencies", args.date)
        if not os.path.exists(input_dir):
            logger.error(f"No data found for date {args.date}")
            return
        
        for filename in os.listdir(input_dir):
            if not filename.endswith(".json") or not filename.startswith("agencies-"):
                continue
            
            file_path = os.path.join(input_dir, filename)
            process_agencies_file(file_path, args.local) 