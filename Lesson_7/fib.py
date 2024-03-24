# Function of Fibonacci


def fib_series():
    fibonacci_series = [0, 1]
    while fibonacci_series[-1] + fibonacci_series[-2] <= 50:
        next_fibonacci = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_fibonacci)
    for number in fibonacci_series:
        print(number, end=" ")
