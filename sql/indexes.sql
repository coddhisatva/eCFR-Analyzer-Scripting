-- Drop existing indexes if they exist
DROP INDEX IF EXISTS nodes_top_level_title_idx;
DROP INDEX IF EXISTS nodes_parent_idx;
DROP INDEX IF EXISTS nodes_level_type_idx;
DROP INDEX IF EXISTS nodes_citation_idx;
DROP INDEX IF EXISTS nodes_word_count_idx;
DROP INDEX IF EXISTS nodes_node_type_idx;
DROP INDEX IF EXISTS nodes_title_level_idx;
DROP INDEX IF EXISTS nodes_reserved_idx;
DROP INDEX IF EXISTS content_chunks_section_id_idx;
DROP INDEX IF EXISTS content_chunks_tsvector_idx;
DROP INDEX IF EXISTS content_chunks_chunk_number_idx;
DROP INDEX IF EXISTS content_chunks_section_chunk_idx;

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
CREATE INDEX IF NOT EXISTS nodes_word_count_idx ON nodes USING btree ((metadata->>'word_count'));

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