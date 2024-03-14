"""1.	Write a Python program to calculate the length of a string.
#my_string = ‘Here is string for your exercise!’"""

my_string = 'Here is string for your exercise!'
print(len(my_string))

"""2.	Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'"""


"""3.	Write a Python program to add 'ing' at the end of a given string.
Sample String : 'abc'
Expected Result : 'abcing'"""

sample_string = 'abc'
result = sample_string + 'ing'
print(result)

"""4.	Write a Python program to replace ‘cut’ word to ‘dog’
Sample String : 'I have a cut and I love it'
Expected Result : 'I have a dog and I love it'"""

Sample_string = 'I have a cut and I love it'
Expected_string = Sample_string.replace('cut', 'dog')
print(Expected_string)


"""5.	Write a Python program to reverse 123  to 321 in text.
Sample String : ‘I have 123 books’
Expected Result : 'I have 321 books'"""

Sample_String = 'I have 123 books'
new_string = '123'
print("".join(reversed(new_string)))


"""6.	Replace all occurrence of word five to one.
Sample String : "five five was a race horse, two two was one too."
Expected Result "one one was a race horse, two two was one too."""

old_string = "five five was a race horse, two two was one too."
new_string = old_string.replace('five', 'one')
print(new_string)

"""7.	Write a Python program to which will print the triangle perimeter․
Triangle sides are 3, 4, 7
Expected Result: 14"""

a = 3
b = 4
c = 7
print(a + b + c)


"""8.	Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False """

value1 = 3
group1 = [1, 5, 8, 3]

if value1 in group1:
    print(True)
else:
    print(False)

value2 = -1
group2 = [1, 5, 8, 3]

if value2 in group2:
    print(True)
else:
    print(False)


"""9.	Write a Python program to solve (x + y) * (x + y). 
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49"""

x = 4
y = 3
z = (x + y) ** 2
print(f"({x} + {y}) ^ 2 = {z}")



"""10.Write a Python program which converts float values to integer, and sum of two values, then result print with reversed order.
Test Data: x = 2,5 , y = 13.75
Expected Output: 51"""

x = 2.5
y = 13.75
z = int(x) + int(y)
new_string = str(z)
print("".join(reversed(new_string)))
