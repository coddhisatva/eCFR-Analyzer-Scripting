#!/usr/bin/env python
"""
Agency model for regulatory agencies
"""
from typing import Optional, Dict, Any, List
from dataclasses import dataclass

@dataclass
class Agency:
    """
    Represents a regulatory agency in the system
    
    Attributes:
        id: Unique identifier (slug)
        name: Full agency name
        short_name: Short agency name
        display_name: Display name for the agency
        sortable_name: Name used for sorting
        parent_id: Reference to parent agency
        depth: Hierarchy depth (0 for top-level)
        agency_type: Type of agency (root, middle, zed)
        metadata: Additional agency metadata
        num_children: Number of child agencies
        num_words: Total word count across regulated content
        num_sections: Number of regulated sections
        num_cfr: Number of CFR references
        num_corrections: Number of corrections in regulated content
        cfr_references: List of CFR references
    """
    id: str
    name: str
    short_name: Optional[str] = None
    display_name: Optional[str] = None
    sortable_name: Optional[str] = None
    parent_id: Optional[str] = None
    depth: int = 0
    agency_type: str = "zed"
    metadata: Optional[Dict[str, Any]] = None
    num_children: int = 0
    num_words: int = 0
    num_sections: int = 0
    num_cfr: int = 0
    num_corrections: int = 0
    cfr_references: List[str] = None
    
    def __post_init__(self):
        if self.cfr_references is None:
            self.cfr_references = []
        if self.metadata is None:
            self.metadata = {} 