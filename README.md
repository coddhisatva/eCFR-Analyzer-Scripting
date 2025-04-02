# eCFR Analyzer Scripting

A tool for downloading, processing, and analyzing the Electronic Code of Federal Regulations (eCFR).

## Setup

1. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and fill in your Supabase credentials:
```bash
cp .env.example .env
```

## Usage

### Process a specific title:

1. Process XML data:
```bash
PYTHONPATH=/path/to/project python3 src/data_processing/process_xml.py data/raw/titles/2025-03-31/title-5.xml
```

2. Process agency data:
```bash
PYTHONPATH=/path/to/project python3 src/data_processing/process_agencies.py data/raw/agencies/2025-03-31/agency-title-5.json
```

3. Process corrections data:
```bash
PYTHONPATH=/path/to/project python3 src/data_processing/process_corrections.py data/raw/corrections/2025-03-31/corrections-title-5.json
```

### Process all files for a specific date:

1. Process all XML data:
```bash
PYTHONPATH=/path/to/project python3 src/data_processing/process_xml.py data/raw/titles/2025-03-31/
```

2. Process all agency data:
```bash
PYTHONPATH=/path/to/project python3 src/data_processing/process_agencies.py data/raw/agencies/2025-03-31/
```

3. Process all corrections data:
```bash
PYTHONPATH=/path/to/project python3 src/data_processing/process_corrections.py data/raw/corrections/2025-03-31/
```

## Project Structure

- `src/data_collection/`: Scripts for downloading data
- `src/data_processing/`: Scripts for processing data
- `src/models/`: Data models
- `src/database/`: Database connection and operations
- `data/raw/`: Raw XML files
- `data/processed/`: Processed data