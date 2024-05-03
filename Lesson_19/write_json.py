import json
from validate import validate

file_path = 'data.json'


def write_json(data: list[dict]):
    if_validation_pass = False
    if validate(data):
        if_validation_pass = True

    if if_validation_pass:
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Error {e}")