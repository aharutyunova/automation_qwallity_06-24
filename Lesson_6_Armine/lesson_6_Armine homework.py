
'''
1.	Write a Python program to get the Fibonacci series between 0 to 50. 
Note : The Fibonacci Sequence is the series of numbers : 
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 0 1 1 2 3 5 8 13 21 34
'''

a = 0
b = 1
series_length = [0, 1, 2, 3, 4, 5, 6, 7]

print(a, b, end=' ')
for i in series_length:
    c = a + b
    a = b
    b = c
    print(c, end=' ')

print("\n")

  

'''
2.	Write a Python program that accepts a string and calculate the number of digits and letters.  
Sample Data: Python 3.2
Expected Output:
Letters 6
Digits 2
'''

Example_string = input("Python 3.2")
for i in Example_string:
alpha_count = 0
digit_count = 0
if i.isalpha():
      alpha_count = alpha_count + 1
elif:
      digit_count = digit_count + 1

print(digit_count) 
print(alpha_count)


'''
3.Write a Python program to print alphabet pattern 'L'
Expected Output:
*                                                                      
*                                                                      
*                                                                      
*                                                                      
*                                                                      
*                                                                      
*****
'''
 
list = ['*', '*', '*', '*', '*', '*']
for i in list: 
    print(i)
print('*****')


# I am thinking of around 4th and 5th exercises. I will push them as soon as I solve them))



