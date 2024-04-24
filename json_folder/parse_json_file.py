# import jmespath
import json
from marshmallow import schema, validate, fields, ValidationError

from schema_validation import validate_schema

# Read JSON data from file
with open("my_info.json", "r") as file:
    json_data = json.load(file)
    print(type(json_data))

with open("second_my_info.json", "w+") as file2:
    json_data = json.dump(file2 , indent=4)

# Validate JSON schema
if not validate_schema(json_data):
    print("JSON validation failed.")
    exit()

# Parse and print information
name = json_data["name"]
lastname = json_data["lastname"]
address = json_data["address"]

print("Name:", name)
print("Lastname:", lastname)
print("Address:", address)

# Anna - general steps are correct, but this steps don't combined into one flow
# You should create one function, which will load from json file, check validation using marshmallow and if validaiton will pass print 
# Name, Lastname and Address

# I will add my solution to master branch, please have a look