-- Function to insert CFR references from storage
CREATE OR REPLACE FUNCTION insert_cfr_references_from_storage()
RETURNS void AS $$
DECLARE
    refs_json jsonb;
BEGIN
    -- Read CFR references from storage
    refs_json := (
        SELECT metadata::jsonb 
        FROM storage.objects 
        WHERE bucket_id = 'json-tables' 
        AND name = 'cfr_references.json'
    );
    
    -- Call bulk insert function
    PERFORM bulk_insert_cfr_references(refs_json);
END;
$$ LANGUAGE plpgsql;

-- Command to insert CFR references
SELECT insert_cfr_references_from_storage(); 