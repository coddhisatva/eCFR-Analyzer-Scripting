#!/usr/bin/env python
"""
Correction model for CFR corrections
"""
from dataclasses import dataclass
from typing import Optional, Dict, Any
from datetime import date

@dataclass
class Correction:
    """
    Represents a correction to CFR content
    
    Attributes:
        id: Unique identifier
        node_id: Reference to the corrected CFR node
        title: CFR title number
        corrective_action: Description of the correction
        error_corrected: Date the correction was made
        error_occurred: Date the error occurred
        correction_duration: Number of days between error and correction
        fr_citation: Federal Register citation
        position: Position in the document
        year: Year of the correction
    """
    id: int
    node_id: str
    title: int
    corrective_action: str
    error_corrected: date
    error_occurred: date
    correction_duration: Optional[int] = None
    fr_citation: Optional[str] = None
    position: Optional[int] = None
    year: Optional[int] = None 