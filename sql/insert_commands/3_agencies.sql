-- Function to insert agencies from storage
CREATE OR REPLACE FUNCTION insert_agencies_from_storage()
RETURNS void AS $$
DECLARE
    agencies_json jsonb;
BEGIN
    -- Read agencies from storage
    agencies_json := (
        SELECT metadata::jsonb 
        FROM storage.objects 
        WHERE bucket_id = 'json-tables' 
        AND name = 'agencies.json'
    );
    
    -- Call bulk insert function
    PERFORM bulk_insert_agencies(agencies_json);
END;
$$ LANGUAGE plpgsql;

-- Command to insert agencies
SELECT insert_agencies_from_storage(); 