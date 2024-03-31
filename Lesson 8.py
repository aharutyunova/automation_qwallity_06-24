'''1.	Write a Python program which will open file, if not exist than create it.  Append the following text with two lines:
 Hello - first line
 It's my first file handling! - second line
 Read data from file and print in console. Don't forget and close it, use with block here.
 '''


filename = "hello"
with open(filename, "a+") as file:
    file.write("Hello - first line\n")
    file.write("It's my first file handling! - second line\n")
with open(filename, "r") as file:
    data = file.read()
    print(data)


'''
2.	Write a Python program which will create directory with your name, 
switch to directory and generate there 26 text files named A.txt, B.txt, and so on up to Z.txt.
'''
  



  
'''3. Write a Python program which will open file, add your name, 
 surname and address to the file(keep there as dictionary).'''

file = "file.txt"
with open(file, "a") as file:
    name = input("Mariam")
    surname = input("Galoyan")
    address = input("Tumanyan street")

myinfo = {
        "Name": name,
        "Surname": surname,
        "Address": address
    }
with open("file.txt", "a", encoding="utf-8") as file:
    file.write(str(myinfo) + "\n")

print("exercise_finished")



