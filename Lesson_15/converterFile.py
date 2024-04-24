'''
--Task description--

Write a Python program to convert JSON data to Python object. 

Create validation scheme in separate file as well.

Create your own JSON data about your name, surname, address, keep it separately, 
import it to you python program file, check if schema validation is pass, parse json and print your name, surname and address

'''
import os
import json
def converter(filename, partpath):
    full_path = os.path.join(os.getcwd(),partpath)
    os.chdir(full_path)
    
    with open(filename, 'r') as f:
        result = json.load(f)
    return result


