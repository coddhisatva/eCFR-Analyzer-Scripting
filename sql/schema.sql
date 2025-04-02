-- eCFR Database Schema
-- This file contains the complete database schema for the eCFR Analyzer

-- Drop existing tables and indexes if they exist
DROP TABLE IF EXISTS content_chunks CASCADE;
DROP TABLE IF EXISTS nodes CASCADE;

-- Create the nodes table (structural hierarchy)
CREATE TABLE nodes (
    id TEXT PRIMARY KEY,                    -- Hierarchical ID (e.g., us/federal/ecfr/title=1/chapter=I/part=1)
    citation TEXT,                          -- Formatted citation (e.g., "1 CFR Part 1")
    link TEXT,                              -- URL to the original content
    node_type TEXT,                         -- 'structure' or 'content'
    level_type TEXT,                        -- 'title', 'chapter', 'part', 'section', etc.
    number TEXT,                            -- Identifier for this level
    node_name TEXT,                         -- Display name
    parent TEXT,                            -- Parent node ID
    top_level_title INTEGER,                   -- Title number this belongs to
    reserved TEXT,                          -- For 'reserved' sections
    metadata JSONB                          -- Additional metadata (word counts, etc.)
);

-- Create the content_chunks table (for storing large content)
CREATE TABLE content_chunks (
    id TEXT PRIMARY KEY,                    -- Unique identifier for the chunk
    section_id TEXT REFERENCES nodes(id),   -- Reference to the parent section
    chunk_number INTEGER,                   -- Order of the chunk within the section
    content TEXT,                           -- The actual content text
    content_tsvector tsvector               -- Full-text search vector
);

-- Indexes for nodes table
-- Title index: Used when finding all nodes in a specific title
CREATE INDEX IF NOT EXISTS nodes_top_level_title_idx ON nodes(top_level_title);

-- Parent index: Critical for building the tree structure
CREATE INDEX IF NOT EXISTS nodes_parent_idx ON nodes(parent);

-- Level type index: Used when finding all nodes of a specific type
CREATE INDEX IF NOT EXISTS nodes_level_type_idx ON nodes(level_type);

-- Citation index: Used for searching and filtering by citation
CREATE INDEX IF NOT EXISTS nodes_citation_idx ON nodes(citation);

-- Word count index: Used for analytics on section lengths
CREATE INDEX IF NOT EXISTS nodes_word_count_idx ON nodes USING gin ((metadata->>'word_count'));

-- Node type index: Used for filtering structure vs content nodes
CREATE INDEX IF NOT EXISTS nodes_node_type_idx ON nodes(node_type);

-- Combined index for title and level navigation
CREATE INDEX IF NOT EXISTS nodes_title_level_idx ON nodes(top_level_title, level_type);

-- Reserved sections index
CREATE INDEX IF NOT EXISTS nodes_reserved_idx ON nodes(reserved);

-- Indexes for content_chunks table
-- Section ID index: For finding all chunks of a section
CREATE INDEX IF NOT EXISTS content_chunks_section_id_idx ON content_chunks(section_id);

-- Full-text search index on content
CREATE INDEX IF NOT EXISTS content_chunks_tsvector_idx ON content_chunks USING gin(content_tsvector);

-- Chunk number index: For finding specific chunks by number
CREATE INDEX IF NOT EXISTS content_chunks_chunk_number_idx ON content_chunks(chunk_number);

-- Combined index for finding specific chunks within a section
CREATE INDEX IF NOT EXISTS content_chunks_section_chunk_idx ON content_chunks(section_id, chunk_number); 