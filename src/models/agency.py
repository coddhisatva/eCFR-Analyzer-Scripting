#!/usr/bin/env python
"""
Agency model for regulatory agencies
"""
from typing import Optional, Dict, Any, List
from pydantic import BaseModel

class Agency(BaseModel):
    """
    Represents a regulatory agency in the system
    
    Attributes:
        id: Unique identifier (slug)
        name: Full agency name
        description: Agency description
        parent_id: Reference to parent agency
        depth: Hierarchy depth (0 for top-level)
        num_children: Number of child agencies
        num_words: Total word count across regulated content
        num_sections: Number of regulated sections
        num_cfr: Number of CFR references
        num_corrections: Number of corrections in regulated content
        cfr_references: List of CFR references
    """
    id: str
    name: str
    description: Optional[str] = None
    parent_id: Optional[str] = None
    depth: int = 0
    num_children: int = 0
    num_words: int = 0
    num_sections: int = 0
    num_cfr: int = 0
    num_corrections: int = 0
    cfr_references: List[str] = [] 