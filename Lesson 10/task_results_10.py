# 1. Write a Python class to reverse a string word by word. Input string : 'hello .py'. 
# Expected Output : '.py hello'

class StringReverser:
    def reverse_words(self, input_string):
        text = input_string.split()
        reversed_string = ''.join(reversed(text))
        return reversed_string
    
input_string = 'hello. py'
reverser = StringReverser()
output_string = reverser.reverse_words(input_string)
print(output_string)

# Anna - generally correct. You could also give input_string variable in def__init__()
#  And one more note, in case you want reverse letters in the word you solution is correct
#  In case you want to write sentence from last word to first you should write
"""input_string = 'text1 text2'
text = input_string.split(' ')
print(text[::-1])"""


# 2. Write a Python class which get any string and with methods print_String print this sting in upper case 


class StringUppercase:
    def __init__(self, input_string):
        self.input_string = input_string

input_str = "Hello everyone!"
print_string = input_string.upper()
manipulator = StringUppercase(input_str)
print(input_str)
   
# Anna - In your example StringUppercase class doesn't do anything
# Your class should have print_upper_case method which will convert string to upper case and print it
#  for example
"""
class StringUppercase:
    def __init__(self, input_string):
        self.input_string = input_string

    def print_uppercase(self):
        upper_case_str = self.input_string.upper()
        print(upper_case_str)
    
"""
# Then you will create objet of class and call class's method
# my_obj = StringUppercase("Any String")
# my_obj.print_uppercase()
        
# 3. Write a Python class to generate 26 text files named A.txt, B.txt, and so on up to Z.txt. 

import os

class My_files:
    def __init__(self) -> None:
        pass

my_directory = "Shushanik"
os.mkdir(my_directory)
os.chdir(my_directory)

for f in range(26):
    letter = chr(ord('A')+ f)
    file_name = letter + ".txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"Content of {file_name}\n") 
     
# Anna - In this example also you write logic of creation directory and files out of the class
# Here you also should have method inside the class, which will contains all logic you have out of the class
# os.chdir("..")