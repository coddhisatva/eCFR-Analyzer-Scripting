-- Function to insert CFR references from storage
CREATE OR REPLACE FUNCTION insert_cfr_references_from_storage()
RETURNS void AS $$
DECLARE
    refs_json jsonb;
BEGIN
    -- Read references from storage
    refs_json := (
        SELECT content::jsonb 
        FROM storage.objects 
        WHERE bucket_id = 'json_tables' 
        AND name = 'cfr_references.json'
    );
    
    -- Insert CFR references
    INSERT INTO cfr_references (
        agency_id, title, subheading, ordinal, node_id
    )
    SELECT 
        (jsonb_array_elements(refs_json)->>'agency_id')::text,
        (jsonb_array_elements(refs_json)->>'title')::integer,
        (jsonb_array_elements(refs_json)->>'subheading')::text,
        (jsonb_array_elements(refs_json)->>'ordinal')::integer,
        (jsonb_array_elements(refs_json)->>'node_id')::text
    ON CONFLICT (agency_id, node_id) DO UPDATE SET
        title = EXCLUDED.title,
        subheading = EXCLUDED.subheading,
        ordinal = EXCLUDED.ordinal;
END;
$$ LANGUAGE plpgsql;

-- Command to insert CFR references
SELECT insert_cfr_references_from_storage(); 