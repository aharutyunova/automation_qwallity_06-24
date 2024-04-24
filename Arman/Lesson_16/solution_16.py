"""
Create a simple config file parser.

Config file has the following syntax:

Comments begin with # (may be in the beginning of the line or in the middle of the line.

Blank lines are allowed.

Format of string is key = value

Spaces are allowed around assignment.

Expected output: The data must be loaded into dictionary.

NOTE: Use logging in solution
"""
import json
import logging
import os
import re

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='app.log',
    filemode='w+',
    encoding='utf-8'
)


def extract_dimensions_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            width_match = re.search(r'Width\s*=\s*(\d+)', data, re.IGNORECASE)
            height_match = re.search(r'Height\s*=\s*(\d+)', data, re.IGNORECASE)
            length_match = re.search(r'Length\s*=\s*(\d+)', data, re.IGNORECASE)
            if width_match and height_match and length_match:
                width = int(width_match.group(1))
                height = int(height_match.group(1))
                length = int(length_match.group(1))
                dimension = {"Width": width, "Height": height, "Length": length}
                logging.info(f"Dimensions extracted: {dimension}")
                return dimension
            else:
                logging.error("Failed to extract dimensions from file.")
                return None
    except Exception as e:
        logging.error(f"Error reading file: {e}")
        return None


current_directory = os.getcwd()
configuration_file = 'config_file.py'
full_file_path = os.path.join(current_directory, configuration_file)
dimensions = extract_dimensions_from_file(configuration_file)
if dimensions:
    print(json.dumps(dimensions, indent=4))


# Anna, correct solution, but a bit difficult
# You could get values with easier way
# With this pattern
"""
pattern = (r'\w+\s\=\s\d+')
res = re.findall(pattern, a)
"""
