import os

'''
1. Write a Python program which will open file, if not exist than create it.
Append the following text with two lines:
Hello - first line
It's my first file handling! - second line
Read data from file and print in console. Don't forget and close it, use with block here.
'''

# Anna example of path files = os.getcwd()

# files = os.getcwd()
# file_name = "test_text.txt"
# full_path = os.path.join(files, file_name)
# print(full_path)
#
#
# def write_hello_in_file(input_file):
#     str_list = ["Hello", "It's my first file handling!"]
#     if input_file:
#         with open(input_file, "a") as file:
#
#             for str_item in str_list:
#                 file.write(str_item + "\n")
#
#
# write_hello_in_file(full_path)

# Anna -  the logic and function are correct, only file path is hard coded and 
# from my side didn't work, so try use some universal path, like getcwd() and build full path based on getcwd()

'''
2. Write a Python program which will create directory with your name, 
switch to directory and generate there 26 text files named 
A.txt, B.txt, and so on up to Z.txt.
'''

# main_file_path = os.getcwd()

# def alphabetic_files_generator(input_path):
#     new_directory = "alphabetic_text_files"
#     file_format = ".txt"
#     new_directory_path = os.path.join(input_path, new_directory)
#
#     if not os.path.exists(new_directory_path):
#         os.mkdir(new_directory_path)
#
#     for char in range(ord("A"), ord("Z") + 1):
#         file_path = os.path.join(new_directory_path, chr(char) + file_format)
#         with open(file_path, "w") as file:
#             file.write(chr(char))
#
#
# alphabetic_files_generator(main_file_path)

# Anna - Good solution, again same note for main_file_path, should not be hardcoded

'''
3. Write a Python program which will open file, add your name, 
surname and address to the file (keep there as dictionary).
'''

# files = os.getcwd()
# user_file_name = "user_credentials.py"
# user_full_path = os.path.join(files, user_file_name)


# def write_user_credential_in_file(input_file):
#     ask_for_name = input("(User) Enter your name: ")
#     ask_for_surname = input("(User) Enter your surname: ")
#     ask_for_address = input("(User) Enter your address: ")
#
#     user = {
#         "name": ask_for_name,
#         "surname": ask_for_surname,
#         "address": ask_for_address,
#     }
#
#     with open(input_file, "w") as file:
#         file.write(str(user))
#
#
# write_user_credential_in_file(user_full_path)

# Anna - we didn't discuss json.dumps method yet, solution and way of writing json is correct :)

# If we skip hardcoded paths all 3 tasks solved in very good way!!!
