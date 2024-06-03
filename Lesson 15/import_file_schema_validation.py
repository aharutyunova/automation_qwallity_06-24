'''
import json
from marshmallow import Schema, validate, fields, ValidationError

class JsonSchema(Schema):
    name = fields.String(required=True)
    surname = fields.String(required=True)
    address = fields.String(required=True)
    number = fields.Integer()


with open("json_file.json", 'r', ) as f:
    json_data = json.load(f)

name = json_data.get("name")
surname = json_data.get("surname")
address = json_data.get("address")
number = json_data.get("number")
print(f"name: {name}\nsurname: {surname}\naddress: {address}\nnumber: {number}")

try:
    result = JsonSchema().load(json_data)
except ValidationError as x:
    print(x.messages)
else:
    print("Validation passed")


# Anna - General logic and technices are correct, only there is a bit mess, I didn't find one file or method which was final
# For example you could complete all logic in this one file
# check validation and if validation will pass in else block write all thise code
"""name = json_data.get("name")
surname = json_data.get("surname")
address = json_data.get("address")
number = json_data.get("number")
print(f"name: {name}\nsurname: {surname}\naddress: {address}\nnumber: {number}")"""

# Anyway despite the comments, the general logic is good enougth :)
'''

import json
from marshmallow import Schema, fields, ValidationError


class JsonSchema(Schema):
    name = fields.String(required=True)
    surname = fields.String(required=True)
    address = fields.String(required=True)
    number = fields.Integer()


with open("json_file.json", 'r', ) as f:
    json_data = json.load(f)
# or json_data = json.loads(json_data_raw)
# delete one key with value from json_file and get ValidationError
try:
    result = JsonSchema().load(json_data)
    print("Validation passed.")
    # If validation passes, print the parsed data
    name = json_data.get("name")
    surname = json_data.get("surname")
    address = json_data.get("address")
    number = json_data.get("number")
    print(f"Name: {name}\nSurname: {surname}\nAddress: {address}\nNumber: {number}")
except ValidationError as x:
    print("Validation failed.")
    print(x.messages)

# Anna jan is this solution ok?