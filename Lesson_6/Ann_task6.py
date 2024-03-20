'''
1.	Write a Python program to get the Fibonacci series between 0 to 50. 
Note : The Fibonacci Sequence is the series of numbers : 
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 0 1 1 2 3 5 8 13 21 34
'''
fibonacci_series = [0, 1]
while fibonacci_series[-1] + fibonacci_series[-2] <= 50:
    next_fibonacci = fibonacci_series[-1] + fibonacci_series[-2]
    fibonacci_series.append(next_fibonacci)
for number in fibonacci_series:
    print(number, end=" ")
print()

# Anna - correct
'''
2.	Write a Python program that accepts a string and calculate the number of digits and letters.  
Sample Data: Python 3.2
Expected Output:
Letters 6
Digits 2
'''
str = "python 3.2"
digit = 0
letter = 0
for char in str:
    if char.isdigit():
        digit = digit + 1
    elif char.isalpha():
        letter = letter + 1
    else:
        pass

print("Letters:", letter)
print("Digits:", digit)

# Anna - correct

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
# Solution 1
height = 7
for row in range(height):
    if row == height - 1:
        print("*" * (height - 2))
    else:
        print("*")
# Solution 2
for i in range(11):
    if i >= 6:
        print("*", end="")
    else:
        print("*")
print()

# Anna - both solutions are correct
'''
4.	Write a Python program that reads two integers representing a month and day and prints the season for that month and day.  
Expected Output:
Month: July(7)                   
Day: 31 
Season: Summer                                                    
'''


'''
5.	Write a Python program to find the median of few values. 
Numbers: 15, 26, 28, 33   or   1, 4, 5, 6, 7

Example:
1, 3, 3, 6, 7, 8, 9
Median=6

1, 2, 3, 4, 5, 6, 8, 9,
Median = (4+5)/2 = 4.5
'''
# even numbers
numbers_list = [1, 2, 3, 4, 5, 6, 8, 9]

if len(numbers_list) % 2 != 0:
    print(f"Median is: {numbers_list[len(numbers_list) // 2]}")
else:
    before_center = int(numbers_list[(len(numbers_list) // 2) - 1])
    after_center = int(numbers_list[len(numbers_list) // 2])
    median = (before_center + after_center) / 2
    print(f"Median is: {median}")

# odd numbers
numbers_list = [1, 2, 3, 4, 5, 6, 8]

if len(numbers_list) % 2 != 0:
    print(f"Median is: {numbers_list[len(numbers_list) // 2]}")
else:
    before_center = int(numbers_list[(len(numbers_list) // 2) - 1])
    after_center = int(numbers_list[len(numbers_list) // 2])
    median = (before_center + after_center) / 2
    print(f"Median is: {median}")


# Anna correct :)
# Good job An jan, 4th task will discuss tomorrow  