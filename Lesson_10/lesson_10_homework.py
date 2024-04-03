

# 1. Write a Python class to reverse a string word by word. Input string : 'hello .py'. 
# Expected Output : '.py hello'

class Reverse:
    def __init__(self):
        self.string = input("input string for reversing: ")
    def reverse_str(self):
        modif_str = ' '.join(list(reversed(self.string.split())))
        return modif_str
x = Reverse()
print(x.reverse_str())

# 2. Write a Python class which get any string and with methods print_String print this sting in upper case 

class Upper:
    def __init__(self):
        self.string = input("input string for uppercase: ")
    def upper_str(self):
        modif_str = self.string.upper()
        return modif_str
x = Upper()
print(x.upper_str())
# 3. Write a Python class to generate 26 text files named A.txt, B.txt, and so on up to Z.txt. 
import os
class AlphabetFiles:
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def file_creating(self):
        os.chdir('Lesson_10')
        os.mkdir('AZ_Files')
        os.chdir('AZ_Files')

        for element in range(0, len(self.alphabet)):
            file_name = self.alphabet[element] + '.txt'
            f = open(file_name, 'w+', encoding = 'utf-8')
            f.close()
        return 
x = AlphabetFiles()
x.file_creating()