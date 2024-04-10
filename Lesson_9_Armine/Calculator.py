"""
Write program of calculator
Requirements
- Your function should get 2 numbers (invalid values should not be accepted) and action name
- You could have 4 acitons add, sub, mult, div
- In all cases result format should be int, for example 2+2 = 4 and 16/4 = 4 but 10/8 should be exact value 1.25
- Division on 0 is not allowed
"""

#Dear Anna, I will submit the calculator as soon as possible. I still want to work on it)
#Would you please check:
#Lesson 6 folder - lesson_6_medium checker.py file
#Lesson_7 folder - exercise_1_2.py file
#Lesson_8 folder totally
#Thank you in advance))

# You mentions files are checked :) Good luck with calculator


def Calculator():
    input1 = int(input("Please enter the first number: "))
    input2 = int(input("Please enter the second number: "))
    input3 = input("Please enter one of the actions: +, -, *, /: ")

    if input3 == "+":
        print(input1 + input2)
    elif input3 == "-":
        print(input1 - input2)
    elif input3 == "*":
        print(input1 * input2)
    elif input3 == "/":
        if input2 != 0:
            print(input1 / input2)
        else:
            print("Division by zero is not allowed")
    else:
        print("No such action available")

Calculator()