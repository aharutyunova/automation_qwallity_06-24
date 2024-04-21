import json

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
