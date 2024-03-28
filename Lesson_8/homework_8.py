''' 1.	Write a Python program which will open file, if not exist than create it.  Append the following text with two lines:
 Hello - first line
 It's my first file handling! - second line
 Read data from file and print in console. Don't forget and close it, use with block here.
 '''


f = open("test.txt","w+", encoding = "utf8")
f.write("Hello")
f.write("\nIt's my first file handling!")
f.close()

f = open("test.txt", "r")
print(f.read())
f.close()

'''
2.	Write a Python program which will create directory with your name, 
switch to directory and generate there 26 text files named A.txt, B.txt, and so on up to Z.txt.
'''
from string import ascii_lowercase
import os
os.mkdir("juli")
os.chdir("juli")

for i in ascii_lowercase:
    with open(i + ".txt", "w+",encoding="utf8") as f:
        f.write("")

'''
3.	Write a Python program which will open file, add your name, 
surname and address to the file(keep there as dictionary).
'''
info_about_me = {
    "name":"Juliet",
    "surname":"Revazyan",
    "address":"Anywhere"

}
with open("Info_about_me.txt", "w+", encoding="utf8" ) as f:
    f.write(str(info_about_me))



