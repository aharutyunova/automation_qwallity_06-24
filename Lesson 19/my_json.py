import json
from schema_validation import validate

'''
file_path = 'data.json'


def append_to_json(data):
    validation = False
    if validate(data):
        validation = True
    try:
        with open(file_path, 'a') as f:
            json.dump(data, f, indent=4)
            f.write('\n')
    except Exception as e:
        print(f"Error: {e}")

'''

import json
from schema_validation import validate

file_path = 'data.json'

def append_to_json(data):
    validation = False
    if validate(data):
        validation = True
    try:
        existing_data = []
        try:
            with open(file_path, 'r') as file:
                existing_data = json.load(file)  # Load existing data from the file
        except FileNotFoundError:
            pass

        existing_data.append(data)  # Append new data to the list

        with open(file_path, 'w') as f:  # Open the file in write mode
            json.dump(existing_data, f, indent=4)  # Dump the list to the file as JSON
            f.write('\n')  # Add a newline after each JSON object

    except Exception as e:
        print(f"Error: {e}")


