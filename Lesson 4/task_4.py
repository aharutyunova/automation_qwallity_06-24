#1.	Write a Python program to calculate the length of a string.
#my_string = ‘Here is string for your exercise!’
my_string = 'Here is string for your exercise!'
print(my_string, '- length of my_string is', len(my_string));
#another solution
'''input_my_string = input()
print('Inputed string length is', len(input_my_string), sep = ' - ')
'''
# Anna - correct

#2.	Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
#Sample String : 'w3resource'
#Expected Result : 'w3ce'
#Sample String : 'w3'
#Expected Result : 'w3w3' """ 
Sample_String = 'w3resource'
last_index = len(Sample_String)-1
print('Expected result is', Sample_String[0:2]+ Sample_String[(last_index-1):], sep = ' - ')

#another solution
'''input_Sample_String = input()
last_index = len(input_Sample_String)-1;
print('Expected result is', input_Sample_String[0:2] + input_Sample_String[(last_index-1):], sep = ' - ')
'''
# Anna - correct

#3.	Write a Python program to add 'ing' at the end of a given string.
#Sample String : 'abc'
#Expected Result : 'abcing'
Sample_String = 'abc'
Expected_Result = Sample_String + 'ing'
print(Expected_Result)
#another solution
'''input_Sample_String = input()
Expected_Result = input_Sample_String + 'ing'
print(Expected_Result)
'''

# Anna - correct

#4.	Write a Python program to replace ‘cut’ word to ‘dog’
#Sample String : 'I have a cat and I love it'
#Expected Result : 'I have a dog and I love it'
Sample_String = 'I have a cat and I love it'
Expected_Result = Sample_String.replace('cat', 'dog')
print (Expected_Result)

# Anna - correct

#5.	Write a Python program to reverse 123  to 321 in text.
#Sample String : ‘I have 123 books’
#Expected Result : 'I have 321 books'
Sample_String = 'I have 123 books'
Expected_Result = Sample_String.replace('123', '321')
print (Expected_Result)



#another solution
'''print('input count of books:')
quantity = input()
quantity_reversed = quantity[::-1];
Sample_String = f'I have {quantity_reversed} books'
print (Sample_String)
'''
# Anna - correct

#6.	Replace all occurrence of word five to one.
#Sample String : "five five was a race horse, two two was one too."
#Expected Result "one one was a race horse, two two was one too."
Sample_String = "five five was a race horse, two two was one too."
Expected_Result = Sample_String.replace('five','one')
print(Expected_Result)

# Anna - correct

#7.	Write a Python program to which will print the triangle perimeter․
#Triangle sides are 3, 4, 7
#Expected Result: 14
a,b,c = {3,4,7}
Triangle_Perimeter = a + b + c
print('Triangle sides are ', a, ',', b, ',', c, ',','Triangle_Perimeter is equal to - ',Triangle_Perimeter)

# Anna - correct

#8.	Write a Python program to check whether a specified value is contained in a group of values.
#Test Data :
#3 -> [1, 5, 8, 3] : True
#-1 -> [1, 5, 8, 3] : False
list = [1, 5, 8, 3]
element1 = 3
element2 = -1
print(f'{element1} -> {list} :', list.count(element1) != 0)
print(f'{element2} -> {list} :', list.count(element2) != 0)

# Anna - correct

#9.	Write a Python program to solve (x + y) * (x + y). 
#Test Data : x = 4, y = 3
#Expected Output : (4 + 3) ^ 2) = 49
x = 4 
y = 3
print(f'({x}+{y})^ 2 =', (x + y)**2)

# Anna - correct

#another solution
'''x = int(input('input first number '))
y = int(input('input second number '))
print(f'({x}+{y})^ 2 =', (x + y)**2)
'''

#10.Write a Python program which converts float values to integer, and sum of two values, then result print with reversed order.
#Test Data: x = 2,5 , y = 13.75
#Expected Output: 51
x = 2.5
y = 13.75
print(f'convert {x} and {y} to integer, sum result in reversed order is', str(int(x) + int(y))[::-1])

# Anna - correct

# Very Good!!!