#!/usr/bin/env python
"""
Script to process CFR XML files into database entities
"""
import os
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple
import html
import traceback
import logging
import argparse

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import models
from src.models.node import Node
from src.models.content_chunk import ContentChunk
from src.database.connector import insert_nodes, insert_content_chunks

# Directory for raw and processed data
RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "raw")
PROCESSED_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "processed")

# Base URL for CFR content
BASE_URL = "https://www.ecfr.gov/current"

# Words that indicate a node is reserved
RESERVED_KEYWORDS = ["[RESERVED]", "[Reserved]"]

# Add after the RESERVED_KEYWORDS constant
VALID_TYPES = [
    "TITLE", "SUBTITLE", "CHAPTER", "SUBCHAP", "PART", "SUBPART", 
    "SUBJECT-GROUP", "SECTION", "APPENDIX"
]

# Constants for content chunking
CHUNK_SIZE_BYTES = 800 * 1024  # 800KB
CHUNK_SIZE_WARNING = 700 * 1024  # 700KB - for logging large chunks

def ensure_directory_exists(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def clean_text(text: str) -> str:
    """Clean and normalize text."""
    if text is None:
        return ""
    
    # Replace non-breaking spaces, carriage returns, etc.
    text = text.replace('\xa0', ' ').replace('\r', ' ').replace('\n', ' ')
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Decode HTML entities
    text = html.unescape(text)
    
    return text

def extract_number_from_id(element_id: str) -> str:
    """Extract the number part from an element ID."""
    match = re.search(r'[-_](\d+(?:\.\d+)?(?:[a-zA-Z])?)', element_id)
    if match:
        return match.group(1)
    return element_id

def create_hierarchical_id(components: List[Tuple[str, str]]) -> str:
    """
    Create a hierarchical ID from components.
    
    Args:
        components: List of (level_type, number) tuples
    
    Returns:
        Hierarchical ID (e.g., us/federal/ecfr/title=1/chapter=I/part=1)
    """
    parts = ["us", "federal", "ecfr"]
    
    for level, number in components:
        parts.append(f"{level}={number}")
    
    return "/".join(parts)

def create_citation(components: List[Tuple[str, str]]) -> str:
    """
    Create a citation from components.
    
    Args:
        components: List of (level_type, number) tuples
    
    Returns:
        Formatted citation (e.g., "1 CFR Part 1")
    """
    if not components:
        return ""
    
    title_num = None
    for level, number in components:
        if level == "title":
            title_num = number
            break
    
    if title_num is None:
        return ""
    
    level_type, number = components[-1]
    
    if level_type == "title":
        return f"Title {number} of the CFR"
    elif level_type == "chapter":
        return f"{title_num} CFR Chapter {number}"
    elif level_type == "part":
        return f"{title_num} CFR Part {number}"
    elif level_type == "section":
        parent_level, parent_number = components[-2]
        return f"{title_num} CFR {number}"
    else:
        # Generic format for other levels
        return f"{title_num} CFR {level_type.capitalize()} {number}"

def create_link(components: List[Tuple[str, str]]) -> str:
    """
    Create a link from components.
    
    Args:
        components: List of (level_type, number) tuples
    
    Returns:
        URL to the content
    """
    parts = [BASE_URL]
    
    for level, number in components:
        parts.append(f"{level}-{number}")
    
    return "/".join(parts)

def split_content_into_chunks(content: str, section_id: str) -> List[ContentChunk]:
    """
    Split content into chunks of approximately 800KB each.
    Splits on paragraph boundaries, falling back to sentence boundaries if needed.
    
    Args:
        content: The text content to split
        section_id: The ID of the section this content belongs to
        
    Returns:
        List of ContentChunk objects
    """
    if not content:
        return []
        
    chunks = []
    current_chunk = []
    current_size = 0
    chunk_number = 1
    
    # Split content into paragraphs
    paragraphs = content.split('\n\n')
    
    for paragraph in paragraphs:
        paragraph_size = len(paragraph.encode('utf-8'))
        
        # If a single paragraph is too large, split on sentences
        if paragraph_size > CHUNK_SIZE_BYTES:
            sentences = re.split(r'(?<=[.!?])\s+', paragraph)
            for sentence in sentences:
                sentence_size = len(sentence.encode('utf-8'))
                
                # If current chunk + sentence would exceed limit, create new chunk
                if current_size + sentence_size > CHUNK_SIZE_BYTES:
                    if current_chunk:
                        chunk_content = '\n\n'.join(current_chunk)
                        chunk_id = f"{section_id}_chunk_{chunk_number}"
                        chunks.append(ContentChunk(
                            id=chunk_id,
                            section_id=section_id,
                            chunk_number=chunk_number,
                            content=chunk_content
                        ))
                        chunk_number += 1
                        current_chunk = []
                        current_size = 0
                    
                    # If a single sentence is too large, log warning
                    if sentence_size > CHUNK_SIZE_BYTES:
                        logger.warning(f"Found sentence larger than chunk size in section {section_id}")
                    
                    current_chunk = [sentence]
                    current_size = sentence_size
                else:
                    current_chunk.append(sentence)
                    current_size += sentence_size
        else:
            # If current chunk + paragraph would exceed limit, create new chunk
            if current_size + paragraph_size > CHUNK_SIZE_BYTES:
                if current_chunk:
                    chunk_content = '\n\n'.join(current_chunk)
                    chunk_id = f"{section_id}_chunk_{chunk_number}"
                    chunks.append(ContentChunk(
                        id=chunk_id,
                        section_id=section_id,
                        chunk_number=chunk_number,
                        content=chunk_content
                    ))
                    chunk_number += 1
                    current_chunk = []
                    current_size = 0
                
                current_chunk = [paragraph]
                current_size = paragraph_size
            else:
                current_chunk.append(paragraph)
                current_size += paragraph_size
    
    # Add the last chunk if there's anything left
    if current_chunk:
        chunk_content = '\n\n'.join(current_chunk)
        chunk_id = f"{section_id}_chunk_{chunk_number}"
        chunks.append(ContentChunk(
            id=chunk_id,
            section_id=section_id,
            chunk_number=chunk_number,
            content=chunk_content
        ))
    
    return chunks

def process_children(parent_element, parent_components, parent_id, title_num, nodes, chunks):
    """Process child elements recursively"""
    if not parent_element:
        return
        
    # Look for immediate child DIV elements with a valid TYPE
    logger.info(f"Looking for child elements in {parent_element.name} {parent_element.get('N', '')}")
    for div in parent_element.find_all(["DIV1", "DIV2", "DIV3", "DIV4", "DIV5", "DIV6", "DIV7", "DIV8", "DIV9"], recursive=False):
        div_type = div.get("TYPE", "")
        logger.info(f"Found DIV element: {div.name} with TYPE={div_type}")
        if div_type not in VALID_TYPES:
            logger.info(f"Skipping invalid type: {div_type}")
            continue
            
        logger.info(f"Processing {div_type.lower()} {div.get('N', '')}")
        div_num = div.get("N", "")
        head_elem = div.find("HEAD")
        div_name = clean_text(head_elem.text) if head_elem else ""
        
        # Create components and node for this level
        level_type = div_type.lower()
        div_components = parent_components + [(level_type, div_num)]
        div_id = create_hierarchical_id(div_components)
        div_citation = create_citation(div_components)
        div_link = create_link(div_components)
        
        # Key change: Determine node_type based on level_type, not content
        if level_type in ["section", "appendix"]:
            # Extract content for sections and appendices
            content_elements = div.find_all(["P", "AUTH", "SOURCE", "CITA"])
            content = "\n\n".join(clean_text(elem.text) for elem in content_elements if clean_text(elem.text))
            
            # Split content into chunks
            content_chunks = split_content_into_chunks(content, div_id)
            
            # Calculate total word count
            total_words = sum(len(chunk.content.split()) for chunk in content_chunks)
            
            # Create metadata with chunk information
            metadata = {
                'word_count': total_words,
                'total_chunks': len(content_chunks),
                'first_chunk_id': content_chunks[0].id if content_chunks else None,
                'last_chunk_id': content_chunks[-1].id if content_chunks else None
            }
            
            div_node = Node(
                id=div_id,
                citation=div_citation,
                link=div_link,
                node_type="content",  # Always content for sections/appendix
                level_type=level_type,
                number=div_num,
                node_name=div_name,
                parent=parent_id,
                top_level_title=title_num,
                metadata=metadata
            )
            
            # Add chunks to the list
            chunks.extend(content_chunks)
        else:
            # All other types are structure nodes
            div_node = Node(
                id=div_id,
                citation=div_citation,
                link=div_link,
                node_type="structure",  # Always structure for non-section/appendix
                level_type=level_type,
                number=div_num,
                node_name=div_name,
                parent=parent_id,
                top_level_title=title_num
            )
        
        nodes.append(div_node)
        
        # Process children recursively
        process_children(div, div_components, div_id, title_num, nodes, chunks)

def process_title_xml(xml_file_path: str) -> Tuple[List[Node], List[ContentChunk]]:
    """
    Process a CFR title XML file into database entities
    
    Args:
        xml_file_path: Path to the XML file
    
    Returns:
        Tuple of (list of nodes, list of content chunks)
    """
    logger.info(f"Starting to process {xml_file_path}")
    
    # Parse the XML file
    try:
        with open(xml_file_path, 'r', encoding='utf-8') as f:
            xml_content = f.read()
        
        logger.info(f"XML content length: {len(xml_content)}")
        
        # Use BeautifulSoup for parsing
        soup = BeautifulSoup(xml_content, "xml")
        logger.info(f"BeautifulSoup object created: {soup is not None}")
        
        # Extract title information from DIV1 element
        logger.info("Searching for title element...")
        title_element = soup.find("DIV1", {"TYPE": "TITLE"})
        logger.info(f"Title element found: {title_element is not None}")
        if title_element:
            logger.info(f"Title element attributes: {title_element.attrs}")
        
        if not title_element:
            logger.error(f"No TITLE element found in {xml_file_path}")
            return [], []
        
        # Extract title number and name
        title_num = title_element.get("N", "")
        head_elem = title_element.find("HEAD")
        title_name = clean_text(head_elem.text) if head_elem else ""
        
        # Create the title node
        title_components = [("title", title_num)]
        title_id = create_hierarchical_id(title_components)
        title_citation = create_citation(title_components)
        title_link = create_link(title_components)
        
        title_node = Node(
            id=title_id,
            citation=title_citation,
            link=title_link,
            node_type="structure",
            level_type="title",
            number=title_num,
            node_name=title_name,
            top_level_title=title_num
        )
        
        # Lists to hold all nodes and chunks
        nodes = [title_node]
        chunks = []
        
        # Process the hierarchy recursively
        process_children(title_element, title_components, title_id, title_num, nodes, chunks)
        
        logger.info(f"Finished processing {xml_file_path}. Found {len(nodes)} nodes and {len(chunks)} chunks")
        return nodes, chunks
    
    except Exception as e:
        logger.error(f"Error processing {xml_file_path}: {e}")
        logger.error(traceback.format_exc())
        return [], []

def process_all_titles(date=None):
    """
    Process all downloaded XML files for a specific date
    
    Args:
        date: The date of the files to process (default: current date)
    
    Returns:
        Total number of nodes processed
    """
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    
    input_dir = os.path.join(RAW_DATA_DIR, date)
    if not os.path.exists(input_dir):
        print(f"No data found for date {date}")
        return 0
    
    total_nodes = 0
    total_chunks = 0
    
    # Titles to skip (1-4, 35, and 40)
    skip_titles = set(range(1, 5)) | {35, 40}
    
    for filename in os.listdir(input_dir):
        if not filename.endswith(".xml"):
            continue
            
        # Extract title number from filename
        title_match = re.search(r'title-(\d+)\.xml', filename)
        if not title_match:
            continue
            
        title_num = int(title_match.group(1))
        if title_num in skip_titles:
            print(f"Skipping Title {title_num} (already processed)")
            continue
            
        xml_file_path = os.path.join(input_dir, filename)
        nodes, chunks = process_title_xml(xml_file_path)
        
        if nodes:
            # Write processed nodes to file for backup
            output_file = os.path.join(PROCESSED_DATA_DIR, f"title-{title_num}-processed.txt")
            
            with open(output_file, "w", encoding="utf-8") as f:
                for node in nodes:
                    f.write(f"{node.id}|{node.node_name}|{node.level_type}|{node.parent or 'None'}\n")
            
            # Insert nodes and chunks into database
            try:
                insert_nodes(nodes)
                if chunks:
                    insert_content_chunks(chunks)
                print(f"Inserted {len(nodes)} nodes and {len(chunks)} chunks for {filename}")
            except Exception as e:
                print(f"Error inserting data for {filename}: {e}")
            
            total_nodes += len(nodes)
            total_chunks += len(chunks)
    
    print(f"Processed {total_nodes} total nodes and {total_chunks} total chunks")
    return total_nodes

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process CFR XML files')
    parser.add_argument('file', nargs='?', help='Single XML file to process. If not provided, processes all files for latest date.')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    # Set logging level based on verbose flag
    if not args.verbose:
        logger.setLevel(logging.INFO)
        # Filter out the "Looking for child elements" and "Found DIV element" messages
        class FilterDetailedLogs(logging.Filter):
            def filter(self, record):
                return not (
                    "Looking for child elements" in record.msg or 
                    "Found DIV element" in record.msg or
                    "Processing " in record.msg
                )
        logger.addFilter(FilterDetailedLogs())
    
    ensure_directory_exists(PROCESSED_DATA_DIR)
    
    if args.file:
        # Process single file
        nodes, chunks = process_title_xml(args.file)
        if nodes:
            # Write processed nodes to file for backup
            title_num = nodes[0].number if nodes else "unknown"
            output_file = os.path.join(PROCESSED_DATA_DIR, f"title-{title_num}-processed.txt")
            
            with open(output_file, "w", encoding="utf-8") as f:
                for node in nodes:
                    f.write(f"{node.id}|{node.node_name}|{node.level_type}|{node.parent or 'None'}\n")
            
            # Insert nodes and chunks into database
            try:
                insert_nodes(nodes)
                if chunks:
                    insert_content_chunks(chunks)
                print(f"Inserted {len(nodes)} nodes and {len(chunks)} chunks from {args.file}")
            except Exception as e:
                print(f"Error inserting data from {args.file}: {e}")
    else:
        # Process all files for latest date
        process_all_titles()