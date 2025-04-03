-- Function to insert corrections from storage
CREATE OR REPLACE FUNCTION insert_corrections_from_storage()
RETURNS void AS $$
DECLARE
    corrections_json jsonb;
BEGIN
    -- Read corrections from storage
    corrections_json := (
        SELECT content::jsonb 
        FROM storage.objects 
        WHERE bucket_id = 'json_tables' 
        AND name = 'corrections.json'
    );
    
    -- Insert corrections
    INSERT INTO corrections (
        node_id, agency_id, title, corrective_action, 
        error_corrected, error_occurred, correction_duration,
        fr_citation, position, year, metadata
    )
    SELECT 
        (jsonb_array_elements(corrections_json)->>'node_id')::text,
        (jsonb_array_elements(corrections_json)->>'agency_id')::text,
        (jsonb_array_elements(corrections_json)->>'title')::integer,
        (jsonb_array_elements(corrections_json)->>'corrective_action')::text,
        (jsonb_array_elements(corrections_json)->>'error_corrected')::date,
        (jsonb_array_elements(corrections_json)->>'error_occurred')::date,
        (jsonb_array_elements(corrections_json)->>'correction_duration')::integer,
        (jsonb_array_elements(corrections_json)->>'fr_citation')::text,
        (jsonb_array_elements(corrections_json)->>'position')::integer,
        (jsonb_array_elements(corrections_json)->>'year')::integer,
        (jsonb_array_elements(corrections_json)->'metadata')::jsonb
    ON CONFLICT (node_id, agency_id, title) DO UPDATE SET
        corrective_action = EXCLUDED.corrective_action,
        error_corrected = EXCLUDED.error_corrected,
        error_occurred = EXCLUDED.error_occurred,
        correction_duration = EXCLUDED.correction_duration,
        fr_citation = EXCLUDED.fr_citation,
        position = EXCLUDED.position,
        year = EXCLUDED.year,
        metadata = EXCLUDED.metadata;
END;
$$ LANGUAGE plpgsql;

-- Command to insert corrections
SELECT insert_corrections_from_storage(); 