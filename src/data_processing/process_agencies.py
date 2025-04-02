#!/usr/bin/env python
"""
Script to process agency data into database entities
"""
import os
import json
import logging
from datetime import datetime
from typing import List, Dict, Any, Optional
import argparse

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import models
from src.models.agency import Agency
from src.models.cfr_reference import CFRReference
from src.models.agency_node_mapping import AgencyNodeMapping
from src.database.connector import insert_agencies, insert_cfr_references, insert_agency_node_mappings, get_supabase_client

# Directory for raw and processed data
RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "raw")
PROCESSED_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "processed")

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

def process_agency_data(agency_data: Dict[str, Any], parent_id: Optional[str] = None, depth: int = 0) -> List[Agency]:
    """
    Process agency data recursively to create Agency entities
    
    Args:
        agency_data: Dictionary containing agency data
        parent_id: ID of parent agency (if any)
        depth: Current depth in the hierarchy
        
    Returns:
        List of Agency entities
    """
    agencies = []
    
    # Extract basic agency information
    agency_id = agency_data.get('slug')  # Changed from 'id' to 'slug'
    if not agency_id:
        logger.warning(f"Skipping agency without slug: {agency_data.get('name', 'Unknown')}")
        return []
    
    # Determine if this is a root agency
    is_root = parent_id is None
    
    # Create agency entity
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
        num_words=0,  # Will be calculated later
        num_sections=0,  # Will be calculated later
        num_corrections=0,  # Will be calculated later
        num_cfr_refs=len(agency_data.get('cfr_references', []))  # Count CFR references
    )
    
    agencies.append(agency)
    
    # Process children recursively with incremented depth
    for child in agency_data.get('children', []):
        child_agencies = process_agency_data(child, agency_id, depth + 1)
        agencies.extend(child_agencies)
    
    return agencies

def process_cfr_references(agency_id: str, references_data: List[Dict[str, Any]]) -> List[CFRReference]:
    """
    Process CFR references for an agency
    
    Args:
        agency_id: ID of the agency
        references_data: List of reference data dictionaries
        
    Returns:
        List of CFRReference entities
    """
    references = []
    
    for i, ref_data in enumerate(references_data):
        # Get title number
        title = ref_data.get('title')
        if not title:
            continue
            
        # Build node_id from title and subheading
        subheading = ref_data.get('chapter') or ref_data.get('subchapter') or ref_data.get('subtitle') or ref_data.get('part')
        if not subheading:
            continue
            
        # Get subchapter if present
        subchapter = ref_data.get('subchapter')
            
        node_id = build_node_id(title, subheading, subchapter)
        
        # Generate a unique ID using a hash of the agency_id and node_id
        # This ensures uniqueness while being deterministic
        unique_id = abs(hash(f"{agency_id}:{node_id}:{i}")) % (2**31)  # Ensure positive 32-bit integer
        
        reference = CFRReference(
            id=unique_id,
            agency_id=agency_id,
            title=title,
            subheading=clean_text(subheading),
            ordinal=i,
            node_id=node_id
        )
        references.append(reference)
    
    return references

def process_agency_node_mappings(agency_id: str, references_data: List[Dict[str, Any]]) -> List[AgencyNodeMapping]:
    """
    Process agency-node mappings from CFR references
    
    Args:
        agency_id: ID of the agency
        references_data: List of reference data dictionaries
        
    Returns:
        List of AgencyNodeMapping entities
    """
    mappings = []
    seen_nodes = set()
    
    for i, ref_data in enumerate(references_data):
        # Get title number
        title = ref_data.get('title')
        if not title:
            continue
            
        # Build node_id from title and subheading
        subheading = ref_data.get('chapter') or ref_data.get('subchapter') or ref_data.get('subtitle') or ref_data.get('part')
        if not subheading:
            continue
            
        # Get subchapter if present
        subchapter = ref_data.get('subchapter')
            
        node_id = build_node_id(title, subheading, subchapter)
        
        # Skip if we've already seen this node
        if node_id in seen_nodes:
            continue
        seen_nodes.add(node_id)
        
        # Generate a unique ID using a hash of the agency_id and node_id
        # This ensures uniqueness while being deterministic
        unique_id = abs(hash(f"mapping:{agency_id}:{node_id}")) % (2**31)  # Ensure positive 32-bit integer
        
        mapping = AgencyNodeMapping(
            id=unique_id,
            agency_id=agency_id,
            node_id=node_id,
            is_primary=True,  # These are direct references
            is_direct_reference=True,
            relationship_type='regulatory',  # Default to regulatory relationship
            num_cfr_refs=1  # Each mapping represents one reference
        )
        mappings.append(mapping)
    
    return mappings

def process_agency_file(file_path: str):
    """
    Process a single agency data file
    
    Args:
        file_path: Path to the agency data file
    """
    logger.info(f"Processing agency file: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Get the agencies array from the data
        agencies_data = data.get('agencies', [])
        if not agencies_data:
            logger.error(f"No agencies found in {file_path}")
            return
        
        # Process agencies
        agencies = []
        for agency_data in agencies_data:
            agency_list = process_agency_data(agency_data)
            agencies.extend(agency_list)
        
        if agencies:
            insert_agencies(agencies)
            logger.info(f"Inserted {len(agencies)} agencies")
        
        # Get CFR references for each agency
        all_references = []
        all_mappings = []
        for agency in agencies:
            # Find the original agency data
            agency_data = next((a for a in agencies_data if a.get('slug') == agency.id), None)
            if not agency_data:
                continue
                
            # Process CFR references
            references = process_cfr_references(agency.id, agency_data.get('cfr_references', []))
            if references:
                all_references.extend(references)
            
            # Process agency-node mappings from the same references
            mappings = process_agency_node_mappings(agency.id, agency_data.get('cfr_references', []))
            if mappings:
                all_mappings.extend(mappings)
        
        # Delete existing references and mappings for these agencies
        client = get_supabase_client()
        agency_ids = [agency.id for agency in agencies]
        for agency_id in agency_ids:
            try:
                client.table('cfr_references').delete().eq('agency_id', agency_id).execute()
                client.table('agency_node_mappings').delete().eq('agency_id', agency_id).execute()
            except Exception as e:
                logger.warning(f"Error deleting existing references for agency {agency_id}: {e}")
        
        # Insert new references and mappings
        if all_references:
            insert_cfr_references(all_references)
            logger.info(f"Inserted {len(all_references)} CFR references")
        
        if all_mappings:
            insert_agency_node_mappings(all_mappings)
            logger.info(f"Inserted {len(all_mappings)} agency-node mappings")
        
    except Exception as e:
        logger.error(f"Error processing {file_path}: {e}")
        raise

def process_all_agencies(date=None):
    """
    Process all agency data files for a specific date
    
    Args:
        date: The date of the files to process (default: current date)
    """
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    
    input_dir = os.path.join(RAW_DATA_DIR, date)
    if not os.path.exists(input_dir):
        logger.error(f"No data found for date {date}")
        return
    
    for filename in os.listdir(input_dir):
        if not filename.endswith(".json") or not filename.startswith("agency-"):
            continue
        
        file_path = os.path.join(input_dir, filename)
        process_agency_file(file_path)

def find_matching_node_id(client, title: int, subheading: str) -> Optional[str]:
    """
    Find a matching node ID when exact match fails.
    Since chapters are unique within a title, we can reliably find the correct node
    by matching both title and chapter number.
    
    Args:
        client: Supabase client
        title: CFR title number
        subheading: CFR subheading (chapter/subchapter/etc)
        
    Returns:
        Matching node ID if found, None otherwise
    """
    try:
        # First try exact match
        exact_match = client.table('nodes').select('id').eq('id', f"us/federal/ecfr/title={title}/{subheading}").execute()
        if exact_match.data:
            return exact_match.data[0]['id']
            
        # If no exact match, extract the chapter number if this is a chapter reference
        subheading_parts = subheading.split('=')
        if len(subheading_parts) != 2:
            return None
            
        subheading_type, subheading_value = subheading_parts
        
        # If this is a chapter reference, we can reliably find it by title and chapter
        # since chapters are unique within a title
        if subheading_type.lower() == 'chapter':
            # Search for any node with this title and chapter number
            result = client.table('nodes').select('id').ilike('id', f"%/title={title}%/chapter={subheading_value}%").execute()
            if result.data:
                # Since chapters are unique within a title, we can take the first match
                return result.data[0]['id']
            
    except Exception as e:
        logger.warning(f"Error finding matching node: {e}")
        
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process agency data files')
    parser.add_argument('file', nargs='?', help='Single agency file to process. If not provided, processes all files for latest date.')
    parser.add_argument('--date', help='Date of the files to process (YYYY-MM-DD)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    # Set logging level based on verbose flag
    if not args.verbose:
        logger.setLevel(logging.INFO)
    
    ensure_directory_exists(PROCESSED_DATA_DIR)
    
    if args.file:
        # Process single file
        process_agency_file(args.file)
    else:
        # Process all files for specified date
        process_all_agencies(args.date) 