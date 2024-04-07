import os
import string
""" 
1.Write a Python program which will open file, if not exist than create it. 
Append the following text with two lines:
Hello - first line
It's my first file handling! - second line
Read data from file and print in console. Don't forget and close it, use with block here.
"""

texts_list = ["Hello", "It's my first file handling!"]

with open("Lesson_8.csv", "w") as file:
    for text in texts_list:
        file.write(f'{text}\n')

with open("Lesson_8.csv", "r") as file:
    print(file.read())

# Anna - correct
"""
2.	Write a Python program which will create directory with your name, 
switch to directory and generate there 26 text files named A.txt, B.txt, and so on up to Z.txt.
"""


def create_directory(arg):
    os.mkdir(arg)
    os.chdir(arg)


name = input("Please write your name: ")
create_directory(name)

alphabet = list(string.ascii_uppercase)

for char in alphabet:
    open(f"{char}.txt", "x")

# Anna - correct
"""
3.	Write a Python program which will open file, add your name, 
surname and address to the file(keep there as dictionary).
"""

name = input("Write your name: ")
surname = input("Write your surname: ")
address = input("Write your address: ")

info_dict = {
    "name": name,
    "surname": surname,
    "address": address
}

with open("info_file.csv", "w+") as file:
    file.write(str(info_dict))

with open("info_file.csv", "r") as file:
    print(file.read())

# Anna - correct
# In case you have no need to write in csv you could write in txt file
# In case to write in csv file use csv lib, to keep csv format when inserting data
