# 1. Write a Python class to reverse a string word by word. Input string : 'hello .py'. 
# Expected Output : '.py hello'

class Wordchanges:
    def __init__(self, example):
        self.example = example

    def reversing(self):
        example = ''.join(reversed(self.example.split()))
        print(example)


new = Wordchanges("Hello py.")
new.reversing()


# Write a Python class which get any string and with methods print_String print this sting in upper case 

class UpperCaseString:
    def __init__(self):
        self.input_string = " Hello Mariam"

    def get_string(self, input_string):
        self.input_string = input_string
        input_string = "Hello Mariam"
    
    def print_string(self):
        print(self.input_string.upper())

