"""
Write program of calculator
Requirements
- Your function should get 2 numbers (invalid values should not be accepted) and action name
- You could have 4 acitons add, sub, mult, div
- In all cases result format should be int, for example 2+2 = 4 and 16/4 = 4 but 10/8 should be exact value 1.25
- Division on 0 is not allowed
"""


def calc():
    while True:
        arg1 = input('input number1: ')
        arg2 = input('input number2: ')
        action = input('input action: ')

        if not (arg1.isnumeric() or arg1.replace('.', '', 1).isdigit()) or \
           not (arg2.isnumeric() or arg2.replace('.', '', 1).isdigit()) or \
           action not in ['+', '-', '*', '/']:
            print('Invalid inputs, try again with valid values')
            continue

        if action == '+':
            return float(arg1) + float(arg2)
        elif action == '-':
            return float(arg1) - float(arg2)
        elif action == '*':
            return float(arg1) * float(arg2)
        else: 
            if float(arg2) == 0:
                print('Division by zero is not allowed')
                continue
            elif float(arg1) % float(arg2) == 0:
                return int(float(arg1) / float(arg2))
            else:
                return float(arg1) / float(arg2)

print(calc())


# Anna - Logic is correct, everything work, only one note,
#  your / action return integer (if division result is int) but other actions always return float