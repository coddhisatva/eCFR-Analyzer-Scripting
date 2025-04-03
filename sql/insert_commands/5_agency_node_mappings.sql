-- Function to insert agency-node mappings from storage
CREATE OR REPLACE FUNCTION insert_agency_node_mappings_from_storage()
RETURNS void AS $$
DECLARE
    mappings_json jsonb;
BEGIN
    -- Read mappings from storage
    mappings_json := (
        SELECT content::jsonb 
        FROM storage.objects 
        WHERE bucket_id = 'json_tables' 
        AND name = 'agency_node_mappings.json'
    );
    
    -- Insert agency-node mappings
    INSERT INTO agency_node_mappings (
        agency_id, node_id, metadata
    )
    SELECT 
        (jsonb_array_elements(mappings_json)->>'agency_id')::text,
        (jsonb_array_elements(mappings_json)->>'node_id')::text,
        (jsonb_array_elements(mappings_json)->'metadata')::jsonb
    ON CONFLICT (agency_id, node_id) DO UPDATE SET
        metadata = EXCLUDED.metadata;
END;
$$ LANGUAGE plpgsql;

-- Command to insert agency-node mappings
SELECT insert_agency_node_mappings_from_storage(); 