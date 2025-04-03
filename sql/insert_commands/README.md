# Database Insertion Commands

This directory contains SQL commands for inserting data into the database in the correct order.

## Insertion Order

1. `1_nodes.sql` - Insert nodes for each title
2. `2_content_chunks.sql` - Insert content chunks for each title
3. `3_agencies.sql` - Insert agencies
4. `4_cfr_references.sql` - Insert CFR references
5. `5_agency_node_mappings.sql` - Insert agency-node mappings
6. `6_corrections.sql` - Insert corrections

## Prerequisites

1. The bulk insert functions must be loaded first (from sql/bulk_insert.sql)
2. All files must be uploaded to the 'json-tables' bucket in Supabase storage
3. Storage schema and tables must be enabled in your Supabase project

## File Structure in Storage

The 'json-tables' bucket should contain:
- `title_1/nodes.json`
- `title_1/content_chunks.json`
- `title_2/nodes.json`
- `title_2/content_chunks.json`
- ... (for all titles 1-50, except 35 which is missing)
- `agencies.json`
- `cfr_references.json`
- `agency_node_mappings.json`
- `corrections.json`

## Usage Instructions

1. First, run sql/bulk_insert.sql to create the bulk insert functions
2. Then run the SQL files in order (1-6)
3. For title-specific files (nodes and content_chunks):
   - Test with title_1 first
   - Then run for titles 2-50 (except 35)

## Notes

- All functions handle conflicts appropriately
- The largest file is under Supabase's 100MB storage limit
- Foreign key constraints are maintained by the insertion order
- Title 35 is missing and should be skipped
- Files are read from the storage.objects table's metadata column

____

I've created all the necessary SQL files in sql/insert_commands/. Here's what each file does:
1_nodes.sql - Inserts nodes for each title
2_content_chunks.sql - Inserts content chunks for each title
3_agencies.sql - Inserts all agencies
4_cfr_references.sql - Inserts CFR references
5_agency_node_mappings.sql - Inserts agency-node mappings
6_corrections.sql - Inserts corrections
Each file contains:
A function to read from Supabase storage
A function to insert the data
Proper conflict handling
Type casting for all fields
The README.md explains the order and usage.
To use these:
Upload your JSON files to the 'json_tables' bucket
Run the SQL files in order (1-6)
For nodes and content chunks, run the commands for each title (1-50) -- actually no, we'll run for title 1 as a test, then we need to alter the command for 2-50
Then we'll alter the chunk command for all 1-50
(ps title 35 is missing)
Just remember:
Upload all JSON files to the 'json_tables' bucket first
Run the SQL files in order (1-6)
For nodes and content chunks, you'll need to run the commands for each title (1-50)