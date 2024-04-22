import json

from marshmallow import Schema, fields, ValidationError


class PersonSchema(Schema):
    name = fields.String(required=True)
    surname = fields.String(required=True)
    address = fields.String(required=True)


my_data = {
    "name": "Anush",
    "surname": "Hayrapetyan",
    "address": "Abovyan, Eritasardakan 8"
}


try:
    result = PersonSchema().load(my_data)  
    print("Name:", result["name"])  
    print("Surname:", result["surname"])
    print("Address:", result["address"])
except ValidationError as e:
    print("Validation errors:", e.messages)
else:
    print("Validated Ok")