-- Function to insert agencies from storage
CREATE OR REPLACE FUNCTION insert_agencies_from_storage()
RETURNS void AS $$
DECLARE
    agencies_json jsonb;
BEGIN
    -- Read agencies from storage
    agencies_json := (
        SELECT content::jsonb 
        FROM storage.objects 
        WHERE bucket_id = 'json_tables' 
        AND name = 'agencies.json'
    );
    
    -- Insert agencies
    INSERT INTO agencies (
        id, name, description, parent_id, depth, 
        num_children, num_cfr, num_words, 
        num_sections, num_corrections, cfr_references
    )
    SELECT 
        (jsonb_array_elements(agencies_json)->>'id')::text,
        (jsonb_array_elements(agencies_json)->>'name')::text,
        (jsonb_array_elements(agencies_json)->>'description')::text,
        (jsonb_array_elements(agencies_json)->>'parent_id')::text,
        (jsonb_array_elements(agencies_json)->>'depth')::integer,
        (jsonb_array_elements(agencies_json)->>'num_children')::integer,
        (jsonb_array_elements(agencies_json)->>'num_cfr')::integer,
        (jsonb_array_elements(agencies_json)->>'num_words')::integer,
        (jsonb_array_elements(agencies_json)->>'num_sections')::integer,
        (jsonb_array_elements(agencies_json)->>'num_corrections')::integer,
        (jsonb_array_elements(agencies_json)->'cfr_references')::text[]
    ON CONFLICT (id) DO UPDATE SET
        name = EXCLUDED.name,
        description = EXCLUDED.description,
        parent_id = EXCLUDED.parent_id,
        depth = EXCLUDED.depth,
        num_children = EXCLUDED.num_children,
        num_cfr = EXCLUDED.num_cfr,
        num_words = EXCLUDED.num_words,
        num_sections = EXCLUDED.num_sections,
        num_corrections = EXCLUDED.num_corrections,
        cfr_references = EXCLUDED.cfr_references;
END;
$$ LANGUAGE plpgsql;

-- Command to insert agencies
SELECT insert_agencies_from_storage(); 