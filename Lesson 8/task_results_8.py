''' 1.	Write a Python program which will open file, if not exist than create it.  Append the following text with two lines:
 Hello - first line
 It's my first file handling! - second line
 Read data from file and print in console. Don't forget and close it, use with block here.
 '''

with open(r"C:\automation_qwallity_06-24\Lesson 8\my_file.txt", "w+", encoding="utf-8") as text:
    text.write("Hello - first line\n")
    text.write("It's my first file handling! - second line\n")

'''
2.	Write a Python program which will create directory with your name, 
switch to directory and generate there 26 text files named A.txt, B.txt, and so on up to Z.txt.
'''

import os

my_directory = "Shushan"
os.mkdir(my_directory)
os.chdir(my_directory)

for f in range(26):
    letter = chr(ord('A')+ f)
    file_name = letter + ".txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"Content of {file_name}\n") 


os.chdir("..")


'''
3.	Write a Python program which will open file, add your name, 
surname and address to the file(keep there as dictionary).
'''
    
my_info = {
    "name": "Shushan",
    "surname": "Petrosyan",
    "address": "Village Merdzavan"
}

with open(r"C:\automation_qwallity_06-24\Lesson 8\Shushan_file.txt", "w+", encoding="utf-8") as text:
    text.write(str(my_info))
    text.write("\n")
