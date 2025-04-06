# Directories
NOTEBOOKS_DIR := notebooks
HTML_OUTPUT_DIR := notebook_html
DOCS_DIR := docs
MARKDOWN_DIR := posts
TEMPLATE_DIR := templates

# Python script
GENERATE_SCRIPT := generate_blog.py
PYTHON := poetry run python
JUPYTER := poetry run jupyter

# Notebooks to HTML
NOTEBOOKS := $(wildcard $(NOTEBOOKS_DIR)/*.ipynb)
HTML_NOTEBOOKS := $(patsubst $(NOTEBOOKS_DIR)/%.ipynb,$(HTML_OUTPUT_DIR)/%.html,$(NOTEBOOKS))

# Markdown and templates
MARKDOWN_FILES := $(wildcard $(MARKDOWN_DIR)/*.md)
TEMPLATE_FILES := $(wildcard $(TEMPLATE_DIR)/*)

# Default target
all: blog

# Rule: convert a notebook if it's been updated
$(HTML_OUTPUT_DIR)/%.html: $(NOTEBOOKS_DIR)/%.ipynb
	@mkdir -p $(HTML_OUTPUT_DIR)
	$(JUPYTER) nbconvert --to html $< --output-dir=$(HTML_OUTPUT_DIR) --output=$*.html
	@echo "Converted $< -> $(HTML_OUTPUT_DIR)/$*.html"

# Rule: convert all notebooks
convert_notebooks: $(HTML_NOTEBOOKS)
	@echo "All notebook HTML up to date."

# Rule: generate blog if inputs changed
.blog.timestamp: $(MARKDOWN_FILES) $(HTML_NOTEBOOKS) $(TEMPLATE_FILES) $(GENERATE_SCRIPT)
	@mkdir -p $(DOCS_DIR)
	$(PYTHON) $(GENERATE_SCRIPT)
	@touch .blog.timestamp
	@echo "Blog regenerated."

blog: convert_notebooks .blog.timestamp

# Rule: clean everything
clean:
	rm -rf $(HTML_OUTPUT_DIR)
	rm -rf $(DOCS_DIR)
	rm -f .blog.timestamp

# Rule: commit + push if only Markdown changed
commit_and_push: blog
	@if git status --porcelain | grep -q "$(MARKDOWN_DIR)" && [ $$(git status --porcelain | grep -v "$(MARKDOWN_DIR)" | wc -l) -eq 0 ]; then \
		echo "Only Markdown changed, committing and pushing..."; \
		git add .; \
		git commit -m "Update blog"; \
		git push; \
	else \
		echo "Review changes manually before committing."; \
	fi

.PHONY: all blog clean convert_notebooks commit_and_push
