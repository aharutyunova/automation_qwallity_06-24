# 1. Write a Python class to reverse a string word by word. Input string :
# 'hello .py'.
# Expected Output : '.py hello'

# class ReverseString:
#     def __init__(self, my_string):
#         self.my_string = my_string

#     def my_function(self):
#         split_string = self.my_string.split()
#         new_string = ' '.join(reversed(split_string))
#         print(new_string)


# my_string_1 = ReverseString("hello .py")
# my_string_1.my_function()

# my_string_2 = ReverseString("Good By")
# my_string_2.my_function()

# 2. Write a Python class which get any string and with methods
# print_String print this sting in upper case

# class Uppercase:
#     def __init__(self, my_string):
#         self.my_string = my_string

#     def print_String(self):
#         print(self.my_string.upper())


# my_string_1 = Uppercase("test")
# my_string_1.print_String()

# my_string_2 = Uppercase("hello world")
# my_string_2.print_String()

# my_string_3 = Uppercase(input("Enter any string: "))
# my_string_3.print_String()


# 3. Write a Python class to generate 26 text files named A.txt, B.txt,
# and so on up to Z.txt.

# import os
# dir_name = "New Folder"
# os.mkdir(dir_name)
# os.chdir(dir_name)


# class GenerateFiles:
#     def CreateFiles(self):
#         for i in range(65, 91):
#             file_name = chr(i) + ".txt"
#             with open(file_name, "w") as f:
#                 f.write("This is a file")


# print("Directory created:")

# file_generator = GenerateFiles()
# file_generator.CreateFiles()
