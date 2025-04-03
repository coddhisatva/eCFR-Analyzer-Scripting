-- Function to insert content chunks from storage
CREATE OR REPLACE FUNCTION insert_content_chunks_from_storage(title_num text)
RETURNS void AS $$
DECLARE
    chunks_json jsonb;
BEGIN
    -- Read chunks from storage
    chunks_json := (
        SELECT metadata::jsonb 
        FROM storage.objects 
        WHERE bucket_id = 'json-tables' 
        AND name = 'title_' || title_num || '/content_chunks.json'
    );
    
    -- Call bulk insert function
    PERFORM bulk_insert_content_chunks(chunks_json);
END;
$$ LANGUAGE plpgsql;

-- Command to insert content chunks for a specific title
SELECT insert_content_chunks_from_storage('1');  -- Replace '1' with title number 