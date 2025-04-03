-- Function to insert nodes from storage
CREATE OR REPLACE FUNCTION insert_nodes_from_storage()
RETURNS void AS $$
DECLARE
    nodes_json jsonb;
    title_num INTEGER;
BEGIN
    FOR title_num IN 1..50 LOOP
        -- Skip title 35 as it's missing
        IF title_num != 35 THEN
            -- Read nodes from storage
            nodes_json := (
                SELECT metadata::jsonb 
                FROM storage.objects 
                WHERE bucket_id = 'json_tables' 
                AND name = 'title_' || title_num || '/nodes.json'
            );
            
            -- Call bulk insert function if we found nodes
            IF nodes_json IS NOT NULL THEN
                PERFORM bulk_insert_nodes(nodes_json);
            END IF;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

-- Function to insert nodes from files
CREATE OR REPLACE FUNCTION insert_nodes_from_files()
RETURNS void AS $$
DECLARE
    base_path text := '/Users/conor/eCFR-Analyzer/eCFR-Processing/eCFR-Analyzer-Scripting/src/localPush/json_tables';
    title_num INTEGER;
    nodes_json jsonb;
BEGIN
    FOR title_num IN 1..50 LOOP
        -- Skip title 35 as it's missing
        IF title_num != 35 THEN
            -- Read nodes from file
            nodes_json := (pg_read_file(base_path || '/title_' || title_num || '/nodes.json'))::jsonb;
            
            -- Insert nodes if we found them
            IF nodes_json IS NOT NULL THEN
                INSERT INTO nodes 
                SELECT * FROM jsonb_populate_recordset(null::nodes, nodes_json);
            END IF;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

-- Command to insert all nodes
SELECT insert_nodes_from_storage();

-- Run it
SELECT insert_nodes_from_files(); 