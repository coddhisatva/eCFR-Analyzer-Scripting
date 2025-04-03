#!/usr/bin/env python
"""
Script to process corrections data into database entities or local JSON storage
"""
import os
import json
import logging
from datetime import datetime, date
from typing import List, Dict, Any, Optional
import argparse
from dataclasses import asdict

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import models
from src.models.correction import Correction
from src.database.connector import insert_corrections, get_supabase_client

# Directory for raw and processed data
RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "raw", "corrections")
PROCESSED_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "processed", "corrections")
JSON_TABLES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "src", "localPush", "json_tables")

class DateTimeEncoder(json.JSONEncoder):
    """Custom JSON encoder for datetime objects"""
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)

def ensure_directory_exists(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def clean_text(text: Any) -> str:
    """Clean and normalize text."""
    if text is None:
        return ""
    # Convert to string if not already
    return str(text).strip()

def parse_date(date_str: str) -> Optional[datetime]:
    """Parse date string into datetime object."""
    if not date_str:  # Handle empty strings and None
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        try:
            return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            logger.warning(f"Could not parse date: {date_str}")
            return None

def build_node_id(hierarchy: Dict[str, str]) -> str:
    """
    Build a node ID from the hierarchy data.
    Format: us/federal/ecfr/title=X/chapter=Y/subchap=Z/part=W/section=V
    """
    parts = ["us", "federal", "ecfr"]
    
    # Add title
    if 'title' in hierarchy:
        parts.append(f"title={hierarchy['title']}")
    
    # Add chapter
    if 'chapter' in hierarchy:
        parts.append(f"chapter={hierarchy['chapter']}")
    
    # Add subchapter (converted to subchap)
    if 'subchapter' in hierarchy:
        parts.append(f"subchap={hierarchy['subchapter']}")
    
    # Add part
    if 'part' in hierarchy:
        parts.append(f"part={hierarchy['part']}")
    elif 'section' in hierarchy:
        # If we have a section but no part, try to infer the part number
        section = hierarchy['section'].strip().strip('-').strip()
        if '.' in section:
            # Part number is everything before the dot
            part = section.split('.')[0]
            parts.append(f"part={part}")
    
    # Add subpart if present
    if 'subpart' in hierarchy:
        parts.append(f"subpart={hierarchy['subpart']}")
    
    # Add section
    if 'section' in hierarchy:
        # Clean up section number by removing whitespace and dashes
        section = hierarchy['section'].strip().strip('-').strip()
        parts.append(f"section={section}")
    
    return '/'.join(parts)

def find_matching_node_id(client, hierarchy: Dict[str, str]) -> Optional[str]:
    """
    Find a matching node ID when exact match fails.
    Falls back to higher level nodes if exact match isn't found.
    
    Args:
        client: Supabase client
        hierarchy: Dictionary containing title, chapter, etc.
        
    Returns:
        Matching node ID if found, None otherwise
    """
    try:
        # Get title - this is the minimum we need
        title = hierarchy.get('title')
        if not title:
            return None
            
        # First try exact match with the full node_id
        node_id = build_node_id(hierarchy)
        exact_match = client.table('nodes').select('id').eq('id', node_id).execute()
        if exact_match.data:
            return exact_match.data[0]['id']
            
        # If no exact match, try matching at each level, starting from most specific
        # Build parts of the path we have
        path_parts = []
        path_parts.append(f"title={title}")
        
        if hierarchy.get('chapter'):
            path_parts.append(f"chapter={hierarchy['chapter']}")
            
        if hierarchy.get('subchapter'):
            path_parts.append(f"subchap={hierarchy['subchapter']}")
            
        if hierarchy.get('part'):
            path_parts.append(f"part={hierarchy['part']}")
        elif hierarchy.get('section'):
            # If we have a section but no part, try to infer the part number
            section = hierarchy['section'].strip().strip('-').strip()
            if '.' in section:
                part = section.split('.')[0]
                path_parts.append(f"part={part}")
                
        if hierarchy.get('subpart'):
            path_parts.append(f"subpart={hierarchy['subpart']}")
            
        if hierarchy.get('section'):
            section = hierarchy['section'].strip().strip('-').strip()
            path_parts.append(f"section={section}")
        
        # Try matching at each level, from most specific to least
        while path_parts:
            # Build the path to try
            path = "us/federal/ecfr/" + "/".join(path_parts)
            match = client.table('nodes').select('id').eq('id', path).execute()
            if match.data:
                return match.data[0]['id']
            # Remove the last part and try again
            path_parts.pop()
        
        # If we get here, we couldn't find any match
        # Fall back to title level
        title_path = f"us/federal/ecfr/title={title}"
        title_match = client.table('nodes').select('id').eq('id', title_path).execute()
        if title_match.data:
            return title_match.data[0]['id']
            
    except Exception as e:
        logger.warning(f"Error finding matching node: {e}")
        
    return None

def find_matching_node_id_local(hierarchy: Dict[str, str], nodes: List[Dict]) -> Optional[str]:
    """
    Find a matching node ID using local nodes data.
    If exact match isn't found, falls back to higher level nodes.
    
    Args:
        hierarchy: Dictionary containing title, chapter, etc.
        nodes: List of node dictionaries from JSON
        
    Returns:
        Matching node ID if found, None otherwise
    """
    # Get title - this is the minimum we need
    title = hierarchy.get('title')
    if not title:
        return None
        
    # First try exact match with the full node_id
    node_id = build_node_id(hierarchy)
    exact_match = next((n for n in nodes if n['id'] == node_id), None)
    if exact_match:
        return exact_match['id']
    
    # If no exact match, try matching at each level, starting from most specific
    # Build parts of the path we have
    path_parts = []
    path_parts.append(f"title={title}")
    
    if hierarchy.get('chapter'):
        path_parts.append(f"chapter={hierarchy['chapter']}")
        
    if hierarchy.get('subchapter'):
        path_parts.append(f"subchap={hierarchy['subchapter']}")
        
    if hierarchy.get('part'):
        path_parts.append(f"part={hierarchy['part']}")
    elif hierarchy.get('section'):
        # If we have a section but no part, try to infer the part number
        section = hierarchy['section'].strip().strip('-').strip()
        if '.' in section:
            part = section.split('.')[0]
            path_parts.append(f"part={part}")
            
    if hierarchy.get('subpart'):
        path_parts.append(f"subpart={hierarchy['subpart']}")
        
    if hierarchy.get('section'):
        section = hierarchy['section'].strip().strip('-').strip()
        path_parts.append(f"section={section}")
    
    # Try matching at each level, from most specific to least
    while path_parts:
        # Build the path to try
        path = "us/federal/ecfr/" + "/".join(path_parts)
        match = next((n for n in nodes if n['id'] == path), None)
        if match:
            return match['id']
        # Remove the last part and try again
        path_parts.pop()
    
    # If we get here, we couldn't find any match
    # Fall back to title level
    title_path = f"us/federal/ecfr/title={title}"
    title_match = next((n for n in nodes if n['id'] == title_path), None)
    if title_match:
        return title_match['id']
    
    return None

def process_correction_data(correction_data: Dict[str, Any], nodes: Optional[List[Dict]] = None, client = None) -> List[Correction]:
    """
    Process correction data into Correction entities
    
    Args:
        correction_data: Dictionary containing correction data
        nodes: List of node dictionaries from JSON (for local processing)
        client: Supabase client for node lookups (for database processing)
        
    Returns:
        List of Correction entities (one for each CFR reference)
    """
    corrections = []
    
    # Extract common correction data
    error_corrected = parse_date(correction_data.get('error_corrected', ''))
    error_occurred = parse_date(correction_data.get('error_occurred', ''))
    correction_duration = (error_corrected - error_occurred).days if error_corrected and error_occurred else None
    
    # Process each CFR reference
    for i, cfr_ref in enumerate(correction_data.get('cfr_references', [])):
        # Try to find matching node using hierarchy
        hierarchy = cfr_ref.get('hierarchy', {})
        if nodes:
            node_id = find_matching_node_id_local(hierarchy, nodes)
        else:
            node_id = find_matching_node_id(client, hierarchy)
            
        if not node_id:
            logger.warning(f"Could not find matching node for title={hierarchy.get('title')}, chapter={hierarchy.get('chapter')}")
            continue
        
        # Generate a unique ID using a hash of the node_id and index
        # This ensures uniqueness while being deterministic
        unique_id = abs(hash(f"correction:{node_id}:{i}")) % (2**31)  # Ensure positive 32-bit integer
        
        # Create correction entity
        correction = Correction(
            id=unique_id,
            node_id=node_id,
            agency_id=correction_data.get('agency_id'),  # Store agency_id if present
            title=correction_data.get('title', ''),
            corrective_action=clean_text(correction_data.get('corrective_action', '')),
            error_corrected=error_corrected,
            error_occurred=error_occurred,
            correction_duration=correction_duration,
            fr_citation=clean_text(correction_data.get('fr_citation', '')),
            position=clean_text(correction_data.get('position', '')),
            year=correction_data.get('year'),
            metadata={
                'cfr_reference': clean_text(cfr_ref.get('cfr_reference', '')),
                'last_modified': correction_data.get('last_modified'),
                'display_in_toc': correction_data.get('display_in_toc'),
                'last_updated': datetime.now().isoformat()
            }
        )
        corrections.append(correction)
    
    return corrections

def build_corrections_maps(corrections: List[Correction], nodes: List[Dict], agencies: List[Dict]) -> Dict:
    """
    Build maps for node and agency corrections, and propagate counts up the tree.
    
    Args:
        corrections: List of Correction objects
        nodes: List of node dictionaries from JSON
        agencies: List of agency dictionaries from JSON
        
    Returns:
        Dictionary containing the corrections maps and propagated counts
    """
    # Initialize maps
    node_corrections = {}  # node_id -> count
    agency_corrections = {}  # agency_id -> count
    
    # Count direct corrections
    for correction in corrections:
        # Count node corrections
        if correction.node_id:
            node_corrections[correction.node_id] = node_corrections.get(correction.node_id, 0) + 1
        
        # Count agency corrections
        if correction.agency_id:
            agency_corrections[correction.agency_id] = agency_corrections.get(correction.agency_id, 0) + 1
    
    # Propagate node corrections up the tree
    for node in nodes:
        if node['parent'] and node['id'] in node_corrections:
            current_id = node['parent']
            while current_id:
                node_corrections[current_id] = node_corrections.get(current_id, 0) + node_corrections[node['id']]
                # Find parent node
                parent_node = next((n for n in nodes if n['id'] == current_id), None)
                current_id = parent_node['parent'] if parent_node else None
    
    # Propagate agency corrections up the hierarchy
    for agency in agencies:
        if agency['parent_id'] and agency['id'] in agency_corrections:
            current_id = agency['parent_id']
            while current_id:
                agency_corrections[current_id] = agency_corrections.get(current_id, 0) + agency_corrections[agency['id']]
                # Find parent agency
                parent_agency = next((a for a in agencies if a['id'] == current_id), None)
                current_id = parent_agency['parent_id'] if parent_agency else None
    
    return {
        'node_corrections': node_corrections,
        'agency_corrections': agency_corrections
    }

def save_corrections_to_json(corrections: List[Correction], maps: Dict, title_num: str) -> None:
    """
    Save corrections data and maps to JSON files.
    
    Args:
        corrections: List of Correction objects
        maps: Dictionary containing node and agency correction maps
        title_num: The title number these corrections belong to
    """
    # Create directories if they don't exist
    ensure_directory_exists(JSON_TABLES_DIR)
    title_dir = os.path.join(JSON_TABLES_DIR, f"title_{title_num}")
    ensure_directory_exists(title_dir)
    
    # Save corrections
    corrections_file = os.path.join(title_dir, "corrections.json")
    with open(corrections_file, 'w', encoding='utf-8') as f:
        json.dump([asdict(c) for c in corrections], f, indent=2, ensure_ascii=False, cls=DateTimeEncoder)
    
    # Save correction maps
    maps_file = os.path.join(title_dir, "correction_maps.json")
    with open(maps_file, 'w', encoding='utf-8') as f:
        json.dump(maps, f, indent=2, ensure_ascii=False)
    
    # Save summary
    summary = {
        "title": title_num,
        "correction_count": len(corrections),
        "node_correction_count": len(maps['node_corrections']),
        "agency_correction_count": len(maps['agency_corrections']),
        "last_updated": datetime.now().isoformat()
    }
    summary_file = os.path.join(title_dir, "corrections_summary.json")
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

def process_corrections_file(file_path: str, use_local_storage: bool = False):
    """
    Process a single corrections data file
    
    Args:
        file_path: Path to the corrections data file
        use_local_storage: Whether to store data locally instead of in database
    """
    logger.info(f"Processing corrections file: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Process corrections
        all_corrections = []
        
        if use_local_storage:
            # Load all nodes from all title folders
            all_nodes = []
            all_agencies = []
            
            # Get all title folders
            for title_dir in os.listdir(JSON_TABLES_DIR):
                if not title_dir.startswith('title_'):
                    continue
                    
                title_path = os.path.join(JSON_TABLES_DIR, title_dir)
                if not os.path.isdir(title_path):
                    continue
                    
                # Load nodes
                nodes_file = os.path.join(title_path, "nodes.json")
                if os.path.exists(nodes_file):
                    with open(nodes_file, 'r', encoding='utf-8') as f:
                        all_nodes.extend(json.load(f))
                        
                # Load agencies
                agencies_file = os.path.join(title_path, "agencies.json")
                if os.path.exists(agencies_file):
                    with open(agencies_file, 'r', encoding='utf-8') as f:
                        all_agencies.extend(json.load(f))
            
            logger.info(f"Loaded {len(all_nodes)} nodes and {len(all_agencies)} agencies from all title folders")
            
            # First pass: Process all corrections and build initial maps
            node_corrections = {}  # node_id -> count
            agency_corrections = {}  # agency_id -> count
            
            for correction_data in data.get('ecfr_corrections', []):
                corrections = process_correction_data(correction_data, nodes=all_nodes)
                all_corrections.extend(corrections)
                
                # Build initial correction maps
                for correction in corrections:
                    if correction.node_id:
                        node_corrections[correction.node_id] = node_corrections.get(correction.node_id, 0) + 1
                    if correction.agency_id:
                        agency_corrections[correction.agency_id] = agency_corrections.get(correction.agency_id, 0) + 1
            
            # Second pass: Propagate node corrections up the tree
            for node in all_nodes:
                if node['parent'] and node['id'] in node_corrections:
                    current_id = node['parent']
                    while current_id:
                        node_corrections[current_id] = node_corrections.get(current_id, 0) + node_corrections[node['id']]
                        # Find parent node
                        parent_node = next((n for n in all_nodes if n['id'] == current_id), None)
                        current_id = parent_node['parent'] if parent_node else None
            
            # Third pass: Propagate agency corrections up the hierarchy
            for agency in all_agencies:
                if agency['parent_id'] and agency['id'] in agency_corrections:
                    current_id = agency['parent_id']
                    while current_id:
                        agency_corrections[current_id] = agency_corrections.get(current_id, 0) + agency_corrections[agency['id']]
                        # Find parent agency
                        parent_agency = next((a for a in all_agencies if a['id'] == current_id), None)
                        current_id = parent_agency['parent_id'] if parent_agency else None
            
            # Fourth pass: Update node and agency objects with correction counts
            for node in all_nodes:
                node['num_corrections'] = node_corrections.get(node['id'], 0)
            
            for agency in all_agencies:
                agency['num_corrections'] = agency_corrections.get(agency['id'], 0)
            
            # Save everything back to JSON
            title_num = data.get('ecfr_corrections', [{}])[0].get('title')
            if title_num:
                # Save corrections
                save_corrections_to_json(all_corrections, {
                    'node_corrections': node_corrections,
                    'agency_corrections': agency_corrections
                }, title_num)
                
                # Save updated nodes
                title_dir = os.path.join(JSON_TABLES_DIR, f"title_{title_num}")
                nodes_file = os.path.join(title_dir, "nodes.json")
                with open(nodes_file, 'w', encoding='utf-8') as f:
                    json.dump(all_nodes, f, indent=2, ensure_ascii=False)
                
                # Save updated agencies
                agencies_file = os.path.join(title_dir, "agencies.json")
                with open(agencies_file, 'w', encoding='utf-8') as f:
                    json.dump(all_agencies, f, indent=2, ensure_ascii=False)
                
                logger.info(f"Saved {len(all_corrections)} corrections and updated {len(all_nodes)} nodes and {len(all_agencies)} agencies")
            else:
                logger.error("Could not determine title number from corrections data")
        else:
            # Get Supabase client for database processing
            client = get_supabase_client()
            
            # Process corrections using database lookups
            for correction_data in data.get('ecfr_corrections', []):
                corrections = process_correction_data(correction_data, client=client)
                all_corrections.extend(corrections)
            
            if all_corrections:
                insert_corrections(all_corrections)
                logger.info(f"Inserted {len(all_corrections)} corrections into database")
        
    except Exception as e:
        logger.error(f"Error processing {file_path}: {e}")
        raise

def process_all_corrections(date=None, use_local_storage=False):
    """
    Process all corrections data files for a specific date
    
    Args:
        date: The date of the files to process (default: current date)
        use_local_storage: Whether to store data locally instead of in database
    """
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    
    input_dir = os.path.join(RAW_DATA_DIR, date)
    if not os.path.exists(input_dir):
        logger.error(f"No data found for date {date}")
        return
    
    for filename in os.listdir(input_dir):
        if not filename.endswith(".json") or not filename.startswith("corrections-"):
            continue
        
        file_path = os.path.join(input_dir, filename)
        process_corrections_file(file_path, use_local_storage)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process corrections data files')
    parser.add_argument('file', nargs='?', help='Single corrections file to process. If not provided, processes all files for latest date.')
    parser.add_argument('--date', help='Date of the files to process (YYYY-MM-DD)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    parser.add_argument('--local', '-l', action='store_true', help='Store data locally in JSON format instead of database')
    
    args = parser.parse_args()
    
    # Set logging level based on verbose flag
    if not args.verbose:
        logger.setLevel(logging.INFO)
    
    ensure_directory_exists(PROCESSED_DATA_DIR)
    
    if args.file:
        # Process single file
        process_corrections_file(args.file, args.local)
    else:
        # Process all files for specified date
        process_all_corrections(args.date, args.local) 