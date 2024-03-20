'''
1.	Write a Python program to get the Fibonacci series between 0 to 50. 
Note : The Fibonacci Sequence is the series of numbers : 
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 0 1 1 2 3 5 8 13 21 34
'''
a = 0
b = 1
next_num = 0
while next_num <= 50:
    print(next_num)
    a, b = b, next_num
    next_num = a + b

# Anna - correct

'''
2.	Write a Python program that accepts a string and calculate the number of digits and letters.  
Sample Data: Python 3.2
Expected Output:
Letters 6
Digits 2
'''
given_str = "Python 3.2"
letters = 0
digits = 0

for item in given_str:
    if(item.isdigit()):
        digits += 1
    elif(item.isalpha()):
        letters += 1

print(f"In the given string, Letters = {letters} and Digits = {digits}")

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

text = "";    
for Row in range(0,8):    
    for Column in range(0,8):     
        if (Column == 1 or (Row == 7 and Column != 0 and Column < 7)):  
            text = text +"*"    
        else:      
            text = text +" "    
    text =text +"\n"    
print(text); 

# Anna - correct

'''
4.	Write a Python program that reads two integers representing a month and day and prints the season for that month and day.  
Expected Output:
Month: July(7)                   
Day: 31 
Season: Summer                                                    
'''

month = int(input("Type the number of the month: "))
day = int(input("Type the date: "))
months = ["Jan", "Feb", "March", "April", "May", "Jun", "July", "Aug", "September", "October", "November", "December"]

if (month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31 or month in [2, 4, 6, 9, 11] and 1<= day <= 30):
    if 1 <= month <= 2 or month == 12:
        print(f'Month: {months[month - 1]}({month})\nDay: {day}\nSeason: Winter')
    elif 6 <= month <= 8:
        print(f'Month: {months[month - 1]}({month})\nDay: {day}\nSeason: Summer')
    elif 9 <= month <= 11:
        print(f'Month: {months[month - 1]}({month})\nDay: {day}\nSeason: Autumn')
    elif 3 <= month <= 5:
        print(f'Month: {months[month - 1]}({month})\nDay: {day}\nSeason: Spring')
    else:
        print("Out of range")
elif month == 2 and day > 29:
    print(f'There is no date in February like {day} you entered')
else:
    print("Out of range")


# Anna -correct, interesting solution
'''
5.	Write a Python program to find the median of few values. 
Numbers: 15, 26, 28, 33   or   1, 4, 5, 6, 7

Example:
1, 3, 3, 6, 7, 8, 9

Median=6

1, 2, 3, 4, 5, 6, 8, 9, 
Median = (4+5)/2 = 4.5
'''
num = [1, 3, 7, 6, 7, 6, 10, 20, 4]
if len(num) % 2 != 0:
    print(num[len(num)-(len(num) // 2) - 1])
elif len(num) % 2 == 0:
    print((num[int((len(num)-1) / 2)] + num[int(((len(num)-1) / 2) + 1)]) /2)

    # Anna - The logic is correct, you just put bracket in incorrect place

    # Very good job!!!