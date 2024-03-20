"""
1.	Write a Python program to get the Fibonacci series between 0 and 50.
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 0 1 1 2 3 5 8 13 21 34
"""

ask_for_number = int(input("Enter a number: "))


def fibonacci_sequence(number):
    fib_num_one = 0
    fib_num_two = 1

    for num in range(1, number):
        sum_fib_numbers = fib_num_one + fib_num_two
        fib_num_one = fib_num_two
        fib_num_two = sum_fib_numbers
        print(sum_fib_numbers)


fibonacci_sequence(ask_for_number)

'''
2.	Write a Python program that accepts a string and calculate the number of digits and letters.  
Sample Data: Python 3.2
Expected Output:
Letters 6
Digits 2
'''


def check_digit_letter(input_string):
    letter_count = 0
    digit_count = 0
    if input_string:
        for char in input_string:
            if char.isdigit():
                digit_count += 1
            elif char.isalpha():
                letter_count += 1
            else:
                continue
    else:
        return False

    return (f"String: {input_string} \n"
            f"Letters count: {letter_count} \n"
            f"Digit count: {digit_count}")


print(check_digit_letter("lesson_6"))

'''
3.	Write a Python program to print alphabet pattern 'L'
Expected Output:
*                                                                      
*                                                                      
*                                                                      
*                                                                      
*                                                                      
*                                                                      
*****
'''

# z horizontal line
# y vertical line
ask_for_vertical = int(input("Enter a horizontal line value (z): "))
ask_for_horizontal = int(input("Enter a horizontal line value (y): "))
for i in range(ask_for_vertical + 1):
    print("*")
    if i == ask_for_vertical:
        print("*" * ask_for_horizontal)

'''
4.	Write a Python program that reads two integers representing a month
and day and prints the season for that month and day.  
Expected Output:
Month: July(7)                   
Day: 31 
Season: Summer                                                    
'''

# Solution 1
'''
def get_season(month, day):
    # Dictionary mapping months to their respective seasons
    seasons = {
        1: "Winter", 2: "Winter", 3: "Spring",
        4: "Spring", 5: "Spring", 6: "Summer",
        7: "Summer", 8: "Summer", 9: "Fall",
        10: "Fall", 11: "Fall", 12: "Winter"
    }

    season = seasons[month] if (month != 3 or day >= 20) else "Winter"

    return season


ask_for_month = int(input("Enter a month: "))
ask_for_day = int(input("Enter a day: "))

season_of_year = get_season(ask_for_month, ask_for_day)

print(f"Month: {ask_for_month}")
print(f"Day: {ask_for_day}")
print(f"Season: {season_of_year}")
'''

# Solution 2
'''
ask_for_day = int(input("Enter day of day (1-31): "))
ask_for_month = int(input("Enter month (1-12): "))


def get_season(input_day, input_month):
    inner_month = ""
    inner_season = ""
    seasons = ["Winter", "Spring", "Summer", "Autumn"]
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    if input_month in months.keys():
        if input_day < 31:
            if input_month in (1, 2, 3):
                inner_season = seasons[0]
                inner_month = months[input_month] + f"({input_month})"
            elif input_month in (4, 5, 6):
                inner_season = seasons[1]
                inner_month = months[input_month] + f"({input_month})"
            elif input_month in (7, 8, 9):
                inner_season = seasons[2]
                inner_month = months[input_month] + f"({input_month})"
            elif input_month in (10, 11, 12):
                inner_season = seasons[3]
                inner_month = months[input_month] + f"({input_month})"
        else:
            return f"There is no {input_day} day in month"
    else:
        return f"There is no month with number {input_month}"
    return f"Month: {inner_month} \n "f"Day: {input_day} \n " f"Season: {inner_season}"


print(get_season(ask_for_day, ask_for_month))
'''

'''
5. Write a Python program to find the median of few values.
Numbers: 15, 26, 28, 33 or 1, 4, 5, 6, 7

Example:
1, 3, 3, 6, 7, 8, 9

Median = 6

1, 2, 3, 4, 5, 6, 8, 9,
Median = (4 + 5) / 2 = 4.5
'''

first_numbers = 15, 26, 28, 33
second_numbers = 1, 4, 5, 6, 7


def median(input_string):
    med = 0

    # first and second half parts of list
    first_list_part = []
    second_list_part = []

    # convert string to list
    str_list = list(input_string)

    # get length of list
    length = len(str_list)

    # reverse list
    reversed_list = str_list[::-1]

    # get half list value
    half_list = int(length / 2)

    # check if list length is even
    if length % 2 == 0:
        for number in range(1, half_list + 1):
            first_list_part.append(number)
        for number in range(half_list):
            second_list_part.append(reversed_list[number])
            med = (first_list_part[-1] + second_list_part[-1]) / 2
    else:
        # get middle number of the list which length value is odd
        middle_number = sorted(input_string)[len(input_string) // 2]
        return f"Median for {input_string} is: {middle_number}"
    return f"Median for {input_string} is: {med}"


print(median(second_numbers))
