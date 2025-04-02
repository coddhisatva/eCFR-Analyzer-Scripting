#!/usr/bin/env python
"""
Unified processor for eCFR data that handles all processing in memory
before writing to the database.
"""
import os
import logging
from datetime import datetime
from typing import Dict, List, Optional, Set, Tuple
from collections import defaultdict

from src.models.node import Node
from src.models.content_chunk import ContentChunk
from src.models.agency import Agency
from src.models.cfr_reference import CFRReference
from src.models.correction import Correction
from src.database.connector import get_supabase_client

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UnifiedProcessor:
    def __init__(self):
        # In-memory data structures
        self.nodes: Dict[str, Node] = {}  # id -> Node
        self.content_chunks: List[ContentChunk] = []
        self.agencies: Dict[str, Agency] = {}  # id -> Agency
        self.cfr_references: List[CFRReference] = []
        self.corrections: List[Correction] = []
        
        # Indexes for faster lookups
        self.node_by_title: Dict[int, List[Node]] = defaultdict(list)
        self.node_by_parent: Dict[str, List[Node]] = defaultdict(list)
        self.agency_by_parent: Dict[str, List[Agency]] = defaultdict(list)
        
        # Database client
        self.client = get_supabase_client()

    def process_title(self, xml_file_path: str) -> None:
        """Process a title XML file and build the node hierarchy in memory"""
        from src.data_processing.process_xml import process_title_xml
        
        nodes, chunks = process_title_xml(xml_file_path)
        
        # Add nodes and chunks to our in-memory structures
        for node in nodes:
            self.nodes[node.id] = node
            self.node_by_title[node.top_level_title].append(node)
            if node.parent:
                self.node_by_parent[node.parent].append(node)
        
        self.content_chunks.extend(chunks)
        
        # Calculate section counts for this title's hierarchy
        self._calculate_section_counts(nodes[0].id)  # Start from root node

    def _calculate_section_counts(self, node_id: str) -> int:
        """Calculate section counts recursively for a node and its children"""
        node = self.nodes[node_id]
        
        # If this is a section node, it has 1 section
        if node.level_type == 'section':
            node.num_sections = 1
            return 1
        
        # For non-section nodes, sum their children's sections
        total_sections = 0
        for child in self.node_by_parent[node_id]:
            total_sections += self._calculate_section_counts(child.id)
        
        node.num_sections = total_sections
        return total_sections

    def process_agency(self, agency_data: Dict) -> None:
        """Process agency data and build relationships in memory"""
        from src.data_processing.process_agencies import process_agency_data, process_cfr_references
        
        # Process agency hierarchy
        agencies = process_agency_data(agency_data)
        
        # Add agencies to our in-memory structures
        for agency in agencies:
            self.agencies[agency.id] = agency
            if agency.parent_id:
                self.agency_by_parent[agency.parent_id].append(agency)
        
        # Process CFR references
        references = process_cfr_references(agency_data['slug'], agency_data.get('cfr_references', []))
        self.cfr_references.extend(references)
        
        # Update agency metrics based on references
        self._update_agency_metrics(agency_data['slug'])

    def _update_agency_metrics(self, agency_id: str) -> None:
        """Update agency metrics based on its CFR references"""
        agency = self.agencies[agency_id]
        
        # Get all nodes this agency references
        referenced_nodes = {ref.node_id for ref in self.cfr_references if ref.agency_id == agency_id}
        
        # Calculate metrics
        total_sections = 0
        total_words = 0
        total_corrections = 0
        
        for node_id in referenced_nodes:
            if node_id in self.nodes:
                node = self.nodes[node_id]
                total_sections += node.num_sections or 0
                total_words += node.num_words or 0
                total_corrections += node.num_corrections or 0
        
        # Update agency metrics
        agency.num_sections = total_sections
        agency.num_words = total_words
        agency.num_corrections = total_corrections

    def process_correction(self, correction_data: Dict) -> None:
        """Process correction data and update related nodes and agencies"""
        from src.data_processing.process_corrections import build_node_id
        
        # Create correction entity
        node_id = build_node_id(correction_data['hierarchy'])
        if not node_id or node_id not in self.nodes:
            logger.warning(f"Could not find matching node for correction: {correction_data}")
            return
        
        correction = Correction(
            node_id=node_id,
            agency_id=correction_data['agency_id'],
            title=correction_data['title'],
            corrective_action=correction_data['corrective_action'],
            error_corrected=correction_data['error_corrected'],
            error_occurred=correction_data['error_occurred'],
            correction_duration=correction_data.get('correction_duration'),
            fr_citation=correction_data.get('fr_citation'),
            position=correction_data.get('position'),
            year=correction_data.get('year'),
            metadata=correction_data.get('metadata', {})
        )
        
        self.corrections.append(correction)
        
        # Update node's correction count
        if node_id in self.nodes:
            self.nodes[node_id].num_corrections = (self.nodes[node_id].num_corrections or 0) + 1
        
        # Update agency's correction count
        if correction_data['agency_id'] in self.agencies:
            self.agencies[correction_data['agency_id']].num_corrections += 1

    def write_to_database(self) -> None:
        """Write all processed data to the database"""
        logger.info("Writing processed data to database...")
        
        # Clear existing data
        self.client.table('nodes').delete().execute()
        self.client.table('content_chunks').delete().execute()
        self.client.table('agencies').delete().execute()
        self.client.table('cfr_references').delete().execute()
        self.client.table('corrections').delete().execute()
        
        # Write nodes
        nodes_data = [node.__dict__ for node in self.nodes.values()]
        self.client.table('nodes').upsert(nodes_data).execute()
        logger.info(f"Wrote {len(nodes_data)} nodes")
        
        # Write content chunks
        chunks_data = [chunk.__dict__ for chunk in self.content_chunks]
        self.client.table('content_chunks').upsert(chunks_data).execute()
        logger.info(f"Wrote {len(chunks_data)} content chunks")
        
        # Write agencies
        agencies_data = [agency.__dict__ for agency in self.agencies.values()]
        self.client.table('agencies').upsert(agencies_data).execute()
        logger.info(f"Wrote {len(agencies_data)} agencies")
        
        # Write CFR references
        refs_data = [ref.__dict__ for ref in self.cfr_references]
        self.client.table('cfr_references').upsert(refs_data).execute()
        logger.info(f"Wrote {len(refs_data)} CFR references")
        
        # Write corrections
        corrections_data = [corr.__dict__ for corr in self.corrections]
        self.client.table('corrections').upsert(corrections_data).execute()
        logger.info(f"Wrote {len(corrections_data)} corrections")

def process_all_data(date: str) -> None:
    """Process all data for a given date using the unified processor"""
    processor = UnifiedProcessor()
    
    # Process titles
    input_dir = os.path.join("data", "raw", "titles", date)
    for filename in os.listdir(input_dir):
        if filename.endswith(".xml") and filename.startswith("title-"):
            file_path = os.path.join(input_dir, filename)
            logger.info(f"Processing title file: {filename}")
            processor.process_title(file_path)
    
    # Process agencies
    agency_file = os.path.join("data", "raw", "agencies", date, "agencies.json")
    if os.path.exists(agency_file):
        import json
        with open(agency_file, 'r') as f:
            agency_data = json.load(f)
        logger.info("Processing agency data")
        processor.process_agency(agency_data)
    
    # Process corrections
    corrections_file = os.path.join("data", "raw", "corrections", date, "corrections.json")
    if os.path.exists(corrections_file):
        import json
        with open(corrections_file, 'r') as f:
            corrections_data = json.load(f)
        logger.info("Processing corrections data")
        for correction in corrections_data:
            processor.process_correction(correction)
    
    # Write everything to the database
    processor.write_to_database()
    logger.info("Finished processing all data")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Process eCFR data using unified processor")
    parser.add_argument("--date", type=str, required=True, help="Date to process (YYYY-MM-DD)")
    args = parser.parse_args()
    
    process_all_data(args.date) 