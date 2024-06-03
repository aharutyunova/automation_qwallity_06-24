'''
1.	Write a Python program to get the Fibonacci series between 0 to 50.
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 0 1 1 2 3 5 8 13 21 34
'''



def fibonacci(n):
    a = 0
    b = 1

    if n < 0:
        print("incorrect input")
    else:
        for i in range(n):

            if i == 0:
                print(0)
            else:
                c = a + b
                a = b
                b = c
            print(b)


(fibonacci(9))

#another solution

def fibonacci(n):
    if n <= 0:
        return "Incorrect output"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(9))

# Anna - first solution is correct, second not return fibopnacci sequence
'''
2.	Write a Python program that accepts a string and calculate the number of digits and letters.  
Sample Data: Python 3.2
Expected Output:
Letters 6
Digits 2
'''

sample_data = "Fibonacci_50"

count_lett = 0
count_dig = 0
for i in sample_data:
    print(i)
    if i.isalpha():
        count_lett += 1
    if i.isdigit():
        count_dig += 1

print(f"Letters {count_lett}\nDigits {count_dig}")
#we can also use print command for two lines
#print("Letters", count_lett)
#print("Digits", count_dig)

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

height = 7

for i in range(height):
    if i < height - 1:
        print("*")
    else:
        print(height * "*")

# Anna correct

'''
4.	Write a Python program that reads two integers representing a month and day and prints the season for that month and day.  
Expected Output:
Month: July(7)                   
Day: 31 
Season: Summer                                                    
'''

seasons_list = [
    {"Month_name": "January", "Month": 1, "Day": 31, "Season": "Winter"},
    {"Month_name": "February", "Month": 2, "Day": 28, "Season": "Winter"},
    {"Month_name": "March", "Month": 3, "Day": 31, "Season": "Spring"},
    {"Month_name": "April", "Month": 4, "Day": 30, "Season": "Spring"},
    {"Month_name": "May", "Month": 5, "Day": 31, "Season": "Spring"},
    {"Month_name": "June", "Month": 6, "Day": 30, "Season": "Summer"},
    {"Month_name": "July", "Month": 7, "Day": 31, "Season": "Summer"},
    {"Month_name": "August", "Month": 8, "Day": 31, "Season": "Summer"},
    {"Month_name": "September", "Month": 9, "Day": 30, "Season": "Fall"},
    {"Month_name": "October", "Month": 10, "Day": 31, "Season": "Fall"},
    {"Month_name": "November", "Month": 11, "Day": 30, "Season": "Fall"},
    {"Month_name": "December", "Month": 12, "Day": 31, "Season": "Winter"},
]

month = int(input("Month: "))
day = int(input("Day: "))

for i in seasons_list:
    if i["Month"] == month and 1 <= day <= i["Day"]:
        print(f"Month: {i['Month_name']}({month})\nDay: {day}\nSeason: {i['Season']}")
        break
else:
    print("Something went wrong!!!")



# another solution

month = input("Input the month (e.g. January, February etc.): ")
day = int(input("Input the day: "))
if month in ('January', 'February', 'March'):
    season = 'winter'
elif month in ('April', 'May', 'June'):
    season = 'spring'
elif month in ('July', 'August', 'September'):
    season = 'summer'
else:
    season = 'autumn'
if (month == 'March') and (day > 19):
    season = 'spring'
elif (month == 'June') and (day > 20):
    season = 'summer'
elif (month == 'September') and (day > 21):
    season = 'autumn'
elif (month == 'December') and (day > 20):
    season = 'winter'
print("Season is", season)

# Anna - the second solution not accept month as integer and print only Season. First solution cover all requirements
'''
5.	Write a Python program to find the median of few values. 
Numbers: 15, 26, 28, 33   or   1, 4, 5, 6, 7

Example:
1, 3, 3, 6, 7, 8, 9

Median=6

1, 2, 3, 4, 5, 6, 8, 9, 
Median = (4+5)/2 = 4.5
'''

val_list = [78, 41, 9, 32, 64]

median = 0
if len(val_list) % 2 == 0:
    before_median = val_list[:int(len(val_list)//2)]
    after_median = val_list[int(len(val_list)//2):]
    median = (before_median[-1] + after_median[0]) / 2
elif len(val_list) % 2 != 0:
    median = val_list[int(len(val_list) // 2)]
print(median)

# Anna - correct

# Very Good Job for this difficult tasks:)