'''Write program of calculator
Requirements
- Your function should get 2 numbers (invalid values should not be accepted) and action name
- You could have 4 acitons add, sub, mult, div
- In all cases result format should be int, for example 2+2 = 4 and 16/4 = 4 but 10/8 should be exact value 1.25
- Division on 0 is not allowed'''


result = None
actions = ["add", "sub", "mult", "div"]
def calculator(a,b,action):
    
    if action not in actions:
        print("Invalid action")
    elif action == "add":
        res = a + b
    elif action == "sub":
        res = a - b
    elif action == "mult":
        res = a * b
    elif action == "div":
        if b == 0:
            res = "Division on 0 is not allowed"
        else:
            res = a / b
    if isinstance(res, str):
        return res
    elif res.is_integer():
        return int(res)
    else:
        return round(res,2)
    

a = float(input("Write your first number = "))
b =  float(input("Write your first number = "))
action = input("Action = ")


result = calculator(a,b,action)
print(result)


