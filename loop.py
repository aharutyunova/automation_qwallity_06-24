# 1.	Write a Python program to get the Fibonacci series between 0 to 50. 
# Note : The Fibonacci Sequence is the series of numbers : 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# # Expected Output : 0 1 1 2 3 5 8 13 21 34
# '''


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

# Anna - correct but solution is not simple

# '''
# 2.	Write a Python program that accepts a string and calculate the number of digits and letters.  
# Sample Data: Python 3.2
# Expected Output:
# Letters 6
# Digits 2
# '''

num = "qwallity 2024"
count = sum(1 for char in num if char.isalpha())
print(count)
 
num = "qwallity 2024"
count = sum(1 for char in num if char.isdigit())
print(count)

# Anna - correct but you could count digits and letters in on loop

# 3.	Write a Python program to print alphabet pattern 'L'
# Expected Output:
# *                                                                      
# *                                                                      
# *                                                                      
# *                                                                      
# *                                                                      
# *                                                                      
# *****


for row in range(7):
    for col in range(5):
        if col == 0 or (row == 6 and col < 5):
            print("*", end="")
        else:
            print(end=" ")
    print()

# Anna -correct



# 4.	Write a Python program that reads two integers representing a month and day and prints the season for that month and day.  
# Expected Output:
# Month: July(7)                   
# Day: 31 
# Season: Summer                                                    
# '''


i = 5
j = 20
 
seasons = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
 
# #for index, value in enumerate(seasons, 1):
#     print(index, value)
 
if i in (1, 2, 12):
    print("Winter:", seasons[i-1], j)
elif i in (3, 4, 5):
    print("Spring:", seasons[i-1], j)
elif i in (6, 7, 8):
    print("Summer:", seasons[i-1], j)
elif i in (9, 10, 11):
    print("Autumn:", seasons[i-1], j)
else:
    print("Incorrect value")

# Anna - only checking of valid days is absent, but logic and solution is correct

# '''
# 5.	Write a Python program to find the median of few values. 
# Numbers: 15, 26, 28, 33   or   1, 4, 5, 6, 7

# Example:
# 1, 3, 3, 6, 7, 8, 9

# Median=6

# 1, 2, 3, 4, 5, 6, 8, 9, 
# Median = (4+5)/2 = 4.5
# '''
    
    
a = [1,4,5,6,7]
 
if len(a) % 2 == 0:
    print((a[len(a) // 2 - 1] + a[len(a) // 2]) / 2)
else:
    print(a[len(a) // 2 ])
 
b = [15, 26, 28, 33]
 
if len(b) % 2 == 0:
    print((b[len(b) // 2 - 1] + b[len(b) // 2]) / 2)
else:
    print(b[len(b) // 2 ])

    
# Anna - correct
    
# Very Good job!!!