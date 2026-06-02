#!/usr/bin/env bash
# One-shot setup and run script for nanogt results pipeline.
# Run from repo root: bash setup_and_run.sh

set -e
cd "$(dirname "$0")"

echo "=== nanogt setup ==="

# Prefer the existing Python 3.11 venv if available
if [ -d ".venv_(my_python_environment)" ]; then
    source ".venv_(my_python_environment)/bin/activate"
    echo "Using existing venv (Python 3.11)"
elif [ -d ".venv" ]; then
    source ".venv/bin/activate"
    echo "Using .venv"
else
    echo "No venv found — using system Python"
fi

# Install dependencies
echo "Installing dependencies..."
pip install typer requests rich jinja2 pydantic --quiet --break-system-packages 2>/dev/null || \
pip install typer requests rich jinja2 pydantic --quiet

echo ""
echo "=== Running pipeline ==="
python run_results.py

echo ""
echo "=== Reports ==="
ls -la output/
