''' 1.	Write a Python program which will open file, if not exist than create it.  
 Append the following text with two lines:
 Hello - first line
 It's my first file handling! - second line
 Read data from file and print in console. Don't forget and close it, use with block here.
 '''
import os
os.chdir('Lesson_8')
path = os.getcwd() #keep it for task 3
lines_arr = ["Hello \n","It's my first file handling! \n"]
with open('task8.txt', "w+", encoding='utf-8') as f:
    f.writelines(lines_arr)
    f.seek(0)
    print(f.read())

'''
2.	Write a Python program which will create directory with your name, 
switch to directory and generate there 26 text files named A.txt, B.txt, and so on up to Z.txt.
'''
os.mkdir('Raya')
os.chdir('Raya')
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for element in range(0, len(alphabet)):
    file_name = alphabet[element] + '.txt'
    f = open(file_name, 'w+', encoding = 'utf-8')
    f.close()

'''
3.	Write a Python program which will open file, add your name, 
surname and address to the file(keep there as dictionary).
'''
import json
os.chdir(path)
my_data = { "name": "Raya", "surname" : "Manukyan", "address": "Qasakh"}
with open('my_data.txt', 'w+', encoding = 'utf-8') as f:
    f.writelines(json.dumps(my_data))
