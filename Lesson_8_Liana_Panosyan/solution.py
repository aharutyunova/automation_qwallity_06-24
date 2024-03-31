''' 1.	Write a Python program which will open file,
if not exist than create it.
Append the following text with two lines:
Hello - first line
It's my first file handling! - second line
Read data from file and print in console.
Don't forget and close it, use with block here.
 '''

# with open('new_file.txt', 'a+') as f:
#     f.write("Hello\n")
#     f.write("It's my first file handling!\n")
#     f.seek(0)
#     read_data = f.read()
#     print(read_data)

# Anna - very good

'''
2.	Write a Python program which will create directory with your name,
switch to directory and generate there 26 text files
named A.txt, B.txt, and so on up to Z.txt.
'''
# import os
# dir_name = "Liana"
# os.mkdir(dir_name)
# os.chdir(dir_name)
# for i in range(65, 91):
#     file_name = chr(i) + ".txt"
#     with open(file_name, "w") as f:
#         f.write("This is a file")
# print("Directory created:")

# Anna - correct, very good

'''
3.	Write a Python program which will open file, add your name,
surname and address to the file(keep there as dictionary).
'''

my_dict = {"name": "Liana", "surname": "Panosyan",
           "address": "Metsamor city, 2nd building, 23 apartments"}
with open("my_file.txt", "a") as f:
    f.write(str(my_dict) + '\n')
print("My personal information has been added to the newly created file.")

# Anna - correct

# Very good as usual :)