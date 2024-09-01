import os
import markdown
import datetime
from jinja2 import Environment, FileSystemLoader

# Configuration
POSTS_DIR = "posts"
OUTPUT_DIR = "docs"
TEMPLATE_DIR = "templates"


def read_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content


def parse_markdown(content):
    md = markdown.Markdown(extensions=["meta"])
    html = md.convert(content)
    return html, md.Meta


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

            # TODO: add eror handeling for wrong format
            print(f"filename: {filename}")
            print(metadata.get("date", [""]))
            print(metadata.get("date", [""])[0])
            post = {
                "title": metadata.get("title", [""])[0],
                "date": datetime.datetime.strptime(
                    metadata.get("date", [""])[0], "%Y-%m-%d"
                ),
                "content": html_content,
                "filename": os.path.join(
                    "docs", os.path.splitext(filename)[0] + ".html"
                ),
            }
            posts.append(post)

            # Generate individual post pages
            output = post_template.render(post=post)
            with open(post["filename"], "w", encoding="utf-8") as file:
                file.write(output)

    # Sort posts by date
    posts.sort(key=lambda x: x["date"], reverse=True)

    # Generate index page in the root directory
    index_output = index_template.render(posts=posts)
    with open("index.html", "w", encoding="utf-8") as file:
        file.write(index_output)


if __name__ == "__main__":
    generate_blog()
