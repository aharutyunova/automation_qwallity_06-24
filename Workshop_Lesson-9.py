"""
Write program of calculator
Requirements
- Your function should get 2 numbers (invalid values should not be accepted) and action name
- You could have 4 acitons add, sub, mult, div
- In all cases result format should be int, for example 2+2 = 4 and 16/4 = 4 but 10/8 should be exact value 1.25
- Division on 0 is not allowed
"""

actname = {"+","-","*","/"}
a = 6
b = 0
def cal(a,action,b):
    if action == "+":
        print(int(a + b))
    elif action == "-":
        print(int(a - b))
    elif action == "*":
        print(int(a * b)) 
    elif action == "/":
        if b == 0:
              print("Not allow to divide 0")
        elif a%b != 0:
            print(a / b)
        else:
            print(int(a / b))   
    else:
        print("That action can not find by my code")

cal(a,"+", b)
cal(a,"-", b)          
cal(a,"*", b)
cal(a,"/", b)
