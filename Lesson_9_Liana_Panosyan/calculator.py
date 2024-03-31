"""
Write program of calculator
Requirements
- Your function should get 2 numbers (invalid values should not be accepted)
 and action name
- You could have 4 acitons add, sub, mult, div
- In all cases result format should be int, for example 2+2 = 4 and 16/4 = 4 
but 10/8 should be exact value 1.25
- Division on 0 is not allowed
"""

actions = ["add", "sub", "mult", "div"]


def calculator(a, b, action):
    if action not in actions:
        return "Invalid action"

    result = None

    if action == "add":
        result = a + b
    elif action == "sub":
        result = a - b
    elif action == "mult":
        result = a * b
    elif action == "div":
        if b == 0:
            return "Division by zero is not allowed."
        else:
            result = a / b
    if result.is_integer():
        return int(result)
    else:
        return result


a = float(input("Write your first number = "))
b = float(input("Write your second number = "))
action = input("Enter the action (add/sub/mult/div): ")


result = calculator(a, b, action)
print(result)

# Anna very good  :)
# Only note related to float number calculation - for example in case you add 1.1+2.2 you will get not 3.3 but 3.3000000000000003
# Also inptut messages and format are userfriendly
#  It is because of specifications of numbers convertion by interpretator.
#  In case you need get exact result you need use Decimal

# from decimal import Decimal 
# a = Decimal(input("Write your first number = "))
# b = Decimal(input("Write your second number = "))