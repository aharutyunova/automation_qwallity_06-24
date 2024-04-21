
#1. Write a Python function to find the maximum value of given list(write algorithm).

def total_price(*args, **kwargs):
    total = sum(args) + sum(kwargs.values())
    print(f"Total price is {total}.")

total_price(100, 200, 300, apple=100, banana=200, orange=300)

# Anna - The solution for requirement to get total is correct, based on requirements you should get max value :)

#2.	Write a Python function, which will get few numbers from keyboard, return to sum of them

def sum_price(x=50, y=50, c=100):
    total = x + y + c
    print(total)
    return total

result = sum_price()
print("Result:", result)

# Anna - you get numbers from variables nor from input, but it is not a big difference, 
    


#3.	Create module  with name fib.py where keep function of Fibonacci, in second .py file import and call it.

def Fibonacci(n):
    if n < 0:
        print("0")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
    
limit = 50

print("Fibonacci series up to", limit, ":")
for i in range(limit):
    fib_number = Fibonacci(i)
    if fib_number > limit:
        break
    print(fib_number)