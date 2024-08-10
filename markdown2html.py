#!/usr/bin/env python3
import sys
import os
import markdown

"""
generate content from an HTML file using python
"""

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown file and convert it to HTML
    with open(markdown_file, 'r') as md_file:
        md_content = md_file.read()
        html_content = markdown.markdown(md_content)

    # Write the HTML content to the output file
    with open(output_file, 'w') as html_file:
        html_file.write(html_content)

    # If everything went fine, exit with status 0
    sys.exit(0)

if __name__ == "__main__":
    main()

