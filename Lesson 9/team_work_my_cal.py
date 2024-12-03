""" Team members are Shushan, Hamest and Mariam"""

""" 
Write program of calculator
Requirements
- Your function should get 2 numbers (invalid values should not be accepted) and action name
- You could have 4 acitons add, sub, mult, div
- In all cases result format should be int, for example 2+2 = 4 and 16/4 = 4 but 10/8 should be exact value 1.25
- Division on 0 is not allowed
"""


Action_name = ["+", "-", "*", "/"]
a = 15
b = 4

def cal(a, action, b):
    if action == "+":
        print(int(a + b))
    elif action == "-":
        print(int(a - b))
    elif action == "*":
        print(int(a * b))
    elif action == "/":
        if a == 0 or b == 0:
            print("Division by zero is not allowed.")
        elif a%b != 0:
            print(a / b)
        else: 
            print(int(a / b))
    else:
        print("Invalid action. Please choose from '+', '-', '*', '/'.")


action = input("Please enter the action what you want")-
cal(a, action, b)

# Anna - why you need actions as a list? I changed it to one action  - line 35
#  In Line 25 where you check a or b are equal to 0, when you write a or b==0, it means check, a exists or b ==0, 
#  So you should write if a == 0 or b == 0:
# But in your case you should check that only b is not equal to 0, "a" could be equal to 0

# Other logic is correct :)