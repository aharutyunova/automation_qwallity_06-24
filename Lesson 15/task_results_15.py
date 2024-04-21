

"""Write a Python program to convert JSON data to Python object. """

import json

try:
    with open(r"C:\automation_qwallity_06-24\Lesson 15\my_example.json", "r") as f:
        json_data = f.read() 
        python_object = json.loads(json_data)  
    print(python_object)
except FileNotFoundError:
    print("Error: The specified file 'my_example.json' does not exist.")


"""Create validation scheme in separate file as well."""

from validation_scheme import Validate_data

try:
    with open(r"C:\automation_qwallity_06-24\Lesson 15\my_example.json", "r") as f:
        json_data = f.read() 
        python_object = json.loads(json_data) 

    print(python_object)

except FileNotFoundError:
    print("Error: The specified file 'my_example.json' does not exist.")



"""Create your own JSON data about your name, surname, address, keep it separately, 
import it to you python program file, check if schema validation is pass, parse json and print your name, surname and address"""

from validation_scheme import Validate_data

try:
    with open(r"C:\automation_qwallity_06-24\Lesson 15\my_file.json", "r") as f:
        json_data = f.read() 
        python_object = json.loads(json_data) 

    print(python_object)

except FileNotFoundError:
    print("Error: The specified file 'my_file.json' does not exist.")