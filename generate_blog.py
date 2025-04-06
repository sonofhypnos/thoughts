import os
import re
import json
import markdown
import datetime
from typing import Dict, List, Tuple, Any, Optional, Union
from jinja2 import Environment, FileSystemLoader
from bs4 import BeautifulSoup

# Constants
OUTPUT_DIR = "docs"
TEMPLATE_DIR = "templates"
POSTS_DIR = "posts"
NOTEBOOKS_DIR = "notebooks"
NOTEBOOKS_HTML_DIR = "notebook_html"
PREVIEW_LENGTH = 200
BASE_URL = "https://www.tassiloneubauer.com"  # Added https:// for valid URLs
BLOG_TITLE = "Tassilo Neubauer"
BLOG_DESCRIPTION = "Tassilo Neubauer's Blog"  # Add a description for your blog
BLOG_AUTHOR = "Tassilo Neubauer"  # Add your name as the author


def generate_description(html_content: str, max_length: int = 200) -> str:
    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text()
    description = " ".join(text.split()[:30])  # Get first 30 words
    if len(description) > max_length:
        description = description[: max_length - 3] + "..."
    return description


def extract_first_image(html_content: str) -> str:
    soup = BeautifulSoup(html_content, "html.parser")
    img = soup.find("img")
    return img["src"] if img else ""


def parse_notebook(file_path: str) -> Dict[str, str]:
    with open(file_path, "r", encoding="utf-8") as file:
        notebook_content = json.load(file)

    first_cell = notebook_content["cells"][0]
    if first_cell["cell_type"] != "markdown":
        raise ValueError("First cell must be markdown")

    title = first_cell["source"][0].strip("#").strip()
    if not title:
        raise ValueError(
            "Title must be provided in the first cell in the first line of the notebook."
        )

    metadata: Dict[str, str] = {"title": title}

    return metadata


def read_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def generate_preview(html_content: str) -> str:
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the first image
    img_tag = soup.find("img")
    img_html = str(img_tag) if img_tag else ""

    # Get text content
    text_content = soup.get_text()
    text_preview = text_content[:PREVIEW_LENGTH].rsplit(" ", 1)[0] + "..."

    return f"{img_html}<p>{text_preview}</p>"


def read_markdown_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def parse_markdown(content: str) -> Tuple[str, Dict[str, List[str]]]:
    md = markdown.Markdown(
        extensions=["meta", "footnotes", "fenced_code", "codehilite"]
    )
    html = md.convert(content)
    return html, md.Meta


def to_title_case(title: str) -> str:
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


def strip_html_tags(html_content: str) -> str:
    """Strip HTML tags from content for RSS description"""
    soup = BeautifulSoup(html_content, "html.parser")
    return soup.get_text()


def generate_rss(posts: List[Dict[str, Any]]) -> None:
    """Generate RSS feed XML from posts"""
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    rss_template = env.get_template("rss.xml")

    # Make a copy of posts and modify for RSS compatibility
    rss_posts = []
    for post in posts:
        rss_post = post.copy()
        # Ensure full URL for content
        rss_post["full_url"] = f"{BASE_URL}/{os.path.basename(post['filename'])}"
        # Strip HTML tags for description
        rss_post["plain_description"] = strip_html_tags(post["description"])
        rss_posts.append(rss_post)

    # Generate RSS feed
    rss_output = rss_template.render(
        posts=rss_posts,
        blog_title=BLOG_TITLE,
        blog_description=BLOG_DESCRIPTION,
        blog_url=BASE_URL,
        build_date=datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000"),
        author=BLOG_AUTHOR,
    )

    # Write RSS file
    with open(os.path.join("./", "feed.xml"), "w", encoding="utf-8") as file:
        file.write(rss_output)


def generate_blog() -> None:
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    post_template = env.get_template("post.html")
    index_template = env.get_template("index.html")

    # Process all markdown files
    posts: List[Dict[str, Any]] = []
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".md"):
            file_path = os.path.join(POSTS_DIR, filename)
            content = read_markdown_file(file_path)
            processed_html, metadata = parse_markdown(content)

            try:
                # TODO: check that id is unique and otherwise throw warning
                blogpost_id = metadata.get("id", [""])[0]
                if blogpost_id[0] == '"':
                    blogpost_id = blogpost_id[1:]
                if blogpost_id[-1] == '"':
                    blogpost_id = blogpost_id[:-1]

                post = {
                    "title": to_title_case(metadata.get("title", [""])[0]),
                    "date": datetime.datetime.strptime(
                        metadata.get("date", [""])[0], "%Y-%m-%d"
                    ),
                    "content": processed_html,
                    "filename": os.path.join(OUTPUT_DIR, blogpost_id + ".html"),
                    "tags": metadata.get("tags", []),
                    "preview": generate_preview(processed_html),
                    "url": f"{BASE_URL}/{blogpost_id}.html",
                    "description": metadata.get("description", [""])[0]
                    or generate_description(processed_html),
                    "image": metadata.get("image", [""])[0]
                    or extract_first_image(processed_html),
                    "blog_title": BLOG_TITLE,
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
            processed_html = read_file(file_path)

            # Extract date and title from filename (assuming YYYY-MM-DD-title.html format)
            strings = filename.split("-")
            date_str = "-".join(strings[0:3])
            title = "-".join(strings[3:]).replace(".html", "")

            try:
                post = {
                    "title": to_title_case(title),
                    "date": datetime.datetime.strptime(date_str, "%Y-%m-%d"),
                    "content": processed_html,
                    "preview": generate_preview(processed_html),
                    "filename": os.path.join(OUTPUT_DIR, filename),
                    "tags": ["notebook"],
                    "url": f"{BASE_URL}/{filename}",
                    "description": generate_description(processed_html),
                    "image": extract_first_image(processed_html),
                    "blog_title": BLOG_TITLE,
                }
                posts.append(post)

                # Generate individual notebook pages
                output = post_template.render(post=post)
                with open(post["filename"], "w", encoding="utf-8") as file:
                    file.write(output)
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

    # Generate RSS feed
    generate_rss(filtered_posts)


if __name__ == "__main__":
    generate_blog()
