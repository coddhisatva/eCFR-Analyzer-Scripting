-- Function to read JSON file and insert into table
CREATE OR REPLACE FUNCTION insert_from_json(table_name text, json_path text)
RETURNS void AS $$
BEGIN
    EXECUTE format('
        INSERT INTO %I 
        SELECT * FROM jsonb_populate_recordset(
            null::%I, 
            (pg_read_file(%L))::jsonb
        )', 
        table_name, 
        table_name,
        json_path
    );
END;
$$ LANGUAGE plpgsql;

-- Insert all data
DO $$
DECLARE
    base_path text := '/Users/conor/eCFR-Analyzer/eCFR-Processing/eCFR-Analyzer-Scripting/src/localPush/json_tables';
    title_num INTEGER;
BEGIN
    -- Insert global files
    PERFORM insert_from_json('agencies', base_path || '/agencies.json');
    PERFORM insert_from_json('cfr_references', base_path || '/cfr_references.json');
    PERFORM insert_from_json('agency_node_mappings', base_path || '/agency_node_mappings.json');
    
    -- Insert per-title files
    FOR title_num IN 1..50 LOOP
        IF title_num != 35 THEN  -- Skip title 35 as it's missing
            -- Insert nodes
            PERFORM insert_from_json(
                'nodes', 
                base_path || '/title_' || title_num || '/nodes.json'
            );
            
            -- Insert content chunks
            PERFORM insert_from_json(
                'content_chunks',
                base_path || '/title_' || title_num || '/content_chunks.json'
            );
        END IF;
    END LOOP;
END $$; 