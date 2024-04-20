"""
--Task description--

1. Write a Python program to convert JSON data to Python object.

2. Create validation scheme in separate file as well.

3. Create your own JSON data about your name, surname, address, keep it separately,

4. import it to you python program file, check if schema validation is pass, parse json and print your name, surname and address

"""
import json

from my_dictionary import my_data
from validation_schema import ValidationSchema, MyDataValidation

# 1. Write a Python program to convert JSON data to Python object.

test_user = '''{
    "name": "John",
    "surname": "Doe",
    "age": 30
}
'''

user_dict = {
    "name": "John",
    "surname": "Doe",
    "age": 25
}
# Anna - You don't need to have user_dict separately, you get it when loads from json string

def from_json_to_object(input_data):
    py_object = {}
    if isinstance(input_data, str):
        try:
            py_object = json.loads(input_data) # Anna - you should return py_object in try or else block, becasue in case of exception you will have no object to return
        except json.JSONDecodeError as error:
            print(error)
        return py_object
    else:
        return "Variable datatype should be JSON to convert to Python object"


print(from_json_to_object(test_user))

# 2. Create validation scheme in separate file as well.

validation_schema = ValidationSchema()
validate_user = validation_schema.validate(user_dict)
print(validate_user)

# 3. Create your own JSON data about your name, surname, address, keep it separately

# From my_dictionary .py file my object data
my_str_data = my_data

# Try to convert my data from string JSON to Python object
my_dict_data = from_json_to_object(my_str_data)

# Create instance of my custom data validation
my_data_validation = MyDataValidation()

# Check my dictionary data schema validation
check_my_data_schema = my_data_validation.validate(my_dict_data)

# Anna - general technices are used but you didn't use everything as a parts of same flow.
# Look you should write one function which will get your json string, will check if json format pass validation, print name, surname, address values

# You separately checked validation, print data, but didn't get everything as an end to end flow