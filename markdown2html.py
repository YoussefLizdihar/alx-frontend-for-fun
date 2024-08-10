#!/usr/bin/python3
"""
a Python script that takes two arguments:
First argument is the name of the Markdown file
Second argument is the output file name
"""
import sys
import os.path
import re
import hashlib

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f'Missing {input_file}', file=sys.stderr)
        exit(1)

    with open(input_file, 'r') as read_file:
        with open(output_file, 'w') as html_file:
            unordered_start = False
            ordered_start = False
            paragraph = False

            for line in read_file:
                # Replace bold and italic syntax
                line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
                line = re.sub(r'__(.*?)__', r'<em>\1</em>', line)

                # Process MD5 hash
                md5_matches = re.findall(r'\[\[(.+?)\]\]', line)
                for match in md5_matches:
                    hashed = hashlib.md5(match.encode()).hexdigest()
                    line = line.replace(f'[[{match}]]', hashed)

                # Remove letter 'C'
                remove_c_matches = re.findall(r'\(\((.+?)\)\)', line)
                for match in remove_c_matches:
                    without_c = ''.join(c for c in match if c not in 'Cc')
                    line = line.replace(f'(({match}))', without_c)

                # Headings
                heading_match = re.match(r'^(#{1,6})\s+(.*)', line)
                if heading_match:
                    heading_level = len(heading_match.group(1))
                    heading_text = heading_match.group(2)
                    line = f'<h{heading_level}>{heading_text}</h{heading_level}>\n'

                # Unordered lists
                unordered_match = re.match(r'^-\s+(.*)', line)
                if unordered_match:
                    if not unordered_start:
                        html_file.write('<ul>\n')
                        unordered_start = True
                    line = f'<li>{unordered_match.group(1)}</li>\n'

                # Ordered lists
                ordered_match = re.match(r'^\*\s+(.*)', line)
                if ordered_match:
                    if not ordered_start:
                        html_file.write('<ol>\n')
                        ordered_start = True
                    line = f'<li>{ordered_match.group(1)}</li>\n'

                # Close lists if necessary
                if not unordered_match and unordered_start:
                    html_file.write('</ul>\n')
                    unordered_start = False

                if not ordered_match and ordered_start:
                    html_file.write('</ol>\n')
                    ordered_start = False

                # Paragraphs
                if not (heading_match or unordered_match or ordered_match):
                    if line.strip():
                        if not paragraph:
                            html_file.write('<p>\n')
                            paragraph = True
                        else:
                            html_file.write('<br/>\n')
                    else:
                        if paragraph:
                            html_file.write('</p>\n')
                            paragraph = False

                html_file.write(line)

            # Final closing tags
            if unordered_start:
                html_file.write('</ul>\n')
            if ordered_start:
                html_file.write('</ol>\n')
            if paragraph:
                html_file.write('</p>\n')

    exit(0)
