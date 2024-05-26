"""
Write program of calculator
Requirements
- Your function should get 2 numbers (invalid values should not be accepted) and arg_3 name
- You could have 4 arg_3s add, sub, mult, div
- In all cases result format should be int, for example 2+2 = 4 and 16/4 = 4 but 10/8 should be exact value 1.25
- Division on 0 is not allowed
"""


def calculator(num1, num2, action):

    if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
        return "Invalid input: Please enter valid numbers"

    if action == 'add':
        result = num1 + num2
    elif action == 'sub':
        result = num1 - num2
    elif action == 'mult':
        result = num1 * num2
    elif action == 'div':

        if num2 == 0:
            return "Division by zero is not allowed"
        else:
            result = num1 / num2
    else:
        return "Invalid action: Please choose 'add', 'sub', 'mult', or 'div'"

    if result.is_integer():
        result = int(result)

    return result


num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))
_action = input("Enter action (add, sub, mult, div): ")

print(calculator(num_1, num_2, _action))

# Anna - everything is correct
