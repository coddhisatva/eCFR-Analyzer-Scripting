#!/usr/bin/env python
"""
Node model for CFR entities
"""
from dataclasses import dataclass
from typing import Optional, Dict, Any

@dataclass
class Node:
    """
    Represents a node in the CFR hierarchy
    """
    id: str  # Hierarchical ID (e.g., us/federal/ecfr/title=1/chapter=I/part=1)
    citation: str  # Formatted citation (e.g., "1 CFR Part 1")
    link: Optional[str] = None  # URL to the original content
    node_type: str = "structure"  # 'structure', 'content', or 'hub'
    level_type: str = None  # 'title', 'chapter', 'part', 'section', etc.
    number: str = None  # Identifier for this level
    node_name: str = None  # Display name
    parent: Optional[str] = None  # Parent node ID
    top_level_title: Optional[str] = None  # Title number this belongs to
    reserved: Optional[str] = None  # For 'reserved' sections
    content: Optional[str] = None  # Text content (for sections)
    metadata: Optional[Dict[str, Any]] = None  # Additional metadata