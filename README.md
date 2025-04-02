# eCFR Analyzer

A tool for analyzing and processing eCFR (Electronic Code of Federal Regulations) data.

## Setup

1. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Unix/macOS
# or
.\venv\Scripts\activate  # On Windows
```

2. Install dependencies:
```bash
pip install -e .
```

## Processing Data

1. Process all XML files:
```bash
python src/data_processing/process_xml.py --input-dir data/raw/2024-03-31
```

2. Compute node counts:
```bash
python src/precompute/compute_node_counts.py
```

3. Process agencies:
```bash
python src/precompute/process_agencies.py
```

4. Compute correction counts:
```bash
python src/precompute/compute_correction_counts.py
```

## Development

- The project uses Python 3.x
- Dependencies are managed via `requirements.txt`
- The project is installed in development mode for easy imports