#!/usr/bin/env python
"""
Agency Node Mapping model for agency-node relationships
"""
from dataclasses import dataclass
from typing import Optional, Dict, Any

@dataclass
class AgencyNodeMapping:
    """
    Represents a mapping between an agency and a CFR node
    
    Attributes:
        id: Unique identifier
        agency_id: Reference to the agency
        node_id: Reference to the CFR node
        is_primary: Whether this is the primary agency for this node
        is_direct_reference: Whether this is a direct CFR reference vs. inherited
        relationship_type: Type of relationship (regulatory, advisory, etc.)
        metadata: Additional information about the relationship
        num_cfr_refs: Number of CFR references for this relationship
    """
    id: int
    agency_id: str
    node_id: str
    is_primary: bool = False
    is_direct_reference: bool = False
    relationship_type: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    num_cfr_refs: int = 0 