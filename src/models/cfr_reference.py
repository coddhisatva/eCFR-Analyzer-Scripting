#!/usr/bin/env python
"""
CFR Reference model for agency-CFR relationships
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class CFRReference:
    """
    Represents a reference between an agency and a CFR section
    
    Attributes:
        id: Unique identifier
        agency_id: Reference to the agency
        title: CFR title number
        subheading: CFR subheading text
        is_primary: Whether this is the primary agency for this reference
        ordinal: Order of this reference
        node_id: Reference to the CFR node
    """
    id: int
    agency_id: str
    title: int
    subheading: Optional[str] = None
    is_primary: bool = True
    ordinal: Optional[int] = None
    node_id: Optional[str] = None 