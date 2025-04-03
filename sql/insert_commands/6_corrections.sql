-- Function to insert corrections from storage
CREATE OR REPLACE FUNCTION insert_corrections_from_storage()
RETURNS void AS $$
DECLARE
    corrections_json jsonb;
BEGIN
    -- Read corrections from storage
    corrections_json := (
        SELECT metadata::jsonb 
        FROM storage.objects 
        WHERE bucket_id = 'json-tables' 
        AND name = 'corrections.json'
    );
    
    -- Call bulk insert function
    PERFORM bulk_insert_corrections(corrections_json);
END;
$$ LANGUAGE plpgsql;

-- Command to insert corrections
SELECT insert_corrections_from_storage(); 