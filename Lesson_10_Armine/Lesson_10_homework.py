
# 1. Write a Python class to reverse a string word by word. Input string : 'hello .py'. 
# Expected Output : '.py hello'

class Wordchanges:
    def __init__(self, example):
        self.example = example

    def reversing_fun(self):
        example = ''.join(reversed(self.example.split()))
        print(example)


new = Wordchanges("Hello py.")
new.reversing_fun()

# Anna - correct


# 2. Write a Python class which get any string and with methods print_String print this sting in upper case 

class Uppercaseword:
    def __init__(self, str):
        self.str = str

    def upper_case_fun(self):
        print(self.str.upper())


my_word = Uppercaseword("My name is Armine")
my_word.upper_case_fun()

# Anna - correct

# 3. Write a Python class to generate 26 text files named A.txt, B.txt, and so on up to Z.txt. 

import os

import string


class TestCreator:
    def __init__(self):
        pass     # Anna - in case you don't need pass something in __init__, you can skip it and don't write in the class

    def doc_creator(self):
        current = os.getcwd()
        os.chdir(r"C:\Users\Public\automation_qwallity_06-24\Lesson_10_Armine")
        os.mkdir("Textfiles")
        os.chdir("Textfiles")
        print(string.ascii_uppercase)

    for char in string.ascii_uppercase:
        name1 = char + '.txt'
        with open(name1, 'a+', encoding='utf-8') as file1:
          f = file1
          print(f) 





# Anna - path is hardcoded
# You could move to the folder in the same - doc_creator method
# The other logic is correct
# Also note - Code style is improved :)

new_file = TestCreator()
new_file.doc_creator()
