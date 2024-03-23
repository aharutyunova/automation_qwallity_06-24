# 1. Write a Python function to find the maximum value of given list(write algorithm).

def func1(listik):
    if not listik:
        return None
    max1 = max(listik)
    return max1


my_list = [21, 5, 1, 14, 2, 7, 46]
print("Maximum value in the list:", func1(my_list))

# Answer` 46

# 2. Write a Python function, which will get few numbers from keyboard, return to sum of them 


def new_func(a, b, c):
    return sum([a, b, c])


result = new_func(5, 6, 7)
print("This is sum:", result)


# Answer` 18

# 3. Create module  with name fib.py where keep function of Fibonacci, in second .py file import and call it.


a = 0
b = 1

while b < 50:
    print(b)
    a = b
    b = a + b