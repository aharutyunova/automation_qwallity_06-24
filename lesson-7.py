#1. Write a Python function to find the maximum value of given list(write algorithm).


def find_max(input_list):
    max_value = input_list[0]
    for num in input_list[1:]:
        if num > max_value:
            max_value = num
    return max_value
mylist = [15, 55, 37, 62, 28]
result = find_max(mylist)
print("The maximum value in the list is:", result) 


#2.	Write a Python function, which will get few numbers from keyboard, return to sum of them

def new_func(m, a, r):
    return sum([m, a, r])


result = new_func(13, 1, 18)
print("This is sum:", result)


#3.	Create module  with name fib.py where keep function of Fibonacci, in second .py file import and call it

a = 3
b = 2

while b < 50:
    print(a,b)
    a = b
    b = a + b