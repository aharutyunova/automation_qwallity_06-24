from Arman.modules import fib

# 1. Write a Python function to find the maximum value of given list (write algorithm).

random_numbers_list_one = [1, 2, 5, 7, 9, 12, 17, 19, 23, 24, 32]
random_numbers_list_two = [10, 50, 72, 92, 70, 102, 109, 233, 240, 120]


# function finds maximum value in any list with integers
# Solution 1
def list_max_value(input_list):
    max_value = 0
    if input_list:
        max_value = input_list[0]
        for number in input_list:
            if number > max_value:
                max_value = number
    return max_value


# Solution 2
def lst_max_value(input_list):
    return sorted(input_list)[-1]


print(f" Solution 1: {list_max_value(random_numbers_list_one)}")
print(f" Solution 2: {lst_max_value(random_numbers_list_two)}")


# 2. Write a Python function, which will get few numbers from keyboard, return to sum of them

# function returns numbers sum from input
# question count 5 in the function
def sum_numbers():
    question_count = 1
    numbers = []
    print("Question total count: 5")
    while question_count < 6:
        print(f"Question: {question_count}")
        enter_number = int(input("Enter a number: "))
        numbers.append(enter_number)
        question_count += 1
    return f"sum of numbers of list: {sum(numbers)}"


print(sum_numbers())

# 3. Create module with name fib-py where keep function of Fibonacci, in second •py file import and call

# get user number from input
ask_for_number = int(input("Enter a number (fibonacci sequence): "))

# run fibonacci sequence function
fibonacci_sequence = fib.fibonacci_sequence(ask_for_number)
