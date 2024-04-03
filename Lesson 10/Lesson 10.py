import os
import string


# 1. Write a Python class to reverse a string word by word. Input string : 'hello .py'.
# Expected Output : '.py hello'

class StringReverser:

    @staticmethod
    def reverse_words(word: str) -> str:
        words = word.split()
        reversed_string = ' '.join(reversed(words))
        return reversed_string


input_string = input("Please type some words with space separated: ")
reverser = StringReverser()
output_string = reverser.reverse_words(input_string)

print(output_string)

# Anna - will be better to pass variable with __init__ method and use instance method not staic
# Functionality is correct



# 2. Write a Python class which get any string and with methods print_String print this sting in upper case


class StringToUpperCase:

    @staticmethod
    def uppercase_words(word: str) -> str:
        word = word.upper()
        return word


input_string = input("Please type any word: ")
to_uppercase = StringToUpperCase()
output_string = to_uppercase.uppercase_words(input_string)

print(output_string)
# Anna - the same comment as for task 1

# 3. Write a Python class to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.


class TextFileGenerator:
    @staticmethod
    def generate_files():
        os.mkdir("a_z")
        os.chdir("a_z")
        for char in list(string.ascii_uppercase):
            file_name = f'{char}.txt'
            open(file_name, 'x')


generator = TextFileGenerator()
generator.generate_files()
# Anna - And the same is here :) 
# Anna - Try to use static method in exeptional cases not as a rule
