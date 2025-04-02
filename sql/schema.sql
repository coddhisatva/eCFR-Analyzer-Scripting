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
    top_level_title INTEGER,                -- Title number this belongs to
    depth INTEGER,                   
    display_order INTEGER,                   -- Order of the node in the title
    reserved TEXT,                          -- For 'reserved' sections
    metadata JSONB,
    num_corrections INTEGER DEFAULT 0                         -- Additional metadata (word counts, etc.)
);

-- Create the content_chunks table (for storing large content)
CREATE TABLE content_chunks (
    id TEXT PRIMARY KEY,                    -- Unique identifier for the chunk
    section_id TEXT REFERENCES nodes(id),   -- Reference to the parent section
    chunk_number INTEGER,                   -- Order of the chunk within the section
    content TEXT,                           -- The actual content text
    content_tsvector tsvector               -- Full-text search vector
);

-- Nodes

-- NAV TREE
-- for top level of tree:
CREATE INDEX nodes_depth0_title_idx ON nodes(top_level_title) 
WHERE depth = 0;
--- How to query it
SELECT * FROM nodes 
WHERE depth = 0 
ORDER BY top_level_title;
--top level, depth, just in case:
CREATE INDEX nodes_title_depth_idx ON nodes(top_level_title, depth);

-- This is how we do tree navigation on the homepage! Parent based index
CREATE INDEX nodes_parent_idx ON nodes(parent, display_order);
-- Get children in correct display order
SELECT * FROM nodes 
WHERE parent = 'parent_id'
ORDER BY display_order;


-- Content nodes for querying
CREATE INDEX nodes_node_type_content_idx ON nodes(node_type) WHERE node_type = 'content';
-- word count
CREATE INDEX nodes_metadata_word_count_idx ON nodes USING btree ((metadata->>'word_count'));

--CHUNKS
-- Primary search
CREATE INDEX IF NOT EXISTS content_chunks_tsvector_idx ON content_chunks USING gin(content_tsvector);
-- Section ID index: For finding all chunks of a section
CREATE INDEX IF NOT EXISTS content_chunks_section_id_idx ON content_chunks(section_id);
-- Combined index for finding specific chunks within a section
CREATE INDEX IF NOT EXISTS content_chunks_section_chunk_idx ON content_chunks(section_id, chunk_number);



---QUERYING---
-- Simple GIN index on content
CREATE INDEX content_chunks_content_gin_idx ON content_chunks USING gin (content);

-- GIN index on tsvector
CREATE INDEX content_chunks_content_tsvector_idx ON content_chunks USING gin (to_tsvector('english', content));



 CREATE INDEX nodes_number_idx ON nodes(number);

-- Index for citation searches
CREATE INDEX nodes_citation_idx ON nodes(citation);

-- Index for node name searches
CREATE INDEX nodes_name_idx ON nodes(node_name);