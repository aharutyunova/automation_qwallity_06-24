import json
from marshmallow import ValidationError


def validate_response(response):
    try:
        validated_data = json.load(response[0])
        return validated_data
    except ValidationError as e:
        print("Schema validation failed:", e.messages)
        return None


def write_to_file(data, filename):
    with open(filename, 'w') as f:
        json(data, f,)