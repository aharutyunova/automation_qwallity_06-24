"""
Write program of calculator
Requirements
- Your function should get 2 numbers (invalid values should not be accepted) and action name
- You could have 4 acitons add, sub, mult, div
- In all cases result format should be int, for example 2+2 = 4 and 16/4 = 4 but 10/8 should be exact value 1.25
- Division on 0 is not allowed
"""

actions = ["add", "sub", "mult", "div"]


def calculator(a, b, action):
    if action not in actions:
        return "Invalid action"
    elif action == "add":
        return a + b
    elif action == "sub":
        return a - b
    elif action == "mult":
        return a * b
    elif action == "div":
        if b == 0:
            return "Division on 0 is not allowed"
        else:
            return a / b


a = float(input("Write your first number = "))
b = float(input("Write your first number = "))
action = input("Action = ")
result = calculator(a, b, action)
# check the type of result
if isinstance(result, str):
    print(result)
elif isinstance(result, float) and result.is_integer():
    print(int(result))
else:
    print((result))


# Anna - very good, didn't find any bugs)))