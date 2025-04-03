-- Functions for bulk inserting nodes and content chunks
-- This file contains functions for efficient bulk insertion of data

-- Function to bulk insert nodes
CREATE OR REPLACE FUNCTION bulk_insert_nodes(nodes_json JSONB)
RETURNS void AS $$
BEGIN
    -- Delete existing nodes for the titles in the batch
    DELETE FROM nodes
    WHERE id IN (
        SELECT (jsonb_array_elements(nodes_json)->>'id')::text
    );
    
    -- Insert new nodes
    INSERT INTO nodes (
        id, citation, link, node_type, level_type, number, 
        node_name, parent, top_level_title, depth, display_order,
        reserved, metadata, num_corrections, num_sections, num_words
    )
    SELECT
        (node->>'id')::text,
        (node->>'citation')::text,
        (node->>'link')::text,
        (node->>'node_type')::text,
        (node->>'level_type')::text,
        (node->>'number')::text,
        (node->>'node_name')::text,
        (node->>'parent')::text,
        (node->>'top_level_title')::integer,
        (node->>'depth')::integer,
        (node->>'display_order')::integer,
        (node->>'reserved')::text,
        (node->'metadata')::jsonb,
        (node->>'num_corrections')::integer,
        (node->>'num_sections')::integer,
        (node->>'num_words')::integer
    FROM jsonb_array_elements(nodes_json) AS node;
END;
$$ LANGUAGE plpgsql;

-- Function to bulk insert content chunks
CREATE OR REPLACE FUNCTION bulk_insert_content_chunks(chunks_json JSONB)
RETURNS void AS $$
BEGIN
    -- Delete existing chunks for the sections in the batch
    DELETE FROM content_chunks
    WHERE section_id IN (
        SELECT DISTINCT (jsonb_array_elements(chunks_json)->>'section_id')::text
    );
    
    -- Insert new chunks
    INSERT INTO content_chunks (
        id, section_id, chunk_number, content
    )
    SELECT
        (chunk->>'id')::text,
        (chunk->>'section_id')::text,
        (chunk->>'chunk_number')::integer,
        (chunk->>'content')::text
    FROM jsonb_array_elements(chunks_json) AS chunk;
END;
$$ LANGUAGE plpgsql; 