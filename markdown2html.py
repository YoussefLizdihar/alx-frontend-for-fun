#!/usr/bin/env python3

"""
This script checks for the correct number of arguments,
verifies if the input Markdown file exists,
and handles errors accordingly.
If all conditions are met,
the script simply exits with a success code (0).
"""


import sys
import os

def main():
    # Check if the number of arguments is less than 2
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    # Extract the arguments
    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)
    
    # At this point, the script is successful
    sys.exit(0)

if __name__ == "__main__":
    main()

