ask_for_number = int(input("Enter a number: "))


def fibonacci_sequence(number):
    fib_num_one = 0
    fib_num_two = 1

    for num in range(number):
        sum_fib_numbers = fib_num_one + fib_num_two
        fib_num_one = fib_num_two
        fib_num_two = sum_fib_numbers
        print(sum_fib_numbers)


fibonacci_sequence(ask_for_number)
