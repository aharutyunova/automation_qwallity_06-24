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

def config_file(file_path):
    file_path = "text_file.txt"
    config_data = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                match = re.match(r'^\s*([^\s=]+)\s*=\s*([^#]+)(?=\s*#|$)', line)
                key = match.group(1)
                value = match.group(2)
                config_data[key] = value
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except Exception as e:
         logging.error(f"An error occurred: {str(e)}")
    finally:
        logging.info("Config is completed")
        return config_data

if __name__ == "__main__":
    config_file_path = "text_file.txt"
    config_data = config_file(config_file_path)
    print(config_data)

