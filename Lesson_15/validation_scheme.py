import json
from marshmallow import Schema, fields, ValidationError


class MyDataSchema(Schema):
    name = fields.String(required=True)
    surname = fields.String(required=True)
    address = fields.String(required=True)


data_str = '''
{
    "name": "Anna",
    "surname": "Avtandilyan",
    "address": "Shirazi 36"
}
'''

json_data = json.loads(data_str)
try:
    result = MyDataSchema().load(json_data)
except ValidationError as x:
    print(x.messages)
else:
    print("Validation Pass")
