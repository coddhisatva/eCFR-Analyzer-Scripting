-- Function to insert agency node mappings from storage
CREATE OR REPLACE FUNCTION insert_agency_node_mappings_from_storage()
RETURNS void AS $$
DECLARE
    mappings_json jsonb;
BEGIN
    -- Read mappings from storage
    mappings_json := (
        SELECT metadata::jsonb 
        FROM storage.objects 
        WHERE bucket_id = 'json-tables' 
        AND name = 'agency_node_mappings.json'
    );
    
    -- Call bulk insert function
    PERFORM bulk_insert_agency_node_mappings(mappings_json);
END;
$$ LANGUAGE plpgsql;

-- Command to insert agency node mappings
SELECT insert_agency_node_mappings_from_storage(); 