# 1 Write a Python class to reverse a string word by word. Input string : 'hello .py'. 

class Anush:
    def __init__(self, string):
        self.string = string

    def rev_word(self):
        return self.string[::-1]


inputt = 'hello.py'
rev = Anush(inputt)
new = rev.rev_word()
print("Original string:", inputt)
print("Reversed string:", new)


# 2 Write a Python class which get any string and with methods print_String print this sting in upper case

class Uppercase:
    def __init__(self, string):
        self.string = string
        
    def stringWord(self):
        print(self.string.upper())


newString = "Hello Anush , you are so beautiful"
print1 = Uppercase(newString)
print1.stringWord()



# 3  Write a Python class to generate 26 text files named A.txt, B.txt, and so on up to Z.txt. 


import os

os.makedirs("letter")

with open("txt57", "w+") as f:
    f.writelines(letter)
       
       
       
#      To be continued․․․․․․․․․․․․