# Makefile for blog generation

# Directories
NOTEBOOKS_DIR := notebooks
HTML_OUTPUT_DIR := notebook_html
DOCS_DIR := docs
MARKDOWN_DIR := posts

# Python script
GENERATE_SCRIPT := generate_blog.py

# TODO: find nicer way to get env
# Python interpreter (using Poetry's virtual environment)
PYTHON := /home/tassilo/.cache/pypoetry/virtualenvs/thoughts-nVi2q3I2-py3.10/bin/python

# Find all Jupyter notebooks and Markdown files
NOTEBOOKS := $(wildcard $(NOTEBOOKS_DIR)/*.ipynb)
HTML_NOTEBOOKS := $(patsubst $(NOTEBOOKS_DIR)/%.ipynb,$(HTML_OUTPUT_DIR)/%.html,$(NOTEBOOKS))
MARKDOWN_FILES := $(wildcard $(MARKDOWN_DIR)/*.md)

# Default target
all: generate_blog

# Convert Jupyter notebooks to HTML
convert_notebooks: $(HTML_NOTEBOOKS)

$(HTML_OUTPUT_DIR)/%.html: $(NOTEBOOKS_DIR)/%.ipynb
	@mkdir -p $(HTML_OUTPUT_DIR)
	jupyter nbconvert --to html $< --output-dir=$(HTML_OUTPUT_DIR)

# Generate blog
generate_blog: convert_notebooks
	$(PYTHON) $(GENERATE_SCRIPT)

# Check if only Markdown files have changed
markdown_changed:
	@if git status --porcelain | grep -q "$(MARKDOWN_DIR)"; then \
		echo "Markdown files changed"; \
		exit 0; \
	else \
		echo "No Markdown files changed"; \
		exit 1; \
	fi

# Commit and push changes if only Markdown files changed
commit_and_push: markdown_changed generate_blog
	git add .
	git commit -m "Update blog"
	git push

# Clean generated files
clean:
	rm -rf $(HTML_OUTPUT_DIR)
	rm -rf $(DOCS_DIR)

# Phony targets
.PHONY: all convert_notebooks generate_blog clean markdown_changed commit_and_push
