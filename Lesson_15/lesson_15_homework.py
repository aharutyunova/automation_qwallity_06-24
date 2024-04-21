# --Task description--

# Write a Python program to convert JSON data to Python object. 

import json
import os
os.chdir("c:/automation_qwallity_06-24/Lesson_15")
def python_object():
    with open("data.json", 'r+') as f:
        result = f.read()
        new_result = json.loads(result)
        return new_result

x = python_object()
print(x)

# Create validation scheme in separate file as well.

import json
from marshmallow import Schema, validate, fields, ValidationError

new_data = '''{ 
    "name": "James",
    "surname": "Bond",
    "age": 56,
    "rich":"Barev"
}'''

class ExpectedSchema(Schema):
    name = fields.String(required=True)
    surname = fields.String(required=True)
    age = fields.Integer(required=True)
    rich = fields.String(validate=validate.OneOf(['Yes','No']))


json_data = json.loads(new_data)

try:
    result = ExpectedSchema().load(json_data)
except ValidationError as error:
    print(error.messages)
else:
    print("Everything is OK")

# Create your own JSON data about your name, surname, address, keep it separately, 
# import it to you python program file, check if schema validation is pass, parse json and print your name, surname and address
import json
from marshmallow import Schema, validate, fields, ValidationError
import os
os.chdir("c:/automation_qwallity_06-24/Lesson_15")
class ExpectedSchema(Schema):
    name = fields.String(required=True)
    surname = fields.String(required=True)
    address = fields.String(required=True)

with open("my_data.json", 'r+') as f:
    result = f.read()
    parsedJson = json.loads(result)
    try:
        ExpectedSchema().load(parsedJson)
        print(parsedJson.values())
    except ValidationError as error:
        print(error.messages)

  
    






   