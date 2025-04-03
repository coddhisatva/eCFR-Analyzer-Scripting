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
import json
import xml.etree.ElementTree as ET
from multiprocessing import Pool, cpu_count

from src.models.node import Node
from src.models.content_chunk import ContentChunk
from src.models.agency import Agency
from src.models.cfr_reference import CFRReference
from src.models.correction import Correction
from src.models.agency_node_mapping import AgencyNodeMapping
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
        self.agency_node_mappings: List[AgencyNodeMapping] = []
        
        # Indexes for faster lookups
        self.node_by_title: Dict[int, List[Node]] = defaultdict(list)
        self.node_by_parent: Dict[str, List[Node]] = defaultdict(list)
        self.agency_by_parent: Dict[str, List[Agency]] = defaultdict(list)
        self.mappings_by_agency: Dict[str, List[AgencyNodeMapping]] = defaultdict(list)
        self.mappings_by_node: Dict[str, List[AgencyNodeMapping]] = defaultdict(list)
        
        # Database client
        self.client = get_supabase_client()

    def validate_data(self) -> bool:
        """
        Validate all data before writing to database.
        Returns True if validation passes, False otherwise.
        """
        logger.info("Validating data...")
        
        # 1. Validate node hierarchy
        if not self._validate_node_hierarchy():
            return False
            
        # 2. Validate content chunks
        if not self._validate_content_chunks():
            return False
            
        # 3. Validate agency hierarchy
        if not self._validate_agency_hierarchy():
            return False
            
        # 4. Validate CFR references
        if not self._validate_cfr_references():
            return False
            
        # 5. Validate corrections
        if not self._validate_corrections():
            return False
            
        # 6. Validate agency-node mappings
        if not self._validate_agency_node_mappings():
            return False
            
        # 7. Validate metrics
        if not self._validate_metrics():
            return False
            
        logger.info("All validations passed!")
        return True

    def _validate_node_hierarchy(self) -> bool:
        """Validate node hierarchy structure"""
        # Check that all nodes have valid parents
        for node_id, node in self.nodes.items():
            if node.parent and node.parent not in self.nodes:
                logger.error(f"Node {node_id} has invalid parent {node.parent}")
                return False
                
        # Check that section counts are correct
        for node_id, node in self.nodes.items():
            if node.level_type == 'section' and node.num_sections != 1:
                logger.error(f"Section node {node_id} has incorrect section count: {node.num_sections}")
                return False
                
        # Validate node hierarchy structure
        for node_id, node in self.nodes.items():
            # Check that node appears in correct parent's children
            if node.parent:
                if node not in self.node_by_parent[node.parent]:
                    logger.error(f"Node {node_id} not found in parent {node.parent}'s children")
                    return False
                    
            # Check that all children have correct parent reference
            for child in self.node_by_parent[node_id]:
                if child.parent != node_id:
                    logger.error(f"Child node {child.id} has incorrect parent reference: {child.parent} != {node_id}")
                    return False
                    
        return True

    def _validate_content_chunks(self) -> bool:
        """Validate content chunks"""
        # Check that all chunks reference valid sections
        for chunk in self.content_chunks:
            if chunk.section_id not in self.nodes:
                logger.error(f"Content chunk references invalid section: {chunk.section_id}")
                return False
                
        return True

    def _validate_agency_hierarchy(self) -> bool:
        """Validate agency hierarchy"""
        # Check that all agencies have valid parents
        for agency_id, agency in self.agencies.items():
            if agency.parent_id and agency.parent_id not in self.agencies:
                logger.error(f"Agency {agency_id} has invalid parent {agency.parent_id}")
                return False
                
        # Validate agency hierarchy structure
        for agency_id, agency in self.agencies.items():
            # Check that agency appears in correct parent's children
            if agency.parent_id:
                if agency not in self.agency_by_parent[agency.parent_id]:
                    logger.error(f"Agency {agency_id} not found in parent {agency.parent_id}'s children")
                    return False
                    
            # Check that all children have correct parent reference
            for child in self.agency_by_parent[agency_id]:
                if child.parent_id != agency_id:
                    logger.error(f"Child agency {child.id} has incorrect parent reference: {child.parent_id} != {agency_id}")
                    return False
                    
        return True

    def _validate_cfr_references(self) -> bool:
        """Validate CFR references"""
        # Check that all references point to valid nodes and agencies
        for ref in self.cfr_references:
            if ref.node_id not in self.nodes:
                logger.error(f"CFR reference points to invalid node: {ref.node_id}")
                return False
            if ref.agency_id not in self.agencies:
                logger.error(f"CFR reference points to invalid agency: {ref.agency_id}")
                return False
                
        # Validate reference relationships
        for ref in self.cfr_references:
            node = self.nodes[ref.node_id]
            agency = self.agencies[ref.agency_id]
            
            # Check that node's title matches reference
            if node.top_level_title != ref.title:
                logger.error(f"CFR reference title mismatch: node={node.top_level_title}, ref={ref.title}")
                return False
                
            # Check that there's a corresponding agency-node mapping
            has_mapping = any(m.agency_id == ref.agency_id and m.node_id == ref.node_id 
                            for m in self.agency_node_mappings)
            if not has_mapping:
                logger.error(f"Missing agency-node mapping for CFR reference: agency={ref.agency_id}, node={ref.node_id}")
                return False
                
        return True

    def _validate_corrections(self) -> bool:
        """Validate corrections"""
        # Check that all corrections reference valid nodes and agencies
        for correction in self.corrections:
            if correction.node_id not in self.nodes:
                logger.error(f"Correction references invalid node: {correction.node_id}")
                return False
            if correction.agency_id not in self.agencies:
                logger.error(f"Correction references invalid agency: {correction.agency_id}")
                return False
                
        return True

    def _validate_agency_node_mappings(self) -> bool:
        """Validate agency-node mappings"""
        # Check that all mappings reference valid nodes and agencies
        for mapping in self.agency_node_mappings:
            if mapping.node_id not in self.nodes:
                logger.error(f"Agency-node mapping references invalid node: {mapping.node_id}")
                return False
            if mapping.agency_id not in self.agencies:
                logger.error(f"Agency-node mapping references invalid agency: {mapping.agency_id}")
                return False
                
        # Validate mapping indexes
        for agency_id, mappings in self.mappings_by_agency.items():
            for mapping in mappings:
                if mapping.agency_id != agency_id:
                    logger.error(f"Mapping {mapping.id} has incorrect agency_id in index: {mapping.agency_id} != {agency_id}")
                    return False
                    
        for node_id, mappings in self.mappings_by_node.items():
            for mapping in mappings:
                if mapping.node_id != node_id:
                    logger.error(f"Mapping {mapping.id} has incorrect node_id in index: {mapping.node_id} != {node_id}")
                    return False
                    
        return True

    def _validate_metrics(self) -> bool:
        """Validate all computed metrics"""
        # Validate agency metrics
        for agency_id, agency in self.agencies.items():
            # Get actual counts from references
            referenced_nodes = {ref.node_id for ref in self.cfr_references if ref.agency_id == agency_id}
            actual_sections = sum(self.nodes[node_id].num_sections or 0 for node_id in referenced_nodes if node_id in self.nodes)
            actual_words = sum(self.nodes[node_id].num_words or 0 for node_id in referenced_nodes if node_id in self.nodes)
            actual_corrections = sum(1 for corr in self.corrections if corr.agency_id == agency_id)
            
            # Calculate actual children count
            actual_children = len(self.agency_by_parent[agency_id])
            
            # Calculate actual CFR counts
            actual_cfr = len([ref for ref in self.cfr_references if ref.agency_id == agency_id])
            actual_cfr_refs = len([m for m in self.agency_node_mappings if m.agency_id == agency_id])
            
            # Compare with stored metrics
            if agency.num_sections != actual_sections:
                logger.error(f"Agency {agency_id} has incorrect section count: {agency.num_sections} != {actual_sections}")
                return False
            if agency.num_words != actual_words:
                logger.error(f"Agency {agency_id} has incorrect word count: {agency.num_words} != {actual_words}")
                return False
            if agency.num_corrections != actual_corrections:
                logger.error(f"Agency {agency_id} has incorrect correction count: {agency.num_corrections} != {actual_corrections}")
                return False
            if agency.num_children != actual_children:
                logger.error(f"Agency {agency_id} has incorrect children count: {agency.num_children} != {actual_children}")
                return False
            if agency.num_cfr != actual_cfr:
                logger.error(f"Agency {agency_id} has incorrect CFR count: {agency.num_cfr} != {actual_cfr}")
                return False
            if agency.num_cfr_refs != actual_cfr_refs:
                logger.error(f"Agency {agency_id} has incorrect CFR refs count: {agency.num_cfr_refs} != {actual_cfr_refs}")
                return False
                
        # Validate node correction counts
        for node_id, node in self.nodes.items():
            actual_corrections = sum(1 for corr in self.corrections if corr.node_id == node_id)
            if node.num_corrections != actual_corrections:
                logger.error(f"Node {node_id} has incorrect correction count: {node.num_corrections} != {actual_corrections}")
                return False
                
        return True

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
        
        # Validate node hierarchy after processing
        if not self._validate_node_hierarchy():
            logger.error(f"Invalid node hierarchy after processing {xml_file_path}")
            raise ValueError("Invalid node hierarchy")

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
        from src.data_processing.process_agencies import process_agency_data, process_cfr_references, process_agency_node_mappings
        
        # Get agency slug/id - handle missing slugs gracefully
        agency_slug = agency_data.get('slug')
        if not agency_slug:
            logger.warning(f"Skipping agency without slug: {agency_data.get('name', 'Unknown')}")
            return
        
        # Process agency hierarchy
        agencies = process_agency_data(agency_data)
        
        # Add agencies to our in-memory structures
        for agency in agencies:
            self.agencies[agency.id] = agency
            if agency.parent_id:
                self.agency_by_parent[agency.parent_id].append(agency)
        
        # Process CFR references
        references = process_cfr_references(agency_slug, agency_data.get('cfr_references', []))
        self.cfr_references.extend(references)
        
        # Process agency-node mappings
        mappings = process_agency_node_mappings(agency_slug, agency_data.get('cfr_references', []))
        for mapping in mappings:
            self.agency_node_mappings.append(mapping)
            self.mappings_by_agency[mapping.agency_id].append(mapping)
            self.mappings_by_node[mapping.node_id].append(mapping)
        
        # Calculate agency depths and counts
        self._calculate_agency_depths()
        self._calculate_agency_counts()
        
        # Update agency metrics based on references
        self._update_agency_metrics(agency_slug)
        
        # Validate agency hierarchy and relationships
        if not self._validate_agency_hierarchy():
            logger.error("Invalid agency hierarchy after processing")
            raise ValueError("Invalid agency hierarchy")
            
        if not self._validate_agency_node_mappings():
            logger.error("Invalid agency-node mappings after processing")
            raise ValueError("Invalid agency-node mappings")
            
        if not self._validate_cfr_references():
            logger.error("Invalid CFR references after processing")
            raise ValueError("Invalid CFR references")

    def _calculate_agency_depths(self) -> None:
        """Calculate depth for all agencies in the hierarchy"""
        def calculate_depth(agency_id: str, current_depth: int = 0) -> None:
            agency = self.agencies[agency_id]
            agency.depth = current_depth
            
            # Recursively calculate depth for children
            for child in self.agency_by_parent[agency_id]:
                calculate_depth(child.id, current_depth + 1)
        
        # Start with top-level agencies (those without parents)
        for agency_id, agency in self.agencies.items():
            if not agency.parent_id:
                calculate_depth(agency_id)

    def _calculate_agency_counts(self) -> None:
        """Calculate num_children and num_cfr for all agencies"""
        def calculate_counts(agency_id: str) -> Tuple[int, int, int]:
            agency = self.agencies[agency_id]
            
            # Count direct children
            num_children = len(self.agency_by_parent[agency_id])
            
            # Count direct CFR references (not accumulated from children)
            direct_cfr = len([ref for ref in self.cfr_references if ref.agency_id == agency_id])
            direct_cfr_refs = len([m for m in self.agency_node_mappings if m.agency_id == agency_id])
            
            # Add children counts from children (but not CFR refs)
            for child in self.agency_by_parent[agency_id]:
                child_children, _, _ = calculate_counts(child.id)
                num_children += child_children
            
            # Update agency counts
            agency.num_children = num_children
            agency.num_cfr = direct_cfr  # Only direct CFR references
            agency.num_cfr_refs = direct_cfr_refs  # Only direct CFR refs
            
            return num_children, direct_cfr, direct_cfr_refs
        
        # Start with top-level agencies
        for agency_id, agency in self.agencies.items():
            if not agency.parent_id:
                calculate_counts(agency_id)

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
        
        # Note: num_cfr and num_cfr_refs are now handled in _calculate_agency_counts()
        # which properly accumulates them up the hierarchy

    def process_correction(self, correction_data: Dict) -> None:
        """Process correction data and update related nodes and agencies"""
        from src.data_processing.process_corrections import build_node_id, parse_date
        
        # Create correction entity
        node_id = build_node_id(correction_data['hierarchy'])
        if not node_id or node_id not in self.nodes:
            logger.warning(f"Could not find matching node for correction: {correction_data}")
            return
        
        # Parse dates and calculate duration
        error_corrected = parse_date(correction_data.get('error_corrected', ''))
        error_occurred = parse_date(correction_data.get('error_occurred', ''))
        correction_duration = (error_corrected - error_occurred).days if error_corrected and error_occurred else None
        
        # Generate a unique ID using a hash of the node_id and index
        # This ensures uniqueness while being deterministic
        unique_id = abs(hash(f"correction:{node_id}:{len(self.corrections)}")) % (2**31)
        
        correction = Correction(
            id=unique_id,
            node_id=node_id,
            agency_id=correction_data['agency_id'],
            title=correction_data['title'],
            corrective_action=correction_data['corrective_action'],
            error_corrected=error_corrected,
            error_occurred=error_occurred,
            correction_duration=correction_duration,
            fr_citation=correction_data.get('fr_citation'),
            position=correction_data.get('position'),
            year=correction_data.get('year'),
            metadata={
                'cfr_reference': correction_data.get('cfr_reference', ''),
                'last_modified': correction_data.get('last_modified'),
                'display_in_toc': correction_data.get('display_in_toc'),
                'last_updated': datetime.now().isoformat()
            }
        )
        
        self.corrections.append(correction)
        
        # Update node's correction count
        if node_id in self.nodes:
            self.nodes[node_id].num_corrections = (self.nodes[node_id].num_corrections or 0) + 1
        
        # Update agency's correction count
        if correction_data['agency_id'] in self.agencies:
            self.agencies[correction_data['agency_id']].num_corrections += 1

    def _save_backup(self, backup_dir: str = "data/processed_backup") -> None:
        """Save all processed data to CSV files as backup"""
        import pandas as pd
        import os
        from datetime import datetime

        # Create backup directory with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(backup_dir, timestamp)
        os.makedirs(backup_path, exist_ok=True)
        
        logger.info(f"Saving backup to {backup_path}")
        
        try:
            # Save nodes
            nodes_df = pd.DataFrame([node.__dict__ for node in self.nodes.values()])
            nodes_df.to_csv(os.path.join(backup_path, "nodes.csv"), index=False)
            
            # Save content chunks
            chunks_df = pd.DataFrame([chunk.__dict__ for chunk in self.content_chunks])
            chunks_df.to_csv(os.path.join(backup_path, "content_chunks.csv"), index=False)
            
            # Save agencies
            agencies_df = pd.DataFrame([agency.__dict__ for agency in self.agencies.values()])
            agencies_df.to_csv(os.path.join(backup_path, "agencies.csv"), index=False)
            
            # Save CFR references
            refs_df = pd.DataFrame([ref.__dict__ for ref in self.cfr_references])
            refs_df.to_csv(os.path.join(backup_path, "cfr_references.csv"), index=False)
            
            # Save corrections
            corrections_df = pd.DataFrame([corr.__dict__ for corr in self.corrections])
            corrections_df.to_csv(os.path.join(backup_path, "corrections.csv"), index=False)
            
            # Save agency-node mappings
            mappings_df = pd.DataFrame([mapping.__dict__ for mapping in self.agency_node_mappings])
            mappings_df.to_csv(os.path.join(backup_path, "agency_node_mappings.csv"), index=False)
            
            # Save a metadata file with processing info
            with open(os.path.join(backup_path, "metadata.json"), "w") as f:
                import json
                json.dump({
                    "timestamp": timestamp,
                    "stats": {
                        "nodes": len(self.nodes),
                        "content_chunks": len(self.content_chunks),
                        "agencies": len(self.agencies),
                        "cfr_references": len(self.cfr_references),
                        "corrections": len(self.corrections),
                        "agency_node_mappings": len(self.agency_node_mappings)
                    }
                }, f, indent=2)
            
            logger.info("Successfully saved backup of all processed data")
            return backup_path
        except Exception as e:
            logger.error(f"Error saving backup: {e}")
            raise

    def _load_backup(self, backup_path: str) -> None:
        """Load processed data from CSV backup"""
        import pandas as pd
        from src.models.node import Node
        from src.models.content_chunk import ContentChunk
        from src.models.agency import Agency
        from src.models.cfr_reference import CFRReference
        from src.models.correction import Correction
        from src.models.agency_node_mapping import AgencyNodeMapping
        
        logger.info(f"Loading backup from {backup_path}")
        
        try:
            # Load nodes
            nodes_df = pd.read_csv(os.path.join(backup_path, "nodes.csv"))
            self.nodes = {row['id']: Node(**row) for _, row in nodes_df.iterrows()}
            
            # Load content chunks
            chunks_df = pd.read_csv(os.path.join(backup_path, "content_chunks.csv"))
            self.content_chunks = [ContentChunk(**row) for _, row in chunks_df.iterrows()]
            
            # Load agencies
            agencies_df = pd.read_csv(os.path.join(backup_path, "agencies.csv"))
            self.agencies = {row['id']: Agency(**row) for _, row in agencies_df.iterrows()}
            
            # Load CFR references
            refs_df = pd.read_csv(os.path.join(backup_path, "cfr_references.csv"))
            self.cfr_references = [CFRReference(**row) for _, row in refs_df.iterrows()]
            
            # Load corrections
            corrections_df = pd.read_csv(os.path.join(backup_path, "corrections.csv"))
            self.corrections = [Correction(**row) for _, row in corrections_df.iterrows()]
            
            # Load agency-node mappings
            mappings_df = pd.read_csv(os.path.join(backup_path, "agency_node_mappings.csv"))
            self.agency_node_mappings = [AgencyNodeMapping(**row) for _, row in mappings_df.iterrows()]
            
            # Rebuild indexes
            self._rebuild_indexes()
            
            logger.info("Successfully loaded backup data")
        except Exception as e:
            logger.error(f"Error loading backup: {e}")
            raise

    def _rebuild_indexes(self) -> None:
        """Rebuild all indexes after loading from backup"""
        # Clear existing indexes
        self.node_by_title = defaultdict(list)
        self.node_by_parent = defaultdict(list)
        self.agency_by_parent = defaultdict(list)
        self.mappings_by_agency = defaultdict(list)
        self.mappings_by_node = defaultdict(list)
        
        # Rebuild node indexes
        for node in self.nodes.values():
            self.node_by_title[node.top_level_title].append(node)
            if node.parent:
                self.node_by_parent[node.parent].append(node)
        
        # Rebuild agency indexes
        for agency in self.agencies.values():
            if agency.parent_id:
                self.agency_by_parent[agency.parent_id].append(agency)
        
        # Rebuild mapping indexes
        for mapping in self.agency_node_mappings:
            self.mappings_by_agency[mapping.agency_id].append(mapping)
            self.mappings_by_node[mapping.node_id].append(mapping)

    def write_to_database(self) -> None:
        """Write all processed data to the database"""
        logger.info("Writing processed data to database...")
        
        # Validate data before writing
        if not self.validate_data():
            logger.error("Data validation failed. Aborting database write.")
            return
            
        # Save backup before attempting database write
        try:
            backup_path = self._save_backup()
            logger.info(f"Backup saved to {backup_path}")
        except Exception as e:
            logger.error(f"Failed to save backup: {e}")
            user_input = input("Failed to save backup. Continue with database write anyway? (y/n): ")
            if user_input.lower() != 'y':
                logger.info("Aborting database write")
                return
        
        try:
            # Clear existing data
            self.client.table('nodes').delete().execute()
            self.client.table('content_chunks').delete().execute()
            self.client.table('agencies').delete().execute()
            self.client.table('cfr_references').delete().execute()
            self.client.table('corrections').delete().execute()
            self.client.table('agency_node_mappings').delete().execute()
            
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
            
            # Write agency-node mappings
            mappings_data = [mapping.__dict__ for mapping in self.agency_node_mappings]
            self.client.table('agency_node_mappings').upsert(mappings_data).execute()
            logger.info(f"Wrote {len(mappings_data)} agency-node mappings")
            
        except Exception as e:
            logger.error(f"Database write failed: {e}")
            logger.info(f"Data is safely backed up at: {backup_path}")
            logger.info("You can use the backup to retry the database write later")

    def _process_node_tree_unified(self, node_id: str, parent_metrics: Dict = None) -> Dict:
        """
        Single unified pass through the node tree to calculate all metrics at once.
        Returns a dict with all computed metrics for this subtree.
        """
        node = self.nodes[node_id]
        metrics = {
            'num_sections': 0,
            'num_words': node.num_words or 0,  # Base word count for this node
            'num_corrections': node.num_corrections or 0,  # Base corrections for this node
            'agencies': set(),  # Track agencies for this subtree
            'depth': (parent_metrics['depth'] + 1) if parent_metrics else 0
        }
        
        # If this is a section, count it
        if node.level_type == 'section':
            metrics['num_sections'] = 1
        
        # Process all children in one pass
        for child in self.node_by_parent[node_id]:
            child_metrics = self._process_node_tree_unified(child.id, metrics)
            # Aggregate metrics from child
            metrics['num_sections'] += child_metrics['num_sections']
            metrics['num_words'] += child_metrics['num_words']
            metrics['num_corrections'] += child_metrics['num_corrections']
            metrics['agencies'].update(child_metrics['agencies'])
        
        # Update node with computed metrics
        node.num_sections = metrics['num_sections']
        node.num_words = metrics['num_words']
        node.num_corrections = metrics['num_corrections']
        
        # Process agency relationships for this node
        for mapping in self.mappings_by_node.get(node_id, []):
            metrics['agencies'].add(mapping.agency_id)
            agency = self.agencies[mapping.agency_id]
            # Update agency metrics in one go
            agency.num_sections = metrics['num_sections']
            agency.num_words = metrics['num_words']
            agency.num_corrections = metrics['num_corrections']
            agency.depth = metrics['depth']
        
        return metrics

    def process_title_parallel(self, file_path: str) -> Tuple[Dict, List, List]:
        """Process a single title file, returning its nodes and content chunks"""
        from multiprocessing import current_process
        logger.info(f"Process {current_process().name}: Starting {file_path}")
        
        title_nodes = {}
        title_chunks = []
        title_mappings = []
        
        try:
            # Process the XML file
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            # Extract title number
            title_num = int(os.path.basename(file_path).split('-')[1].split('.')[0])
            
            # Process the title structure
            for div in root.findall('.//DIV1'):
                nodes, chunks, mappings = self._process_div(div, title_num)
                title_nodes.update(nodes)
                title_chunks.extend(chunks)
                title_mappings.extend(mappings)
            
            logger.info(f"Process {current_process().name}: Finished {file_path} - {len(title_nodes)} nodes, {len(title_chunks)} chunks")
            return title_nodes, title_chunks, title_mappings
            
        except Exception as e:
            logger.error(f"Error processing {file_path}: {e}")
            return {}, [], []

    def process_all_data(self, args):
        """Process all data from raw files into database entities"""
        from multiprocessing import Pool, cpu_count
        
        logger.info("Starting data processing...")
        
        # Process titles in parallel
        title_dir = os.path.join("data", "raw", "titles", args.date)
        title_files = sorted([os.path.join(title_dir, f) for f in os.listdir(title_dir) if f.endswith(".xml")])
        
        # Use number of CPU cores for parallel processing
        num_processes = min(cpu_count(), len(title_files))
        logger.info(f"Processing {len(title_files)} titles using {num_processes} processes")
        
        with Pool(num_processes) as pool:
            # Process titles in parallel and collect results
            results = pool.map(self.process_title_parallel, title_files)
            
            # Combine results from all processes
            for nodes, chunks, mappings in results:
                self.nodes.update(nodes)
                self.content_chunks.extend(chunks)
                self.node_mappings.extend(mappings)
        
        logger.info(f"Finished processing all titles. Found {len(self.nodes)} nodes and {len(self.content_chunks)} chunks")
        
        # Build node relationships
        self._build_node_relationships()
        
        # Single unified pass to calculate all metrics
        logger.info("Calculating all metrics in unified pass...")
        root_nodes = [node_id for node_id, node in self.nodes.items() if not node.parent]
        for root_id in root_nodes:
            self._process_node_tree_unified(root_id)
        
        # Process agency data
        logger.info("Processing agency data")
        agency_dir = os.path.join("data", "raw", "agencies", args.date)
        agency_file = os.path.join(agency_dir, "agencies.json")
        
        try:
            with open(agency_file, 'r', encoding='utf-8') as f:
                agency_data = json.load(f)
            
            # Process each agency
            for agency in agency_data.get('agencies', []):
                try:
                    self.process_agency(agency)
                except Exception as e:
                    logger.error(f"Error processing agency {agency.get('name', 'Unknown')}: {e}")
                    continue
        except Exception as e:
            logger.error(f"Error reading agency file {agency_file}: {e}")
            logger.warning("Skipping agency processing due to error")
        
        # Process corrections
        logger.info("Processing corrections")
        corrections_dir = os.path.join("data", "raw", "corrections", args.date)
        try:
            for filename in os.listdir(corrections_dir):
                if not filename.endswith(".json"):
                    continue
                file_path = os.path.join(corrections_dir, filename)
                try:
                    self.process_correction_file(file_path)
                except Exception as e:
                    logger.error(f"Error processing correction file {filename}: {e}")
                    continue
        except Exception as e:
            logger.error(f"Error reading corrections directory {corrections_dir}: {e}")
            logger.warning("Skipping corrections processing due to error")
        
        # Save backup before database write
        backup_path = self._save_backup()
        logger.info(f"Backup saved to {backup_path}")
        
        # Write to database
        logger.info("Writing to database...")
        try:
            self._write_to_database()
            logger.info("Successfully wrote all data to database")
        except Exception as e:
            logger.error(f"Database write failed: {e}")
            logger.info(f"Data is safely backed up at: {backup_path}")
            logger.info("You can use the backup to retry the database write later")

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