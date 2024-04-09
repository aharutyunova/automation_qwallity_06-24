# 1. Write a Python class to reverse a string word by word. Input string : 'hello .py'. 
# Expected Output : '.py hello'

class StringReverser:
    def reverse_words(self, input_string):
        text = input_string.split()
        reversed_string = ''.join(reversed(text))
        return reversed_string
    
input_string = 'hello .py'
reverser = StringReverser()
output_string = reverser.reverse_words(input_string)
print(output_string)


# 2. Write a Python class which get any string and with methods print_String print this sting in upper case 


class StringUppercase:
    def __init__(self, input_string):
        self.input_string = input_string

input_str = "Hello everyone!"
print_string = input_string.upper()
manipulator = StringUppercase(input_str)
print(input_str)
   
        
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
     
     
os.chdir("..")