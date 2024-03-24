
# 1. Write a Python function to find the maximum value of given list(write algorithm).

def max_value(list_numbers):
    max = list_numbers[0]
    for x in list_numbers:
        if x > max:
            max = x
    return max


list_numbers = [10, 20, 50, 30, 40]
print("Max value is:", max_value(list_numbers))

# 2. Write a Python function, which will get few numbers from keyboard, return to sum of them.

# example_1


def sum_numbers():
    numbers = []

    number_1 = int(input("Enter a number: "))
    numbers.append(number_1)
    number_2 = int(input("Enter a number: "))
    numbers.append(number_2)
    number_3 = int(input("Enter a number: "))
    numbers.append(number_3)

    return sum(numbers)


print("Sum number is:", sum_numbers())


# Example_2


def sum_numbers():
    numbers = []
    n = int(input("Enter the number of numbers: "))
    for _ in range(n):
        number = int(input("Enter a number: "))
        numbers.append(number)
    return sum(numbers)


print("Sum number is:", sum_numbers())


# 3.	Create module  with name fib.py where keep function of Fibonacci, in second .py file import and call it.

# import function
import fib

# call function
fib.fib_series()
