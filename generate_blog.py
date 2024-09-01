import os
import json
import markdown
import datetime
from jinja2 import Environment, FileSystemLoader
from bs4 import BeautifulSoup
import nbformat
from nbconvert import HTMLExporter


# Constants
OUTPUT_DIR = "docs"
TEMPLATE_DIR = "templates"
POSTS_DIR = "posts"
NOTEBOOKS_DIR = "notebooks"
NOTEBOOKS_HTML_DIR = "notebook_html"
PREVIEW_LENGTH = 200

# def parse_notebook(file_path):
#     with open(file_path, "r", encoding="utf-8") as file:
#         notebook_content = json.load(file)

#     notebook = nbformat.from_dict(notebook_content)
#     first_cell = notebook_content["cells"][0]
#     if first_cell["cell_type"] != "markdown":
#         raise ValueError("First cell must be markdown")

#     title = first_cell["source"][0].strip("#").strip()
#     if not title:
#         raise ValueError(
#             "Title must be provided in the first cell in the first line of the notebook."
#         )

#     # Extract metadata from the filename
#     filename = os.path.basename(file_path)
#     date_str, title = filename.split("-", 1)

#     # Convert notebook to HTML
#     html_exporter = nbconvert.HTMLExporter()
#     html_exporter.template_name = "basic"
#     html_content, _ = html_exporter.from_notebook_node(notebook)

#     metadata = {"title": [title], "date": [date_str]}

#     return html_content, metadata


def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def parse_notebook(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        notebook_content = json.load(file)

    # Create a NotebookNode object
    notebook = nbformat.from_dict(notebook_content)

    # Extract metadata from the filename
    filename = os.path.basename(file_path)
    date_str, title = filename.split("-", 1)
    title = title.rsplit(".", 1)[0].replace("-", " ").title()

    # Convert notebook to HTML
    html_exporter = HTMLExporter()
    html_exporter.template_name = "basic"
    html_content, _ = html_exporter.from_notebook_node(notebook)

    metadata = {"title": [title], "date": [date_str]}

    return html_content, metadata


def generate_preview(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the first image
    img_tag = soup.find("img")
    img_html = str(img_tag) if img_tag else ""

    # Get text content
    text_content = soup.get_text()
    text_preview = text_content[:PREVIEW_LENGTH].rsplit(" ", 1)[0] + "..."

    return f"{img_html}<p>{text_preview}</p>"


def read_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def parse_markdown(content):
    md = markdown.Markdown(
        extensions=["meta", "footnotes", "fenced_code", "codehilite"]
    )
    html = md.convert(content)
    return html, md.Meta


def to_title_case(title):
    words = title.split()
    minor_words = {
        "a",
        "an",
        "and",
        "as",
        "at",
        "but",
        "by",
        "for",
        "in",
        "nor",
        "of",
        "on",
        "or",
        "so",
        "the",
        "to",
        "up",
        "yet",
    }

    result = []
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word.lower() not in minor_words:
            result.append(word.capitalize())
        else:
            result.append(word.lower())

    return " ".join(result)


def generate_blog():
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    post_template = env.get_template("post.html")
    index_template = env.get_template("index.html")

    # Process all markdown files
    posts = []
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".md"):
            file_path = os.path.join(POSTS_DIR, filename)
            content = read_markdown_file(file_path)
            html_content, metadata = parse_markdown(content)

            try:
                post = {
                    "title": to_title_case(metadata.get("title", [""])[0]),
                    "date": datetime.datetime.strptime(
                        metadata.get("date", [""])[0], "%Y-%m-%d"
                    ),
                    "content": html_content,
                    "filename": os.path.join(
                        OUTPUT_DIR, os.path.splitext(filename)[0] + ".html"
                    ),
                    "tags": metadata.get("tags", []),
                    "preview": generate_preview(html_content),
                }
                print(f"Processing {filename}...")
                print(f"Tags: {post['tags']}")
                posts.append(post)

                # Generate individual post pages
                output = post_template.render(post=post)
                with open(post["filename"], "w", encoding="utf-8") as file:
                    file.write(output)
            except (ValueError, IndexError, AttributeError) as e:
                print(f"Error processing {filename}: {str(e)}")
                continue

    # Process Jupyter Notebooks
    for filename in os.listdir(NOTEBOOKS_HTML_DIR):
        if filename.endswith(".html"):
            file_path = os.path.join(NOTEBOOKS_HTML_DIR, filename)
            html_content = read_file(file_path)

            # Extract date and title from filename (assuming YYYY-MM-DD-title.html format)
            strings = filename.split("-")
            date_str = "-".join(strings[0:3])
            title = strings[3].split(".")[0]
            print(title)

            title = title.rsplit(".", 1)[0].replace("-", " ").title()

            try:
                post = {
                    "title": to_title_case(title),
                    "date": datetime.datetime.strptime(date_str, "%Y-%m-%d"),
                    "content": html_content,
                    "preview": generate_preview(html_content),
                    "filename": os.path.join(OUTPUT_DIR, filename),
                    "tags": ["notebook"],
                }
                posts.append(post)

                # Copy the HTML file to the output directory
                with open(post["filename"], "w", encoding="utf-8") as file:
                    file.write(html_content)
            except (ValueError, IndexError) as e:
                print(f"Error processing {filename}: {str(e)}")
                continue
    # Sort posts by date
    posts.sort(key=lambda x: x["date"], reverse=True)

    filtered_posts = [post for post in posts if "hidden" not in post["tags"]]

    # Generate index page in the root directory
    index_output = index_template.render(posts=filtered_posts)
    with open(os.path.join("./", "index.html"), "w", encoding="utf-8") as file:
        file.write(index_output)


if __name__ == "__main__":
    generate_blog()
