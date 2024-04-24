'''
--Task description--

Write a Python program to convert JSON data to Python object.

Create validation scheme in separate file as well.

Create your own JSON data about your name, surname, address, keep it separately,
import it to you python program file, check if schema validation is pass, parse json
and print your name, surname and address
'''

import json

json_data_raw = """{
        "name": "Mariam",
        "surname": "Galoyan",
        "address": "Yerevan",
        "number": 12345
}"""

json_data = json.loads(json_data_raw)
print(json_data)
print(type(json_data))

# Anna - Mariam jan this part of code and part with schema validation are correct
# End to End flow of requirement didn't covered, but what you wrote is correct