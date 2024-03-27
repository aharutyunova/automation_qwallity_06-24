''' 1.	Write a Python program which will open file, if not exist than create it.  Append the following text with two lines:
 Hello - first line
 It's my first file handling! - second line
 Read data from file and print in console. Don't forget and close it, use with block here.
 '''

# Open file in 'append' mode ('a+'), if not exist than create it
# with open('my_file.txt', 'a+', encoding="utf8") as file:
#     # Append the text to the file
#     file.write("Hello\n")
#     file.write("It's my first file handling!\n")

# Open the file in 'read' mode ('r')

with open(r'C:\Qwallity\Automation_02_2024\automation_qwallity_06-24\task.txt', 'r') as file:
    # Read data from file
    file.read()
    # Print the contents to the console
    print(file.read())
    # Close
# Anna - generally correct, only when you read from the file in the line 17 and the print the read result nothing is printed
#  It is happened because because when you read from the 
# file the coursor is moved to the end of the file and when you read it second time and print, nothing is printed

#  When you use with open sintax, no need to close file at the end, file automatically closed





'''
2.	Write a Python program which will create directory with your name, 
switch to directory and generate there 26 text files named A.txt, B.txt, and so on up to Z.txt.
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

# Anna - everything is correct,
#  Other way to get all letters is to use string lib
#  Can try this one
"""
import string

print(string.ascii_uppercase)
"""

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

# Anna - correct

# All tasks are good enough