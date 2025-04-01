#!/usr/bin/env python
"""
Content chunk model for storing large text sections
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class ContentChunk:
    """
    Represents a chunk of content from a section
    """
    id: str  # Unique ID for the chunk
    section_id: str  # Reference to parent node
    chunk_number: int  # Order of the chunk
    content: str  # The actual text content
    content_tsvector: Optional[str] = None  # PostgreSQL tsvector for search

    def __post_init__(self):
        """Validate chunk ID format"""
        if not self.id.startswith(self.section_id):
            raise ValueError(f"Chunk ID {self.id} must start with section_id {self.section_id}")
        if not self.id.endswith(f"_chunk_{self.chunk_number}"):
            raise ValueError(f"Chunk ID {self.id} must end with _chunk_{self.chunk_number}") 