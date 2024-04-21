import json
from validation_scheme import json_data
from validation_scheme import result


with open("json_data.json", "r+") as f:
    res = f.read()
    new_res = json.loads(res)
    print(new_res)
    print(type(new_res))


is_valid = result

if is_valid:
    name = json_data['name']
    surname = json_data['surname']
    address = json_data['address']
    print("Name:", name)
    print("Surname:", surname)
    print("Address:", address)
else:
    print("Validation failed:")



'''
--Task description--

Write a Python program to convert JSON data to Python object. 

Create validation scheme in separate file as well.+

Create your own JSON data about your name, surname, address, keep it separately, +
import it to you python program file, check if schema validation is pass, parse json and print your name, surname and address

'''
