''' 1.	Write a Python program which will open file, if not exist than create it.  Append the following text with two lines:
 Hello - first line
 It's my first file handling! - second line
 Read data from file and print in console. Don't forget and close it, use with block here.
 '''


'''
#Open the file in 'append' mode ('a+'), creating it if it doesn't exist
with open('my_file.txt', 'a+') as file:
    # Append the specified text to the file
    file.write("Hello\n")
    file.write("It's my first file handling!\n")

# Open the file in 'read' mode ('r')
with open('my_file.txt', 'r') as file:
    # Read data from file
    file.read()
    # Print the contents to the console
    print(file.read())
    file.close()
'''

'''
2.	Write a Python program which will create directory with your name, 
switch to directory and generate there 26 text files named A.txt, B.txt, and so on up to Z.txt.
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
with open("my_info.txt", "a") as file:
    file.write(str(info) + "\n")