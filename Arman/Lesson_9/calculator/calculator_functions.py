# calculator functions

def addition(number_one, number_two):
    """Add two numbers and return the result."""
    if number_one and number_two:
        return format(number_one + number_two, '.1f')
    return 0


def subtraction(number_one, number_two):
    """Subtract number_two from number_one and return the result."""
    if number_one and number_two:
        return format(number_one - number_two, '.1f')
    return 0


def multiplication(number_one, number_two):
    """Multiply two numbers and return the result"""
    if number_one and number_two:
        return format(number_one * number_two, '.1f')
    return 0


def division(number_one, number_two):
    """Divide number_one by number_two and return the result"""
    if number_one and number_two:
        return format(number_one / number_two, '.1f')
    else:
        return "Number cannot be divided by 0"


def calculator_operation(first_number, second_number, operation_type):
    """General function of the calculator operation"""
    calculation_result = 0
    if operation_type == "+":
        calculation_result = addition(first_number, second_number)
    elif operation_type == "-":
        calculation_result = subtraction(first_number, second_number)
    elif operation_type == "*":
        calculation_result = multiplication(first_number, second_number)
    elif operation_type == "/":
        calculation_result = division(first_number, second_number)
    else:
        return f"There is no operation type like: ({operation_type})"
    return print(f"Result: {calculation_result}")
