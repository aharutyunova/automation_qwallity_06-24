# calculator functions

def add(number_one, number_two):
    if number_one and number_two:
        return number_one + number_two
    return " "


def sub(number_one, number_two):
    if number_one and number_two:
        return number_one - number_two
    return " "


def mult(number_one, number_two):
    if number_one and number_two:
        if number_one == 0 or number_two == 0:
            return number_one * number_two
    return 0


def div(number_one, number_two):
    if number_one and number_two:
        if number_one > 0 and number_two > 0:
            return float(number_one / number_two)
    return 0
