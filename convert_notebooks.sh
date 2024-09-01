#!/bin/bash

NOTEBOOKS_DIR="notebooks"
HTML_OUTPUT_DIR="notebook_html"

# Create output directory if it doesn't exist
mkdir -p "$HTML_OUTPUT_DIR"

# Convert each notebook to HTML
for notebook in "$NOTEBOOKS_DIR"/*.ipynb; do
    filename=$(basename "$notebook" .ipynb)
    jupyter nbconvert --to html "$notebook" --output-dir="$HTML_OUTPUT_DIR" --output="${filename}.html"
done

echo "Conversion complete. HTML files are in $HTML_OUTPUT_DIR"
