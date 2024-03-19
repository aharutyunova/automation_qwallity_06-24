'''
1.	Write a Python program to get the Fibonacci series between 0 to 50. 
Note : The Fibonacci Sequence is the series of numbers : 
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 0 1 1 2 3 5 8 13 21 34
'''


def my_fibonachi():
    z = int(input("Please enter the number which will be the included border of  the fibonachi elements list\n"))
    # n = int(input("Please enter the number you want to see the fibonachi elements list\n"))
    if z < 0:
        print("Invalid value")
    elif z == 0:
        a = [0]
    elif z == 1:
        a = [0, 1]
    else:
        a = [0, 1]
        i = 2
        while not z <= a[i]:
            a.insert(i, a[i-1] + a[i-2])
            i = i+1
    print(a)
# not complite

'''
2.	Write a Python program that accepts a string and calculate the number of digits and letters.  
Sample Data: Python 3.2
Expected Output:
Letters 6
Digits 2
'''


def calculator_of_dig_num():
    my_string = input("Please enther the string you want to calculate\n")
    my_list = list(my_string)
    print(my_list)
    count_of_dig = 0
    count_of_str = 0
    for k in my_list:
        if k.isdigit():
            count_of_dig = count_of_dig + 1
        elif k.isalpha():
            count_of_str = count_of_str + 1
    print("Letters ", count_of_str, "\nDigits ", count_of_dig)

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


def drow_L():
    n = input("This program drow L, please enther the simbol you like\n")
    if len(n) > 1:
        print("Please enther only 1 symbol")
    else:
        if n == " " or n == "\n" or n == "\t":
            print("Please enther the visible simbol")
        else:
            i = 7
            while i > 0:
                if i == 1:
                    print(n, n, n, n, n)
                    i = i - 1
                else:
                    print(f"{n}\n")
                    i = i - 1


my_fibonachi()
# calculator_of_dig_num()
# drow_L()
