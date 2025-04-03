# Database Configuration

This directory contains configuration files for database and storage operations.

## Setup Instructions

1. Copy `db_config.sh` to `db_config.local.sh`:
   ```bash
   cp db_config.sh db_config.local.sh
   ```

2. Edit `db_config.local.sh` with your actual credentials:
   ```bash
   # Database Connection Details
   export DB_HOST="your-actual-host"
   export DB_PORT="5432"
   export DB_NAME="your-db-name"
   export DB_USER="your-username"
   export DB_PASSWORD="your-password"
   
   # Supabase Storage Settings
   export STORAGE_BUCKET="json-tables"
   export STORAGE_URL="https://your-project.supabase.co/storage/v1"
   export SUPABASE_ANON_KEY="your-anon-key"
   ```

3. Source the configuration file before running any commands:
   ```bash
   source config/db_config.local.sh
   ```

## Available Functions

- `get_connection_string`: Get the PostgreSQL connection string
- `get_psql_command`: Get the psql command with connection
- `run_sql_file`: Run a SQL file
- `check_storage_bucket`: Check if storage bucket exists
- `list_storage_files`: List files in storage bucket
- `upload_to_storage`: Upload a file to storage
- `download_from_storage`: Download a file from storage
- `run_all_sql_files`: Run all SQL files in order
- `run_title_sql_files`: Run SQL files for a specific title

## Example Usage

```bash
# Source the configuration
source config/db_config.local.sh

# Run all SQL files
run_all_sql_files "sql/insert_commands"

# Run SQL files for title 1
run_title_sql_files "sql/insert_commands" "1"

# List files in storage bucket
list_storage_files

# Upload a file to storage
upload_to_storage "path/to/file.json" "title_1/nodes.json"
```

## Security Notes

- Never commit `db_config.local.sh` to version control
- Keep your credentials secure
- Use environment variables for sensitive data in production 