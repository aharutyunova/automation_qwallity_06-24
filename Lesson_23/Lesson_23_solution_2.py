import os
import json


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = "xPath_list.json"
FILE_PATH = os.path.join(CURRENT_DIR, FILENAME)

try:
    with open(FILE_PATH, 'r') as f:
        xPath = json.load(f)

        print(xPath)

        coount = 0
        for lines in xPath:
            coount += 1
        print(coount)
except FileNotFoundError:
    print(f"Error: '{FILENAME}' not found")
except json.JSONDecodeError:
    print(f"Error: Invalid JSON format in '{FILENAME}'")
