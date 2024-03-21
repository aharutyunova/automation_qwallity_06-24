'''
5.	Write a Python program to find the median of few values. 
Numbers: 15, 26, 28, 33   or   1, 4, 5, 6, 7

Example:
1, 3, 3, 6, 7, 8, 9

Median=6

1, 2, 3, 4, 5, 6, 8, 9, 
Median = (4+5)/2 = 4.5
'''


integer_list = [ 1, 4, 10, 9, 9, 7]
print (integer_list)
length = len(integer_list)
if length % 2 != 0:
    median = integer_list[int(length/2)]
    print('median is:', median)
else:
    median = float((integer_list[int(length / 2 - 1)] + integer_list[int(length / 2)]) / 2)
    print('median is:', median)

# Exactly :) The total homework is very very good!!!