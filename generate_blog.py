import os
import markdown
import datetime
from jinja2 import Environment, FileSystemLoader
from bs4 import BeautifulSoup

# Constants
OUTPUT_DIR = "docs"
TEMPLATE_DIR = "templates"
POSTS_DIR = "posts"


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
                }
                posts.append(post)

                # Generate individual post pages
                output = post_template.render(post=post)
                with open(post["filename"], "w", encoding="utf-8") as file:
                    file.write(output)
            except (ValueError, IndexError) as e:
                print(f"Error processing {filename}: {str(e)}")
                continue

    # Sort posts by date
    posts.sort(key=lambda x: x["date"], reverse=True)

    # Generate index page in the root directory
    index_output = index_template.render(posts=posts)
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as file:
        file.write(index_output)


if __name__ == "__main__":
    generate_blog()
