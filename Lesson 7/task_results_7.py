
# #1. Write a Python function to find the maximum value of given list(write algorithm).

# list = [1, 20, 53, 84, 59, 67, 302, 5, 18]

# def max_value(list):
#     max = list[0]
#     for x in list:
#         if x > max:
#             max = x
#     return max

# print(max_value(list))


# listt = [233.1, 500, 625, 987, 600, 154, 789]

# def min_value(listt):
#     min = listt[0]
#     for y in listt:
#         if y < min:
#             min = y
#     return min 


# print(min_value(listt))

# # Anna -very good

# #2.	Write a Python function, which will get few numbers from keyboard, return to sum of them

# numbers = [1, 2, 3, 4 , 5 , 6]


# def num(numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + 1
#     return sum

# print(num(numbers))


# def k_num():
#     num = input("Enter any numbers: ").split()
#     num = [int(k) for k in num]
#     tot_sum = sum(num)
#     return tot_sum

# print(k_num())

# Anna- correct


#3.	Create module  with name fib.py where keep function of Fibonacci, in second .py file import and call it.
 
import fibonacci_test as fib

print()

# Anna - will be better to write in fibonacci_test.py file only fibonacci function, and in this file call this function and print result

# Totally very good job