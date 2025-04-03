# Database Insertion Commands

This directory contains SQL commands for inserting data into the database in the correct order.

## Insertion Order

1. `1_nodes.sql` - Insert nodes for each title
2. `2_content_chunks.sql` - Insert content chunks for each title
3. `3_agencies.sql` - Insert agencies
4. `4_cfr_references.sql` - Insert CFR references
5. `5_agency_node_mappings.sql` - Insert agency-node mappings
6. `6_corrections.sql` - Insert corrections

## Usage Instructions

1. First, upload all JSON files to the 'json_tables' bucket in Supabase storage
2. Execute the SQL files in order (1-6)
3. For nodes and content chunks, you'll need to run the commands for each title (1-50)

## File Structure in Storage

The 'json_tables' bucket should contain:
- `title_1/nodes.json`
- `title_1/content_chunks.json`
- `title_2/nodes.json`
- `title_2/content_chunks.json`
- ... (for all titles 1-50)
- `agencies.json`
- `cfr_references.json`
- `agency_node_mappings.json`
- `corrections.json`

## Notes

- All functions handle conflicts with ON CONFLICT DO UPDATE
- The largest file is under Supabase's 100MB storage limit
- Foreign key constraints are maintained by the insertion order 