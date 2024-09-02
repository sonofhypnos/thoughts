# Makefile for blog generation

# Directories
NOTEBOOKS_DIR := notebooks
HTML_OUTPUT_DIR := notebook_html
DOCS_DIR := docs
MARKDOWN_DIR := posts
TEMPLATE_DIR := templates

# Python script
GENERATE_SCRIPT := generate_blog.py

# Python interpreter (using Poetry's virtual environment)
PYTHON := /home/tassilo/.cache/pypoetry/virtualenvs/thoughts-nVi2q3I2-py3.10/bin/python

# Find all Jupyter notebooks, Markdown files, and templates
NOTEBOOKS := $(wildcard $(NOTEBOOKS_DIR)/*.ipynb)
HTML_NOTEBOOKS := $(patsubst $(NOTEBOOKS_DIR)/%.ipynb,$(HTML_OUTPUT_DIR)/%.html,$(NOTEBOOKS))
MARKDOWN_FILES := $(wildcard $(MARKDOWN_DIR)/*.md)
TEMPLATE_FILES := $(wildcard $(TEMPLATE_DIR)/*)

# Default target
all: blog

# Convert Jupyter notebooks to HTML
$(HTML_OUTPUT_DIR)/%.html: $(NOTEBOOKS_DIR)/%.ipynb
	@mkdir -p $(HTML_OUTPUT_DIR)
	jupyter nbconvert --to html $< --output-dir=$(HTML_OUTPUT_DIR)

# Generate blog
.blog.timestamp: $(MARKDOWN_FILES) $(HTML_NOTEBOOKS) $(TEMPLATE_FILES) $(GENERATE_SCRIPT)
	@mkdir -p $(DOCS_DIR)
	$(PYTHON) $(GENERATE_SCRIPT)
	@touch $@

blog: .blog.timestamp

# Commit and push changes if only Markdown files changed
commit_and_push: blog
	@if git status --porcelain | grep -q "$(MARKDOWN_DIR)" && [ $$(git status --porcelain | grep -v "$(MARKDOWN_DIR)" | wc -l) -eq 0 ]; then \
		echo "Only Markdown files changed. Committing and pushing changes..."; \
		git add .; \
		git commit -m "Update blog"; \
		git push; \
		echo "Changes pushed successfully."; \
	elif git status --porcelain | grep -q .; then \
		echo "Multiple file types changed. Please review changes and commit manually."; \
	else \
		echo "No changes to commit."; \
	fi

# Clean generated files
clean:
	rm -rf $(HTML_OUTPUT_DIR)
	rm -rf $(DOCS_DIR)
	rm -f .blog.timestamp

# Phony targets
.PHONY: all blog clean commit_and_push
