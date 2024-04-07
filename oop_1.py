# 1. Write a Python class to reverse a string word by word. Input string : 'hello .py'. 
# Expected Output : '.py hello'

class Reverse:
    def __init__(self, word):
        self.word = word

    def hello(self):
        if self.word:
            print('.py hello')
        else:
            print("Incorrect text")


reverse1 = Reverse('hello .py')
reverse1.hello()


# 2. Write a Python class which get any string and with methods print_String print this sting in upper case 


class Point_2():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())

str1 = Point_2()
str1.get_String()
str1.print_String()


# 3. Write a Python class to generate 26 text files named A.txt, B.txt, and so on up to Z.txt. 

class Create:
    def __init__(self, file):
        self.file = ""


def create_26_files(self):
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        filename = letter + '.txt'
        with open(filename, 'w') as file:
            file.write(f"This is file {filename}\n")

        print(f"File {filename} created.")


new_file = Create()
new_file.create_26_files() 