import os
import re
import subprocess
import tempfile


def extract_blog_posts(org_content):
    # Split content into top-level headings
    sections = re.split(r"\n\* ", org_content)

    blog_posts = []
    for section in sections:
        # Check if the section is a blog post (has the :blog: tag)
        if ":blog:" in section:
            # Add the * back to the beginning of the section
            blog_posts.append("* " + section.strip())

    return blog_posts


def extract_metadata(post):
    metadata = {}

    # Extract title and tags
    title_match = re.search(
        r"\* (?:DONE |TODO )?(.+?) :blog:(.*?)$", post, re.MULTILINE
    )
    if title_match:
        metadata["title"] = title_match.group(1)
        metadata["tags"] = [
            tag for tag in title_match.group(2).strip().split(":") if tag
        ]

    # Extract ID and creation date
    id_match = re.search(r":ID: (.+)", post)
    created_match = re.search(r":CREATED: \[(.+)\]", post)

    if id_match:
        metadata["id"] = id_match.group(1)
    if created_match:
        metadata["created"] = created_match.group(1).split()[
            0
        ]  # Just take the date part

    return metadata


def org_to_markdown(org_content):
    with tempfile.NamedTemporaryFile(
        mode="w+", suffix=".org", encoding="utf-8", delete=False
    ) as temp_org:
        temp_org.write(org_content)
        temp_org_name = temp_org.name

    with tempfile.NamedTemporaryFile(
        mode="w+", suffix=".md", encoding="utf-8", delete=False
    ) as temp_md:
        temp_md_name = temp_md.name

    try:
        subprocess.run(
            [
                "pandoc",
                "-f",
                "org",
                "-t",
                "markdown",
                temp_org_name,
                "-o",
                temp_md_name,
            ],
            check=True,
        )
        with open(temp_md_name, "r", encoding="utf-8") as md_file:
            markdown_content = md_file.read()
    finally:
        os.unlink(temp_org_name)
        os.unlink(temp_md_name)

    return markdown_content


def process_org_files(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".org"):
            with open(os.path.join(input_dir, filename), "r", encoding="utf-8") as file:
                org_content = file.read()

            blog_posts = extract_blog_posts(org_content)

            for post in blog_posts:
                metadata = extract_metadata(post)
                if not metadata.get("id"):
                    print(f"Skipped a post in {filename}: No ID found")
                    continue

                markdown_content = org_to_markdown(post)

                # Create YAML front matter
                yaml_front_matter = "---\n"
                for key, value in metadata.items():
                    if key == "tags":
                        value = ", ".join(f'"{tag}"' for tag in value)
                        yaml_front_matter += f"tags: [{value}]\n"
                    else:
                        yaml_front_matter += f'{key}: "{value}"\n'
                yaml_front_matter += "---\n\n"

                # Combine YAML front matter and converted content
                final_content = yaml_front_matter + markdown_content

                output_filename = f"{metadata['id']}.md"
                with open(
                    os.path.join(output_dir, output_filename), "w", encoding="utf-8"
                ) as file:
                    file.write(final_content)
                print(f"Converted a post from {filename} to {output_filename}")


input_directory = "/home/tassilo/org-roam/org-roam"
output_directory = "/home/tassilo/repos/thoughts/test"

process_org_files(input_directory, output_directory)
