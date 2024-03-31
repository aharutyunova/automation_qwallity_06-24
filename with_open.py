''' 1.	Write a Python program which will open file, if not exist than create it.  Append the following text with two lines:
 Hello - first line
 It's my first file handling! - second line
 Read data from file and print in console. Don't forget and close it, use with block here.
 '''

a = "Hello"
b = "It's my first file handling!"

with open("file.txt", "a+", encoding="utf8") as f:
    f.write(f"{a}\n")
    f.write(f"{b}\n")
    f.seek(0)
    
    data = f.read()
    print(data)

'''
2.	Write a Python program which will create directory with your name, 
switch to directory and generate there 26 text files named A.txt, B.txt, and so on up to Z.txt.
'''


import os

def create_26_files(directory):
    cur_dir = os.getcwd()
    print(cur_dir)
    os.makedirs(directory, exist_ok=True)
    os.chdir(directory)

    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        filename = letter + '.txt'
        with open(filename, 'w') as file:
            file.write(f"This is file {filename}\n")

        print(f"File {filename} created.")

# os.chdir(cur_dir)
# os.rdir(directory)

create_26_files("Lianna")




'''
3.	Write a Python program which will open file, add your name, 
surname and address to the file(keep there as dictionary).
'''
def add_info_to_file(filename, info):
    with open(filename, 'a') as file:
        file.write(str(info) + '\n')

    # with open(filename, 'r') as file:
    #     file.write(str(info) + '\n')

info = {
    "name": "Lianna",
    "surname": "Balasanyan",
    "address": "Yerevan, Armenia"
}

add_info_to_file("my_info.txt", info)
print(info)