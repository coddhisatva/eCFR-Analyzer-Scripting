# eCFR Analyzer Scripting

A tool for downloading, processing, and analyzing the Electronic Code of Federal Regulations (eCFR).

## Setup

1. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

2. Install dependencies:
pip install -r requirements.txt

3. Copy `.env.example` to `.env` and fill in your Supabase credentials:
cp .env.example .env

## Usage

### Download CFR XML data:
python src/main.py --download

### Process XML data into database:
python src/main.py --process

### Download and process a specific title:
python src/main.py --download --process --title 4

### Process data for a specific date:
python src/main.py --process --date 2023-01-01

## Project Structure

- `src/data_collection/`: Scripts for downloading data
- `src/data_processing/`: Scripts for processing data
- `src/models/`: Data models
- `src/database/`: Database connection and operations
- `data/raw/`: Raw XML files
- `data/processed/`: Processed data