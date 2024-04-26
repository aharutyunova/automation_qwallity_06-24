"""
Create a simple config file parser.
Config file has the following syntax:
Comments begin with # (may be in the beginning of the line or in the middle of the line.
Blank lines are allowed.
Format of string is key = value
Spaces are allowed around assignment. 

Expected output: The data must be loaded into dictionary.
NOTE: Use logging in solution

# Example of config file: 

# This is a comment
Width = 4 # box width
   Height = 3
Length = 6


# Resulting dictionary should be:

{
    "Width": 4,
    "Height": 3,
    "Length": 6
}
"""
import re
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='my_log.log',
                    filemode='w+',
                    encoding='utf-8')


try:
    new_dict = {}
    with open("config.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            match = re.match(r'\s*([^#][\w\s]+)\s*=\s*([^#]+)', line)
            if match:
                key = match.group(1).strip()
                value = match.group(2).strip()
                new_dict[key] = value
    print("New dictionary will be:", new_dict)

except Exception as e:
    logging.error(f"Error occurred: {e}")
