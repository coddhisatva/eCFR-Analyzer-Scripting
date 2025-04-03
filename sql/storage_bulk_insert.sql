-- Function to read from storage and bulk insert
CREATE OR REPLACE FUNCTION bulk_insert_from_storage(title_num text)
RETURNS void AS $$
DECLARE
    nodes_json jsonb;
    chunks_json jsonb;
BEGIN
    -- Read nodes from storage
    nodes_json := (
        SELECT content::jsonb 
        FROM storage.objects 
        WHERE bucket_id = 'json-tables' 
        AND name = 'title_' || title_num || '/nodes.json'
    );
    
    -- Read chunks from storage
    chunks_json := (
        SELECT content::jsonb 
        FROM storage.objects 
        WHERE bucket_id = 'json-tables' 
        AND name = 'title_' || title_num || '/content_chunks.json'
    );
    
    -- Call bulk insert functions
    PERFORM bulk_insert_nodes(nodes_json);
    PERFORM bulk_insert_content_chunks(chunks_json);
END;
$$ LANGUAGE plpgsql;

-- Function to process all titles
CREATE OR REPLACE FUNCTION process_all_titles()
RETURNS void AS $$
DECLARE
    title_num text;
BEGIN
    -- Process titles 1-50
    FOR title_num IN 1..50 LOOP
        BEGIN
            PERFORM bulk_insert_from_storage(title_num::text);
            RAISE NOTICE 'Successfully processed title %', title_num;
        EXCEPTION WHEN OTHERS THEN
            RAISE WARNING 'Error processing title %: %', title_num, SQLERRM;
        END;
    END LOOP;
END;
$$ LANGUAGE plpgsql; 