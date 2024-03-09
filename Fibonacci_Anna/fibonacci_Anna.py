start = 0
next_number = 1


def generate_fibonacci_sequence(start, next_number, n):
    for _ in range(n):
        print(start)
        new_number = start + next_number
        start, next_number = next_number, new_number

# Example: Generating the first 10 Fibonacci numbers
generate_fibonacci_sequence(start, next_number, 10)
