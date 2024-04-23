'''
--Task description--

Write a Python program to convert JSON data to Python object.

Create validation scheme in separate file as well.

Create your own JSON data about your name, surname, address, keep it separately,
import it to you python program file, check if schema validation is pass, parse json
and print your name, surname and address
'''

import json
from marshmallow import Schema, fields, ValidationError


class JsonSchema(Schema):
    name = fields.String(required=True)
    surname = fields.String(required=True)
    address = fields.String(required=True)
    number = fields.Integer()


json_data_raw = '''
{
    "name": "Mariam",
    "surname": "Galoyan",
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