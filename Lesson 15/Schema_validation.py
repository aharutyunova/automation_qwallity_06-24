import json
from marshmallow import Schema, fields, ValidationError


class JsonSchema(Schema):
    name = fields.String(required=True)
    surname = fields.String(required=True)
    address = fields.String(required=True)
    number = fields.Integer()


json_data_raw = '''
{
    "name": "Izabella",
    "surname": "Mnatsakanian",
    "address": "Yerevan",
    "number": 12345
}
'''

json_data = json.loads(json_data_raw)
try:
    result = JsonSchema().load(json_data)
except ValidationError as x:
    print(x.messages)
else:
    print("Validated OK")
