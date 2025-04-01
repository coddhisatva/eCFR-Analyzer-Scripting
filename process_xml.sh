#!/bin/bash
source venv/bin/activate
PYTHONPATH=$PYTHONPATH:. python3 src/data_processing/process_xml.py "$@" 