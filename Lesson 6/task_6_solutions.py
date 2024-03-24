'''
1.	Write a Python program to get the Fibonacci series between 0 to 50. 
Note : The Fibonacci Sequence is the series of numbers : 
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34
'''

a = 0
b = 1

print(a, end=' ')
while b <= 50:
    print(b, end=' ')
    a, b = b, a + b
print('')
'''
2.	Write a Python program that accepts a string and calculate the number of digits and letters.  
Sample Data: Python 3.2
Expected Output:
Letters 6
Digits 2
'''
sample_data = "Python 3.2"
x = y = 0
for a in sample_data:
    if a.isdigit():
        x = x+1
    elif a.isalpha():
        y = y+1
print(f'digits - {x}')
print(f'letters - {y}')


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

# Version 2
a = 0
while a < 7:
    print('*')
    a += 1
print('*'*7)

# Nel, more good version

'''
4.	Write a Python program that reads two integers representing a month and day and prints the season for that month and day.  
Expected Output:
Month: July(7)                   
Day: 31 
Season: Summer                                                    
month = 7
'''
month = 1
day = 31
month_name = None
season = None

months = ["January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"]
seasons = {"Winter": ["December","January", "February"], "Spring": ["March", "April","May"], "Summer": ["June", "July", "August"], "Automn": ["September", "October", "November"]}
months_to_days = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

if month in range(1, len(months)+1):
    month_name = months[month-1]
    print(f'Month: {month_name}({month})')
    for key in seasons.keys():
        a = seasons[key]
        if month_name in seasons[key]:
            season = key
            print(f'Season: {season}')
    if day not in range(months_to_days[month_name]+1):
        print("Invalid Day")
    else:
        print(f"Day {day}")
else:
    print("Invalid Month")





'''5.	Write a Python program to find the median of few values. 
Numbers: 15, 26, 28, 33   or   1, 4, 5, 6, 7

Example:
1, 3, 3, 6, 7, 8, 9
Median=6

1, 2, 3, 4, 5, 6, 8, 9, 
Median = (4+5)/2 = 4.5
'''

test_list = [1, 4, 5, 5]

if len(test_list) % 2 == 0:
    ind_1 = int(len(test_list) / 2)
    ind_2 = ind_1 -1
    median = (test_list[ind_1] + test_list[ind_2])/2
else:
    ind = int(len(test_list)/2)
    median = test_list[ind]
print(median)


