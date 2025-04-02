#!/usr/bin/env python
"""
Agency model for regulatory agencies
"""
from dataclasses import dataclass
from typing import Optional, Dict, Any

@dataclass
class Agency:
    """
    Represents a regulatory agency in the system
    
    Attributes:
        id: Unique identifier (slug)
        name: Full agency name
        short_name: Abbreviated name
        display_name: Formatted name for display
        sortable_name: Name formatted for sorting
        parent_id: Reference to parent agency
        depth: Hierarchy depth (0 for top-level)
        agency_type: Type of agency ('beg', 'middle', 'zed')
        metadata: Additional flexible data
        num_children: Number of child agencies
        num_words: Total word count across regulated content
        num_sections: Number of regulated sections
        num_corrections: Number of corrections in regulated content
        num_cfr_refs: Number of CFR references for this agency
    """
    id: str
    name: str
    short_name: Optional[str] = None
    display_name: Optional[str] = None
    sortable_name: Optional[str] = None
    parent_id: Optional[str] = None
    depth: int = 0
    agency_type: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    num_children: int = 0
    num_words: int = 0
    num_sections: int = 0
    num_corrections: int = 0
    num_cfr_refs: int = 0 