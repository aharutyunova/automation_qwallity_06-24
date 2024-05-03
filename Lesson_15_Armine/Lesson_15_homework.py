'''
--Task description--

Write a Python program to convert JSON data to Python object. 

Create validation scheme in separate file as well.

Create your own JSON data about your name, surname, address, keep it separately, 
import it to you python program file, check if schema validation is pass, parse json and print your name, surname and address

'''
import json
from valid_scheme import text_validation_funct


def print_data():

    with open(r'C:\Users\Արմինա\automation_qwallity_06-24\Lesson_15_Armine\myexample.json') as ex:
        js_file = json.load(ex)
    
    if text_validation_funct(js_file):
        print(js_file['name'], js_file['surname'], js_file['address'], js_file['phone'])

   
print_data()


     #Dear Anna, I did this following your solution, but nothing returns when I run the code, I cannot find what is incorrect in my code(

# Anna - didn't call the function, that's why you didn't see result (Added line 25)
    
print_data()