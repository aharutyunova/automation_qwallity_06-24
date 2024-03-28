from calculator_functions import *

# Write program of calculator

# Requirements

# 1. Your function should get 2 numbers (invalid values should not be accepted) and action name
# 2. You could have 4 actions add, sub, mult, div
# 3. In all cases result format should be int, for example 2+2 = 4 and 16/4 = 4 but 10/8 should be exact value 1.25
# 4. Division on 0 is not allowed

# result of calculation operation
calculation_result = 0

print("Calculator operations:")
print("1. Addition: (+) ")
print("2. Subtraction: (-) ")
print("3. Multiplication: (*) ")
print("4. Division: (/) ")

ask_for_first_number = int(input("Enter first number: "))
ask_for_second_number = int(input("Enter second number: "))
ask_for_operation_type = input("Enter operation: ")

if ask_for_operation_type == "+":
    calculation_result = add(ask_for_first_number, ask_for_second_number)
elif ask_for_operation_type == "-":
    calculation_result = sub(ask_for_first_number, ask_for_second_number)
elif ask_for_operation_type == "*":
    calculation_result = mult(ask_for_first_number, ask_for_second_number)
elif ask_for_operation_type == "/":
    calculation_result = div(ask_for_first_number, ask_for_second_number)

# print result to console calculation result value
print(f"Result: {calculation_result}")
