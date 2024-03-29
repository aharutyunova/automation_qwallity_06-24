from calculator_functions import *

# Write program of calculator

# Requirements

# 1. Your function should get 2 numbers (invalid values should not be accepted) and action name
# 2. You could have 4 actions add, sub, mult, div
# 3. In all cases result format should be int, for example 2+2 = 4 and 16/4 = 4 but 10/8 should be exact value 1.25
# 4. Division on 0 is not allowed

# show operation types to the console
print("Calculator operations:")
print("1. Addition        (+)")
print("2. Subtraction     (-)")
print("3. Multiplication  (*)")
print("4. Division        (/)")

# ask for first calculator number in console from user
ask_for_first_number = int(input("Enter first number: "))
# ask for first calculator number in console from user
ask_for_second_number = int(input("Enter second number: "))
# ask for first calculator number in console from user
ask_for_operation_type = input("Enter operation: ")
# run calculator operation function and print result to console
calculator_operation(int(ask_for_first_number), int(ask_for_second_number), ask_for_operation_type)
