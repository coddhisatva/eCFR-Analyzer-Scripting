-- Function to insert nodes from storage
CREATE OR REPLACE FUNCTION insert_nodes_from_storage(title_num text)
RETURNS void AS $$
DECLARE
    nodes_json jsonb;
BEGIN
    -- Read nodes from storage
    nodes_json := (
        SELECT content::jsonb 
        FROM storage.objects 
        WHERE bucket_id = 'json_tables' 
        AND name = 'title_' || title_num || '/nodes.json'
    );
    
    -- Call bulk insert function
    PERFORM bulk_insert_nodes(nodes_json);
END;
$$ LANGUAGE plpgsql;

-- Command to insert nodes for a specific title
SELECT insert_nodes_from_storage('1');  -- Replace '1' with title number 