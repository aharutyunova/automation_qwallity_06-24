# calculator functions

def add(number_one, number_two):
    """Add two numbers and return the result."""
    if number_one and number_two:
        return int(number_one + number_two)
    return " "


def sub(number_one, number_two):
    """Subtract number_two from number_one and return the result."""
    if number_one and number_two:
        return int(number_one - number_two)
    return ""


def mult(number_one, number_two):
    """Multiply two numbers and return the result"""
    if number_one and number_two:
        return int(number_one * number_two)
    return 0


def div(number_one, number_two):
    """Divide number_one by number_two and return the result.
    If both numbers are positive and at least one is a float, return a float; otherwise, return an integer.
    """
    if number_one and number_two:
        if number_one > 0 and number_two > 0:
            if isinstance(number_one, float) or isinstance(number_two, float):
                return float(number_one / number_two)
    return 0


def calculator_operation(first_number, second_number, operation_type):
    """General function of the calculator operation"""
    calculation_result = 0
    if operation_type == "+":
        calculation_result = add(first_number, second_number)
    elif operation_type == "-":
        calculation_result = sub(first_number, second_number)
    elif operation_type == "*":
        calculation_result = mult(first_number, second_number)
    elif operation_type == "/":
        calculation_result = div(first_number, second_number)
    return print(f"Result: {calculation_result}")
