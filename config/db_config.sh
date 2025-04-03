#!/bin/bash

# Database Connection Details
export DB_HOST="db.ybootrcxmjgokgzbozgv.supabase.co"
export DB_PORT="5432"
export DB_NAME="postgres"
export DB_USER="postgres"
export DB_PASSWORD="${DB_PASSWORD:-Fj@4P@j5aQ3iJtT}"

# Supabase Storage Settings
export STORAGE_BUCKET="json-tables"
export STORAGE_URL="https://ybootrcxmjgokgzbozgv.supabase.co/storage/v1"

# Database Schema Settings
export DB_SCHEMA="public"

# Function to get the connection string
get_connection_string() {
    echo "postgresql://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}"
}

# Function to get the psql command with connection
get_psql_command() {
    echo "psql \"$(get_connection_string)\""
}

# Function to run a SQL file
run_sql_file() {
    local file=$1
    $(get_psql_command) -f "$file"
}

# Function to check if storage bucket exists
check_storage_bucket() {
    curl -s -X GET "${STORAGE_URL}/bucket/${STORAGE_BUCKET}" \
        -H "Authorization: Bearer ${SUPABASE_ANON_KEY}" \
        -H "Content-Type: application/json"
}

# Function to list files in storage bucket
list_storage_files() {
    curl -s -X GET "${STORAGE_URL}/object/list/${STORAGE_BUCKET}" \
        -H "Authorization: Bearer ${SUPABASE_ANON_KEY}" \
        -H "Content-Type: application/json"
}

# Function to upload a file to storage
upload_to_storage() {
    local file_path=$1
    local storage_path=$2
    curl -s -X POST "${STORAGE_URL}/object/${STORAGE_BUCKET}/${storage_path}" \
        -H "Authorization: Bearer ${SUPABASE_ANON_KEY}" \
        -H "Content-Type: application/json" \
        --data-binary "@${file_path}"
}

# Function to download a file from storage
download_from_storage() {
    local storage_path=$1
    local output_path=$2
    curl -s -X GET "${STORAGE_URL}/object/${STORAGE_BUCKET}/${storage_path}" \
        -H "Authorization: Bearer ${SUPABASE_ANON_KEY}" \
        -o "${output_path}"
}

# Function to run all SQL files in order
run_all_sql_files() {
    local base_dir=$1
    local files=(
        "1_nodes.sql"
        "2_content_chunks.sql"
        "3_agencies.sql"
        "4_cfr_references.sql"
        "5_agency_node_mappings.sql"
        "6_corrections.sql"
    )
    
    for file in "${files[@]}"; do
        echo "Running ${file}..."
        run_sql_file "${base_dir}/${file}"
    done
}

# Function to run SQL files for a specific title
run_title_sql_files() {
    local base_dir=$1
    local title_num=$2
    
    echo "Running nodes for title ${title_num}..."
    $(get_psql_command) -c "SELECT insert_nodes_from_storage('${title_num}');"
    
    echo "Running content chunks for title ${title_num}..."
    $(get_psql_command) -c "SELECT insert_content_chunks_from_storage('${title_num}');"
}

# Export all functions
export -f get_connection_string
export -f get_psql_command
export -f run_sql_file
export -f check_storage_bucket
export -f list_storage_files
export -f upload_to_storage
export -f download_from_storage
export -f run_all_sql_files
export -f run_title_sql_files 