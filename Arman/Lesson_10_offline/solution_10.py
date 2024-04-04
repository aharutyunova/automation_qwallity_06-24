# 1. Write a Python class to reverse a string word by word. Input string : 'hello .py'.
# Expected Output : '.py hello'
# 2. Write a Python class which get any string and with methods print_String print this sting in upper case
# 3. Write a Python class to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.

class CustomString:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_string(self):
        return self.input_string[::-1]

    def print_upper_case(self):
        return self.input_string.upper()

    @staticmethod
    def generate_a_to_z(input_format):
        char_list = []
        for char in range(ord("A"), ord("Z") + 1):
            char_list.append(chr(char) + input_format)
        return char_list


not_reversed_string = CustomString("python.py")
lower_case_string = CustomString("test")
file_format = CustomString(".txt")

print(not_reversed_string.reverse_string())
print(lower_case_string.print_upper_case())
print(file_format.generate_a_to_z(".txt"))
