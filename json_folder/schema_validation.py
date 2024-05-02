import json
from marshmallow import schema, validate, fields, validationError

def validate_schema(data):
    required_fields = {"name", "lastname", "address"}
    for field in required_fields:
        if field not in data:
            return False
    return True


# Anna - here you import marshmallow but didn't use it for validation :)