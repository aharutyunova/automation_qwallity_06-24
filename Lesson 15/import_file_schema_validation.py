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
    print("Validated OK")


# Anna - General logic and technices are correct, only there is a bit mess, I didn't find one file or method which was final
# For example you could complete all logic in this one file
# check validation and if validation will pass in else block write all thise code
"""name = json_data.get("name")
surname = json_data.get("surname")
address = json_data.get("address")
number = json_data.get("number")
print(f"name: {name}\nsurname: {surname}\naddress: {address}\nnumber: {number}")"""

# Anyway despite the comments, the general logic is good enougth :)