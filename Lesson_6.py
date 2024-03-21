# 1 Write a Python program to get the Fibonacci series between 0 to 50. 
# Note : The Fibonacci Sequence is the series of numbers : 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 0 1 1 2 3 5 8 13 21 34


a, b = 0, 1
while a <= 50:
    print(a, end=' ')
    a, b = b, a + b



# 2.	Write a Python program that accepts a string and calculate the number of digits and letters.  
# Sample Data: Python 3.2
# Expected Output:
# Letters 6
# Digits 2
    


# 3.	Write a Python program to print alphabet pattern 'L'
# Expected Output:
# *                                                                       
# *                                                                      
# *                                                                      
# *                                                                      
# *                                                                      
# *                                                                      
# *****
    

def paint():
    for i in range(7):
        if i < 6:
            print("*")
        else:
            print("******")

paint()



#4.	Write a Python program that reads two integers representing a month and day and prints the season for that month and day.  
#Expected Output:
#Month: July(7)                   
#Day: 31 
#Season: Summer                                                    


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


# 5.	Write a Python program to find the median of few values. 
# Numbers: 15, 26, 28, 33   or   1, 4, 5, 6, 7

