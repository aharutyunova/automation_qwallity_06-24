# 1.	Write a Python program to get the Fibonacci series between 0 to 50. 

a = 0
b = 1

while b < 50:
    print(b)
    a = b
    b = a+b

# Anna correct

# Answer: 1, 2, 4, 8, 16, 32


# 2. Write a Python program that accepts a string and calculate the number of digits and letters.

x = "Python 3.2"

num_let = 0
num_dig = 0

for i in x:
    if i.isalpha():
        num_let = num_let + 1
    elif i.isdigit:
        num_dig = num_dig + 1
print("Letter:",  num_let)
print("Digits: ", num_dig)

# Anna correct

# 3.	Write a Python program to print alphabet pattern 'L'


print("Expected Output:")
print("*")
print("*")
print("*")
print("*")
print("*")
print("*****")

# Anna - will be better use loop for solution

# 4  Write a Python program that reads two integers representing a month and day and prints the season for that month and day.  


month = input("Input the month: ")
day = int(input("Input the day: "))


if month in ('December', 'January', 'February'):
    season = 'winter'
elif month in ('March', 'April', 'May'):
    season = 'spring'
elif month in ('June', 'July', 'August'):
    season = 'summer'
elif month in ('September', 'October', 'November'):
    season = 'summer'


if (month == 'March') or (month == 'April') or (month == 'May'):
    season = 'spring'
elif (month == 'June') or (month == 'July') or (month == 'August'):
    season = 'summer'
elif (month == 'September') or (month == 'October') or (month == 'November'):
    season = 'autumn'
elif (month == 'December') or (month == 'January') or (month == 'Febrary'):
    season = 'winter'

print("Season is", season) 

# Anna - the main logic is close to correct, but there some bugs :)
#  1.as you use season only in if/elif blocks, it is local space, so when you try print season, python gove you error,
#  you need to define season before if/else, for example in line 52 write season=None
# 2.per requirement your program should accept month as integerm not by name and print month name

# 5 Write a Python program to find the median of few values.
numbers1 = [15, 26, 28, 33]
numbers2 = [1, 4, 5, 6, 7]
x = len(numbers1)
print(x)

y = len(numbers2)
print(y)


if x % 2 == 0:
    print((numbers1[1] + numbers1[2])/2)
else:
    print("nothing")


if y % 2 != 0:
    print(numbers2[2])
else:
    print("nothing")

# Anna - solution works only in case list len is 5 and 4, as you hardcoded indexes, in case list len is changed, your code willn't work
    
# Anna - As it is our first complex task, it is good you find out solutions, even with some mistakes