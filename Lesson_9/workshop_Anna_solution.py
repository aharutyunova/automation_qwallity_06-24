
"""
Write program of calculator
Requirements
- Your function should get 2 numbers (invalid values should not be accepted) and action name
- You could have 4 acitons add, sub, mult, div
- In all cases result format should be int, for example 2+2 = 4 and 16/4 = 4 but 10/8 should be exact value 1.25
- Division on 0 is not allowed
"""


def calculator(a, b, operator="add"):
    """Operator should be add, sub, mult, div"""
    if not ((isinstance(a, int) or isinstance(a, float))
            and (isinstance(b, float) or (isinstance(b, int)))):
        return ("Incorrect value of a or b")
    elif operator not in ("add", "sub", "mult", "div"):
        return ("incorrect operator")
    if operator == "add":
        return (a + b)
    elif operator == "sub":
        return a - b
    elif operator == "mult":
        return a * b
    elif operator == "div":
        if b == 0:
            return ("Zero division error")
        else:
            if a % b == 0:
                return int(a / b)
            else:
                return (a / b)
    else:
        pass


res = calculator(1, 0, operator="mult")
print(res)