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

# Import models
from src.models.node import Node
from src.database.connector import insert_nodes

# Directory for raw and processed data
RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "raw")
PROCESSED_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "processed")

# Base URL for CFR content
BASE_URL = "https://www.ecfr.gov/current"

# Words that indicate a node is reserved
RESERVED_KEYWORDS = ["[RESERVED]", "[Reserved]"]

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

def process_title_xml(xml_file_path: str) -> List[Node]:
    """
    Process a CFR title XML file into database entities
    
    Args:
        xml_file_path: Path to the XML file
    
    Returns:
        List of node entities to be stored in the database
    """
    print(f"Processing {xml_file_path}...")
    
    # Parse the XML file
    try:
        with open(xml_file_path, 'r', encoding='utf-8') as f:
            xml_content = f.read()
        
        # Use BeautifulSoup for parsing
        soup = BeautifulSoup(xml_content, "xml")
        
        # Extract title information
        title_element = soup.find("TITLE")
        if not title_element:
            print(f"No TITLE element found in {xml_file_path}")
            return []
        
        # Extract title number and name
        title_num = title_element.get("titlenum", "")
        title_name = clean_text(title_element.get("heading", ""))
        
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
            node_name=f"Title {title_num} - {title_name}",
            top_level_title=title_num
        )
        
        # List to hold all nodes
        nodes = [title_node]
        
        # Process the hierarchy recursively
        process_children(title_element, title_components, title_id, title_num, nodes)
        
        print(f"Processed {len(nodes)} nodes from {xml_file_path}")
        return nodes
    
    except Exception as e:
        print(f"Error processing {xml_file_path}: {e}")
        traceback.print_exc()
        return []

def process_children(parent_element, parent_components, parent_id, title_num, nodes):
    """
    Recursively process child elements
    
    Args:
        parent_element: The parent XML element
        parent_components: List of (level_type, number) tuples for the parent
        parent_id: The parent node ID
        title_num: The title number
        nodes: List to append nodes to
    """
    if not parent_element:
        return
    
    # Process chapters if present
    for chapter in parent_element.find_all("CHAPTER", recursive=False):
        process_chapter(chapter, parent_components, parent_id, title_num, nodes)
    
    # Process parts directly under title if present
    for part in parent_element.find_all("PART", recursive=False):
        process_part(part, parent_components, parent_id, title_num, nodes)

def process_chapter(chapter, parent_components, parent_id, title_num, nodes):
    """Process a chapter element"""
    chapter_num = chapter.get("chapternum", "")
    chapter_name = clean_text(chapter.get("heading", ""))
    
    # Check if reserved
    reserved = None
    for keyword in RESERVED_KEYWORDS:
        if keyword in chapter_name:
            reserved = "reserved"
            break
    
    # Create chapter components and ID
    chapter_components = parent_components + [("chapter", chapter_num)]
    chapter_id = create_hierarchical_id(chapter_components)
    chapter_citation = create_citation(chapter_components)
    chapter_link = create_link(chapter_components)
    
    chapter_node = Node(
        id=chapter_id,
        citation=chapter_citation,
        link=chapter_link,
        node_type="structure",
        level_type="chapter",
        number=chapter_num,
        node_name=chapter_name,
        parent=parent_id,
        top_level_title=title_num,
        reserved=reserved
    )
    
    nodes.append(chapter_node)
    
    # Process subchapters if present
    for subchapter in chapter.find_all("SUBCHAP", recursive=False):
        process_subchapter(subchapter, chapter_components, chapter_id, title_num, nodes)
    
    # Process parts under chapter
    for part in chapter.find_all("PART", recursive=False):
        process_part(part, chapter_components, chapter_id, title_num, nodes)

def process_subchapter(subchapter, parent_components, parent_id, title_num, nodes):
    """Process a subchapter element"""
    subchapter_num = subchapter.get("subchapnum", "")
    subchapter_name = clean_text(subchapter.get("heading", ""))
    
    # Check if reserved
    reserved = None
    for keyword in RESERVED_KEYWORDS:
        if keyword in subchapter_name:
            reserved = "reserved"
            break
    
    # Create subchapter components and ID
    subchapter_components = parent_components + [("subchapter", subchapter_num)]
    subchapter_id = create_hierarchical_id(subchapter_components)
    subchapter_citation = create_citation(subchapter_components)
    subchapter_link = create_link(subchapter_components)
    
    subchapter_node = Node(
        id=subchapter_id,
        citation=subchapter_citation,
        link=subchapter_link,
        node_type="structure",
        level_type="subchapter",
        number=subchapter_num,
        node_name=subchapter_name,
        parent=parent_id,
        top_level_title=title_num,
        reserved=reserved
    )
    
    nodes.append(subchapter_node)
    
    # Process parts under subchapter
    for part in subchapter.find_all("PART", recursive=False):
        process_part(part, subchapter_components, subchapter_id, title_num, nodes)

def process_part(part, parent_components, parent_id, title_num, nodes):
    """Process a part element"""
    part_num = part.get("partnum", "")
    part_name = clean_text(part.get("heading", ""))
    
    # Check if reserved
    reserved = None
    for keyword in RESERVED_KEYWORDS:
        if keyword in part_name:
            reserved = "reserved"
            break
    
    # Create part components and ID
    part_components = parent_components + [("part", part_num)]
    part_id = create_hierarchical_id(part_components)
    part_citation = create_citation(part_components)
    part_link = create_link(part_components)
    
    part_node = Node(
        id=part_id,
        citation=part_citation,
        link=part_link,
        node_type="structure",
        level_type="part",
        number=part_num,
        node_name=part_name,
        parent=parent_id,
        top_level_title=title_num,
        reserved=reserved
    )
    
    nodes.append(part_node)
    
    # Process subparts if present
    for subpart in part.find_all("SUBPART", recursive=False):
        process_subpart(subpart, part_components, part_id, title_num, nodes)
    
    # Process sections directly under part
    for section in part.find_all("SECTION", recursive=False):
        process_section(section, part_components, part_id, title_num, nodes)

def process_subpart(subpart, parent_components, parent_id, title_num, nodes):
    """Process a subpart element"""
    subpart_num = subpart.get("subpartnum", "")
    subpart_name = clean_text(subpart.get("heading", ""))
    
    # Check if reserved
    reserved = None
    for keyword in RESERVED_KEYWORDS:
        if keyword in subpart_name:
            reserved = "reserved"
            break
    
    # Create subpart components and ID
    subpart_components = parent_components + [("subpart", subpart_num)]
    subpart_id = create_hierarchical_id(subpart_components)
    subpart_citation = create_citation(subpart_components)
    subpart_link = create_link(subpart_components)
    
    subpart_node = Node(
        id=subpart_id,
        citation=subpart_citation,
        link=subpart_link,
        node_type="structure",
        level_type="subpart",
        number=subpart_num,
        node_name=subpart_name,
        parent=parent_id,
        top_level_title=title_num,
        reserved=reserved
    )
    
    nodes.append(subpart_node)
    
    # Process sections under subpart
    for section in subpart.find_all("SECTION", recursive=False):
        process_section(section, subpart_components, subpart_id, title_num, nodes)

def process_section(section, parent_components, parent_id, title_num, nodes):
    """Process a section element"""
    section_num = section.get("sectnum", "")
    section_subject = clean_text(section.get("subject", ""))
    
    # Check if reserved
    reserved = None
    for keyword in RESERVED_KEYWORDS:
        if keyword in section_subject:
            reserved = "reserved"
            break
    
    # Create section components and ID
    section_components = parent_components + [("section", section_num)]
    section_id = create_hierarchical_id(section_components)
    section_citation = create_citation(section_components)
    section_link = create_link(section_components)
    
    # Extract section content
    content = None
    word_count = 0
    
    if reserved != "reserved":
        # Get all content from the section
        content_elements = section.find_all(["P", "FP"])
        content_texts = []
        
        for element in content_elements:
            text = clean_text(element.get_text())
            if text:
                content_texts.append(text)
        
        if content_texts:
            content = "\n\n".join(content_texts)
            word_count = len(content.split())
    
    # Create metadata with metrics
    metadata = {
        "word_count": word_count
    }
    
    section_node = Node(
        id=section_id,
        citation=section_citation,
        link=section_link,
        node_type="content",
        level_type="section",
        number=section_num,
        node_name=f"§ {section_num} {section_subject}",
        parent=parent_id,
        top_level_title=title_num,
        reserved=reserved,
        content=content,
        metadata=metadata
    )
    
    nodes.append(section_node)

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
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".xml"):
            xml_file_path = os.path.join(input_dir, filename)
            nodes = process_title_xml(xml_file_path)
            
            if nodes:
                # Write processed nodes to file for backup
                title_num = nodes[0].number if nodes else "unknown"
                output_file = os.path.join(PROCESSED_DATA_DIR, f"title-{title_num}-processed.txt")
                
                with open(output_file, "w", encoding="utf-8") as f:
                    for node in nodes:
                        f.write(f"{node.id}|{node.node_name}|{node.level_type}|{node.parent or 'None'}\n")
                
                # Insert nodes into database
                try:
                    insert_nodes(nodes)
                    print(f"Inserted {len(nodes)} nodes for {filename}")
                except Exception as e:
                    print(f"Error inserting nodes for {filename}: {e}")
                
                total_nodes += len(nodes)
    
    print(f"Processed {total_nodes} total nodes")
    return total_nodes

if __name__ == "__main__":
    ensure_directory_exists(PROCESSED_DATA_DIR)
    process_all_titles()