# Makefile for blog generation

# Directories
NOTEBOOKS_DIR := notebooks
HTML_OUTPUT_DIR := notebook_html
DOCS_DIR := docs
MARKDOWN_DIR := posts

# Python script
GENERATE_SCRIPT := generate_blog.py

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
check_changes:
	@echo "Checking for changes..."
	@if git status --porcelain | grep -q "$(MARKDOWN_DIR)" && [ $$(git status --porcelain | grep -v "$(MARKDOWN_DIR)" | wc -l) -eq 0 ]; then \
		echo "Only Markdown files changed. Safe to auto-commit."; \
		echo "markdown_only" > .change_status; \
	elif git status --porcelain | grep -q .; then \
		echo "Multiple file types changed. Manual review required."; \
		echo "mixed_changes" > .change_status; \
	else \
		echo "No changes detected."; \
		echo "no_changes" > .change_status; \
	fi

# Commit and push changes if only Markdown files changed
commit_and_push: check_changes generate_blog
	@if [ "$$(cat .change_status)" = "markdown_only" ]; then \
		echo "Committing and pushing changes..."; \
		git add .; \
		git commit -m "Update blog"; \
		git push; \
		echo "Changes pushed successfully."; \
	elif [ "$$(cat .change_status)" = "mixed_changes" ]; then \
		echo "Blog generated. Please review changes and commit manually."; \
	else \
		echo "No changes to commit."; \
	fi
	@rm .change_status

# Clean generated files
clean:
	rm -rf $(HTML_OUTPUT_DIR)
	rm -rf $(DOCS_DIR)
	rm -f .change_status

# Phony targets
.PHONY: all convert_notebooks generate_blog clean check_changes commit_and_push
