'''
--Task description--

Write a Python program to convert JSON data to Python object. 

Create validation scheme in separate file as well.

Create your own JSON data about your name, surname, address, keep it separately, 
import it to you python program file, check if schema validation is pass, parse json and print your name, surname and address

'''
import json
from schema_val import validate_json_data


def print_data(json_file):

    with open(json_file) as f:
        json_str = json.load(f)

    if validate_json_data(json_str):
        print(json_str['name'], json_str['surname'], json_str['address'])


print_data('my_data.json')
