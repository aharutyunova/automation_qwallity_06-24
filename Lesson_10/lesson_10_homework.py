# 1. Write a Python class to reverse a string word by word. Input string : 'hello .py'. 
# Expected Output : '.py hello'

# class My_class:
#     def __init__(self, my_string):
#         self.my_string = my_string
#     def reverse_string(self):
#         l = self.my_string.split()
#         l.reverse()
#         new_string = " "
#         return new_string.join(l)
    

# string1 = My_class("hello .py")
# y = string1.reverse_string()
# print(y)

# 2. Write a Python class which get any string and with methods print_String print this sting in upper case 


# class my_class:
#     def __init__(self,any_string):
#         self.any_string = any_string
#     def upper_string(self):
#         x = self.any_string.upper()
#         return x
    
# string1 = my_class("Barev")
# print(string1.upper_string())

# 3. Write a Python class to generate 26 text files named A.txt, B.txt, and so on up to Z.txt. 

from string import ascii_uppercase
import os



class Generate_files:
    os.mkdir("c:/automation_qwallity_06-24/Lesson_10/juli")
    os.chdir("c:/automation_qwallity_06-24/Lesson_10/juli")
    for i in ascii_uppercase:
        with open(i + ".txt", "w+", encoding="utf8") as f:
            f.write("")


x = Generate_files()
