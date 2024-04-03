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
        if  arg1.isalpha() or arg2.isalpha() or action not in('+','-', '*', '/'):
            print('Invalid inputs, try again with valid values', float(arg1), float(arg2))
            break
        else:
            if action == '+':
                return float(arg1) + float(arg2)
            elif action == '-':
                return float(arg1) - float(arg2)
            elif action == '*':
                return float(arg1) * float(arg2)
            else:
                if arg2 == '0':
                    print('Division on 0 is not allowed')
                    break
                else:
                    if float(arg1) % float(arg2) == 0:
                        return int(float(arg1)/float(arg2))
                    else:
                        return float(arg1)/float(arg2)

print(calc())