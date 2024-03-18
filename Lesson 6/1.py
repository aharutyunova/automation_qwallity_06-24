'''
1.	Write a Python program to get the Fibonacci series between 0 to 50. 
Note : The Fibonacci Sequence is the series of numbers : 
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 0 1 1 2 3 5 8 13 21 34
'''
a = 0
b = 1
n = 2
c = a + b
print( a,b, end = ' ')
while c < 50:
    print(c, end = ' ')
    a = b
    b = c
    c = a + b
    n = n + 1

