''' 1.	Write a Python program which will open file, if not exist than create it.  Append the following text with two lines:
 Hello - first line
 It's my first file handling! - second line
 Read data from file and print in console. Don't forget and close it, use with block here.
 '''



import os

os.chdir("Lesson_8_Armine")

with open("my_new_document.txt", "w+", encoding="utf8") as doc: 
    print(doc.write("Hello\n"))
    print(doc.write("It's my first file handling!"))
    content = doc.read()
    
with open("my_new_document.txt", "r", encoding="utf8") as doc: 
    readonly = doc.read()
    print(readonly)



'''
2.	Write a Python program which will create directory with your name, 
switch to directory and generate there 26 text files named A.txt, B.txt, and so on up to Z.txt.
'''

import os
current=os.getcwd()
os.chdir(r"C:\Users\Public\automation_qwallity_06-24\Lesson_8_Armine")
os.mkdir("Armine")

os.chdir("Armine")
import string

def doccreator():
    print(string.ascii_uppercase)
    
    for char in string.ascii_uppercase:
        name1 = char + '.txt'
        with open(name1, 'a+', encoding='utf-8') as file1:
            f = file1
            print(f)

doccreator()


'''
3.	Write a Python program which will open file, add your name, 
surname and address to the file(keep there as dictionary).
'''


import os
os.chdir("Lesson_8_Armine")
import json

info = {"name": "Armine",
        "surname": "Barseghyan",
        "address": "Yerevan"}

with open("my_info.txt", mode ="w+",encoding="utf-8") as myinfo:
    myinfo.write(json.dumps(info))