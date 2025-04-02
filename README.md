# eCFR Analyzer

A comprehensive tool for analyzing and processing the Electronic Code of Federal Regulations (eCFR) data. This project provides a robust pipeline for processing, analyzing, and visualizing regulatory data from the eCFR.

## Overview

The eCFR Analyzer is part of a larger ecosystem that includes:
- [eCFR-Analyzer-UI](https://github.com/your-org/eCFR-Analyzer-UI) - The frontend application
- [eCFR-Analyzer-API](https://github.com/your-org/eCFR-Analyzer-API) - The backend API service
- [Live Demo](https://ecfr-analyzer.vercel.app) - The deployed application

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

## Processing Data

1. Process all XML files (recommended approach):
```bash
./process_xml.sh 2024-03-31  # Replace with your desired date
```

Alternative direct Python approach:
```bash
python src/data_processing/process_xml.py --date 2024-03-31
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