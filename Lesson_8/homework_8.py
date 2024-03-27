''' 1.	Write a Python program which will open file, if not exist than create it.  Append the following text with two lines:
 Hello - first line
 It's my first file handling! - second line
 Read data from file and print in console. Don't forget and close it, use with block here.
 '''
'''
# Open file in 'append' mode ('a+'), if not exist than create it
with open('my_file.txt', 'a+', encoding="utf8") as file:
    # Append the text to the file
    file.write("Hello\n")
    file.write("It's my first file handling!\n")

# Open the file in 'read' mode ('r')
with open('my_file.txt', 'r') as file:
    # Read data from file
    file.read()
    # Print the contents to the console
    print(file.read())
    # Close
    file.close()
'''

'''
2.	Write a Python program which will create directory with your name, 
switch to directory and generate there 26 text files named A.txt, B.txt, and so on up to Z.txt.
'''
'''
import os

# 1. Define directory name
directory_name = "Anna_directory"

# 2. Create directory
os.mkdir(directory_name)

# 3. Switch to created directory
os.chdir(directory_name)

# 4. Generate there 26 text files named A.txt, B.txt, ..., Z.txt
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    file_name = letter + ".txt"
    with open(file_name, "w", encoding="utf8") as file:
        file.write(f"{file_name}\n")
'''

'''
3.	Write a Python program which will open file, add your name, 
surname and address to the file(keep there as dictionary).
'''

# Define name, surname, and address
name = "Anna"
surname = "Avtandilyan"
address = "Sisakyan 2"

# Create a dictionary to store the information
info = {
    "Name": name,
    "Surname": surname,
    "Address": address
}
# Open file and write the dictionary to it
with open("my_info.txt", "a", encoding="utf8") as file:
    file.write(str(info) + "\n")
