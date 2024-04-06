import os

# 1. Write a Python class to reverse a string word by word.
# Input string : 'hello .py'.
# Expected Output : '.py hello'


class StringReverser:
    # I couldn't understand why "input_string" parameter is not accessed?
    def __init__(self, input_string=None):
        self.input_string = input("Enter a string and get it Reversed: ")
        self.reversed_string()

    def reversed_string(self):
        words = self.input_string.split()
        reversed_words = words[::-1]
        reversed_string = ' '.join(reversed_words)
        print("Reversed string:", reversed_string)


reverser = StringReverser()


# 2. Write a Python class which get any string and with methods print_String
# print this sting in upper case
class StringUpperCase:
    def __init__(self, input_string=None):
        self.input_string = input("Enter a string and get it Uppercased: ")
        self.print_String()

    def string_to_uppercase(self):
        up_str = self.input_string.upper()
        return up_str

    def print_String(self):
        print("Uppercased string:", self.string_to_uppercase())


uppercased_string = StringUpperCase()


# 3. Write a Python class to generate 26 text files named A.txt, B.txt,
# and so on up to Z.txt.
class GenerateFiles:
    def __init__(self):
        self.files_with_names_A_to_Z()

    def files_with_names_A_to_Z(self):
        self.file_name = ord("A")
        self.file_extension = ".txt"

        os.chdir("Lesson_10")
        os.mkdir("My_files")
        os.chdir("My_files")

        while self.file_name <= ord("Z"):
            full_file_name = chr(self.file_name) + self.file_extension
            with open(full_file_name, "w+"):
                pass
            self.file_name += 1
        return


generate_files = GenerateFiles()
