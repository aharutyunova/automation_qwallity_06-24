# 1.	Write a Python program to calculate the length of a string.
# my_string = ‘Here is string for your exercise!’

def func1():
    print("Please Enther the string1 you want")
    my_string1 = input()
    print("This is solution of 1-st task\n", len(my_string1))

# Anna - correct
    
# 2.	Write a Python program to get a string made of the first 2 and the last 2
# chars from a given a string.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'

def func2():
    print("Please Enther the string2 you want")
    my_string2 = input()
    print("This is solution of 2-nd task\n", my_string2[0:2] + my_string2[-2::])

# Anna - correct
    
# 3.	Write a Python program to add 'ing' at the end of a given string.
# Sample String : 'abc'
# Expected Result : 'abcing'


def func3():
    print("Please Enther the string3 you want")
    my_string3 = input()
    print("This is solution of 3-d task\n", my_string3 + "ing")

# Anna - correct

# 4.	Write a Python program to replace ‘cut’ word to ‘dog’
# Sample String : 'I have a cut and I love it'
# Expected Result : 'I have a dog and I love it'


def func4():
    my_string4 = "I have a cut and I love it"
    print("This is solution of 4-d task\n", my_string4.replace("cut", "dog"))

# Anna - correct
    
# 5.	Write a Python program to reverse 123  to 321 in text.
# Sample String : ‘I have 123 books’
# Expected Result : 'I have 321 books'
    

def func5():
    print("Please Enther the valid integer number")
    my_number = int(input())
    my_string5 = f"I have {my_number} books"
    print("This is my input string5\n", my_string5)
    mini_string = f"{my_number}"
    to_rep = ''.join(reversed(mini_string))
    print("This is solution of 5-d task\n")
    print(my_string5.replace(mini_string, to_rep))

# Anna - correct, Interesting solution

# 6.	Replace all occurrence of word five to one.
# Sample String : "five five was a race horse, two two was one too."
# Expected Result "one one was a race horse, two two was one too."


def func6():
    my_string6 = "five five was a race horse, two two was one too."
    print("This is solution of 6-d task\n", my_string6.replace("five", "one"))

# Anna - correct

# 7.	Write a Python program to which will print the triangle perimeter․
# Triangle sides are 3, 4, 7
# Expected Result: 14


def func7():
    print("Please Enther 3 valid integer number as  3 valid side of triangel")
    print("a = ", end="")
    a = int(input())
    print("\nb = ", end="")
    b = int(input())
    print("\nc = ", end="")
    c = int(input())

    if ((a+b <= c) or (b+c <= a) or (a+c <= b)):
        print("There is no triangel with your entered sides")
        print("any 2 sides summery will be greaten the the third side. ")

    else:
        print("This is solution of 7-d task\n", "perimiter=", a+b+c)

# Anna - very complex solution :)

# 8.	Write a Python program to check whether a specified value is contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False


def func8():
    print("Please enter the valid integer number : the count of new creating list's elemets")
    n = int(input())
    print(f"Please Enter {n} integer elements")
    my_list = []
    i = 0
    while (n > 0):
        my_inp = int(input())
        my_list.insert(i, my_inp)
        n = n-1
        i = i+1
    print("This is your list", my_list)
    print("Enther the number you want to find in your list")
    my_find_element = input()
    my_list_str = f"{my_list}"
    print("This is solution of 8-d task\n", my_find_element in my_list_str)

# Anna - correct, again complex solution 

# 9.	Write a Python program to solve (x + y) * (x + y). 
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49


def func9():
    print("Please Enther 2 valid integer numbers")
    print("x = ", end="")
    x = int(input())
    print("\ny = ", end="")
    y = int(input())
    print("Program will solv the folowwing formula\n(x+y)*(x+y)")
    print("This is solution of 9-d task\n", (x+y)*2)

# Anna - Almost correct , task is require ^2 action not *2 :) but it is not critical

# 10.Write a Python program which converts float values to integer, and sum of two values, then result print with reversed order.
# Test Data: x = 2,5 , y = 13.75
# Expected Output: 51

def func10():
    print("Please Enther 2 valid floating numbers")
    print("x = ", end="")
    x = float(input())
    print("\ny = ", end="")
    y = float(input())
    z = int(x) + int(y)
    str_sum = f"{z}"
    print("This is solution of 10-d task\n", ''.join(reversed(str_sum)))

# Anna correct

# func1()
# func2()
# func3()
# func4()
# func5()
# func6()
# func7()
# func8()
# func9()
# func10()

# Anna - good job, even more than enougth :)