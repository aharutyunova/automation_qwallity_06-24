# 3.	Create module  with name fib.py where keep function of Fibonacci, in second .py file import and call it.
from Fibonacci import Fibonacci as fib



# 1. Write a Python function to find the maximum value of given list(write algorithm)

list_1 = [17, 25, 4, 7, 76, 54, 83, 123]


def max_value(args):
    print(max(args))


max_value(list_1)


# another way of solving this task
def max_value(args):
    large_el = args[0]
    for x in args:
        if x > large_el:
            large_el = x

    return large_el


print(max_value(list_1))


# 2.	Write a Python function, which will get few numbers from keyboard, return to sum of them


def sum_nums(args):
    final_sum = 0

    for i in args.split():
        if not i.isdigit():
            return "Please input only numbers!!!"
        final_sum += int(i)
    return final_sum


numbers = input("Please input numbers from space in one line: ")
print(sum_nums(numbers))

# 3.	Create module  with name fib.py where keep function of Fibonacci, in second .py file import and call it.
fib.fibonacci(50)
