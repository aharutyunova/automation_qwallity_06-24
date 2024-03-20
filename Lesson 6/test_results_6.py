"""1.	Write a Python program to get the Fibonacci series between 0 to 50. 
Note : The Fibonacci Sequence is the series of numbers : 
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 0 1 1 2 3 5 8 13 21 34"""

fibonacci_result = 9
f_1 = 1
f_2 = 0

for f in range(fibonacci_result):
    f = f_1 + f_2
    f_1 = f_2
    f_2 = f

    print(f)



'''
2.	Write a Python program that accepts a string and calculate the number of digits and letters.  
Sample Data: Python 3.2
Expected Output:
Letters 6
Digits 2
'''

string_name = input ("Enter a string: ")
d = l = 0

for c in string_name:
    if c.isdigit():
        d = d + 1
    elif c.isalpha():
        l = l + 1
    else:
        pass

print("Letters", l)
print("Digits", d)



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

'''
4.	Write a Python program that reads two integers representing a month and day and prints the season for that month and day.  
Expected Output:
Month: July(7)                   
Day: 31 
Season: Summer                                                    
'''
month = input("Enter the month")
day = int(input("Enter the day: "))

month = int(month)

if month in [1, 2, 12]:
    season = "Winter"
elif month in [3, 4, 5]:
    season = "Spring"
elif month in [6, 7, 8]:
    season = "Summer"
elif month in [9, 10, 11]:
    season = "Autumn"
else:
    season = "Invalid month"

print("Month:", month)
print("Day:", day)
print("Season:", season)


'''
5.	Write a Python program to find the median of few values. 
Numbers: 15, 26, 28, 33   or   1, 4, 5, 6, 7

Example:
1, 3, 3, 6, 7, 8, 9

Median=6

1, 2, 3, 4, 5, 6, 8, 9, 
Median = (4+5)/2 = 4.5
'''
