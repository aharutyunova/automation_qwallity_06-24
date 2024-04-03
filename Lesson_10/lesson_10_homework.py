# 1. Write a Python class to reverse a string word by word. Input string : 'hello .py'. 
# Expected Output : '.py hello'
from string import ascii_uppercase
import os


class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_words(self):
        # Split the input string into words
        words = self.input_string.split()

        # Reverse the list of words
        reversed_words = words[::-1]

        # Join the reversed words back into a string 
        reversed_string = ' '.join(reversed_words)

        return reversed_string


input_string = 'hello .py'
reverser = StringReverser(input_string)
output_string = reverser.reverse_words()
# print("Input string:", input_string)
print("Reversed string:", output_string)


# 2. Write a Python class which get any string and with methods print_String print this sting in upper case 

class GetString():
    def __init__(self, input_string):
        self.input_string = input_string

    def get_String(self):
        self.input_string = input("Enter a string: ")

    def print_String(self):
        print(self.input_string.upper())


input_string = GetString("")
input_string.get_String()
input_string.print_String()


# 3. Write a Python class to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.

directory_name = "26_text_files"
os.mkdir(directory_name)


class Text_File_Generate():

    def generate_files(self, file):
        os.chdir(directory_name)
        for letter in ascii_uppercase:
            with open(f"{letter}.txt", "w+", encoding="utf-8") as file:
                file.write("")


file_generator = Text_File_Generate()
file_generator.generate_files(directory_name)
