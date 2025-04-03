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

-- Function to bulk insert agencies
CREATE OR REPLACE FUNCTION bulk_insert_agencies(agencies_json JSONB)
RETURNS void AS $$
BEGIN
    -- Delete existing agencies
    DELETE FROM agencies;
    
    -- Insert new agencies
    INSERT INTO agencies (
        id, name, abbreviation, parent_id
    )
    SELECT
        (agency->>'id')::text,
        (agency->>'name')::text,
        (agency->>'abbreviation')::text,
        (agency->>'parent_id')::text
    FROM jsonb_array_elements(agencies_json) AS agency;
END;
$$ LANGUAGE plpgsql;

-- Function to bulk insert CFR references
CREATE OR REPLACE FUNCTION bulk_insert_cfr_references(refs_json JSONB)
RETURNS void AS $$
BEGIN
    -- Delete existing references
    DELETE FROM cfr_references;
    
    -- Insert new references
    INSERT INTO cfr_references (
        id, source_node, target_node, reference_type, context
    )
    SELECT
        (ref->>'id')::text,
        (ref->>'source_node')::text,
        (ref->>'target_node')::text,
        (ref->>'reference_type')::text,
        (ref->>'context')::text
    FROM jsonb_array_elements(refs_json) AS ref;
END;
$$ LANGUAGE plpgsql;

-- Function to bulk insert agency node mappings
CREATE OR REPLACE FUNCTION bulk_insert_agency_node_mappings(mappings_json JSONB)
RETURNS void AS $$
BEGIN
    -- Delete existing mappings
    DELETE FROM agency_node_mappings;
    
    -- Insert new mappings
    INSERT INTO agency_node_mappings (
        id, agency_id, node_id, mapping_type
    )
    SELECT
        (mapping->>'id')::text,
        (mapping->>'agency_id')::text,
        (mapping->>'node_id')::text,
        (mapping->>'mapping_type')::text
    FROM jsonb_array_elements(mappings_json) AS mapping;
END;
$$ LANGUAGE plpgsql;

-- Function to bulk insert corrections
CREATE OR REPLACE FUNCTION bulk_insert_corrections(corrections_json JSONB)
RETURNS void AS $$
BEGIN
    -- Delete existing corrections
    DELETE FROM corrections;
    
    -- Insert new corrections
    INSERT INTO corrections (
        id, node_id, correction_type, original_text, corrected_text, 
        correction_date, correction_source
    )
    SELECT
        (correction->>'id')::text,
        (correction->>'node_id')::text,
        (correction->>'correction_type')::text,
        (correction->>'original_text')::text,
        (correction->>'corrected_text')::text,
        (correction->>'correction_date')::timestamp,
        (correction->>'correction_source')::text
    FROM jsonb_array_elements(corrections_json) AS correction;
END;
$$ LANGUAGE plpgsql; 