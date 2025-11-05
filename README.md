# eCFR Analyzer

A comprehensive tool for analyzing and processing the Electronic Code of Federal Regulations (eCFR) data. This project provides a robust pipeline for processing, analyzing, and visualizing regulatory data from the eCFR. This is one of two Repos for project

![eCFR Analyzer Cover](screenshots/eCRF%20Cover.png)

**Live site**: https://ecfr-analyzer-lyart.vercel.app/

**Frontend Repo**: https://github.com/coddhisatva/eCFR-Analyzer-Frontend/tree/main

# Loom Video Demo

Click this link to check out a **loom video demo** of the eCRF Analyzer: https://www.loom.com/share/7732dd6c2c944942baa3e77377b109ad

## Overview

## Tech Stack

- **Backend**: Python 3.x
- **Database**: Supabase (PostgreSQL)
- **Data Processing**: BeautifulSoup4, lxml
- **Development Tools**:
  - Poetry for dependency management
  - Black for code formatting
  - Pytest for testing
  - GitHub Actions for CI/CD

## System Architecture

The system is designed as a modular pipeline with the following components:

1. **Data Processing Pipeline**
   - XML parsing and extraction
   - Node hierarchy processing
   - Agency relationship mapping
   - Correction tracking

2. **Database Layer**
   - Structured storage of regulatory data
   - Efficient querying and indexing
   - Relationship management

3. **Analysis Components**
   - Word count computation
   - Section count aggregation
   - Correction analysis
   - Agency hierarchy processing

## Repository Structure

```
eCFR-Analyzer-Scripting/
├── data/                    # Data storage
│   ├── raw/                # Raw XML files
│   └── processed/          # Processed data
├── src/
│   ├── data_processing/    # XML processing scripts
│   ├── precompute/         # Count computation scripts
│   ├── database/          # Database interaction
│   └── models/            # Data models
├── tests/                  # Test suite
└── scripts/               # Utility scripts
```

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

## Development

- The project uses Python 3.x
- Dependencies are managed via `requirements.txt`
- The project is installed in development mode for easy imports
- Follow PEP 8 style guidelines
- Use type hints for better code maintainability

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Add your license information here]

# eCFR Data Processing

This repository contains scripts for downloading and processing eCFR (Electronic Code of Federal Regulations) data.

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

## Data Pipeline

### 1. Download Data

Download the latest data for each component:

```bash
# Download nodes (XML) data
python3 src/data_download/download_xml.py --date 2025-03-31

# Download agencies data
python3 src/data_download/download_agencies.py --date 2025-03-31

# Download corrections data
python3 src/data_download/download_corrections.py --date 2025-03-31
```

### 2. Process and Compute

The pipeline alternates between processing raw data and computing derived metrics:

#### Nodes
1. Process XML into structured data:
```bash
python3 src/data_processing/process_xml.py --date 2025-03-31
```

2. Compute node metrics:
```bash
python3 src/precompute/compute_node_metrics.py
```

#### Agencies
1. Process agency data:
```bash
python3 src/data_processing/process_agencies.py --date 2025-03-31
```

2. Compute agency metrics:
```bash
python3 src/precompute/compute_agency_counts.py
```

#### Corrections
1. Process corrections data:
```bash
python3 src/data_processing/process_corrections.py --date 2025-03-31
```

2. Compute correction metrics:
```bash
python3 src/precompute/compute_correction_counts.py
```

## Development

For development guidelines and contribution instructions, see [CONTRIBUTING.md](CONTRIBUTING.md).