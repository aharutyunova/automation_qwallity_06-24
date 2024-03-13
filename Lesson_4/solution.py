
''' 1. Write a Python program to calculate the length of a string.
my_string = 'Here is string for your exercise!' '''
my_string = "Here is string for your exercise!"
print(len(my_string))

# Anna - correct
'''
2.	Write a Python program to get a string made of the first 2
and the last 2 chars from a given a string.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : "w3w3"'''
sample_string = "w3resource"
x = sample_string
print(x[:2] + x[-2:])
sample_string = "w3"
x = sample_string
print(x[:2] + x[:2])
# Anna - for second case you also should use the same  x[:2]+x[-2:]

'''
3.	Write a Python program to add 'ing' at the end of a given string.
Sample String : 'abc'
Expected Result : "abcing"'''
sample_string = "abc"
print(sample_string + "ing")

# Anna - correct

'''
4.	Write a Python program to replace 'cut' word to 'dog'
Sample String : 'I have a cut and I love it'
Expected Result : "I have a dog and I love it"'''
sample_string = "I have a cut and I love it"
new_string = sample_string.replace("cut", "dog")
print(new_string)

# Anna - correct

'''
5.	Write a Python program to reverse 123  to 321 in text.
Sample String : 'I have 123 books'
Expected Result : "I have 321 books" '''
sample_string = "I have 123 books"
string_list = sample_string.split()
reverse_number = string_list[2][::-1]
string_list[2] = reverse_number
result_string = " ".join(string_list)
print(result_string)

# Anna - correct

'''
6.	Replace all occurrence of word five to one.
Sample String : "five five was a race horse, two two was one too."
Expected Result "one one was a race horse, two two was one too." '''
sample_string = "five five was a race horse, two two was one too."
new_string = sample_string.replace("five", "one")
print(new_string)

# Anna - correct

'''
7.	Write a Python program to which will print the triangle perimeter.
Triangle sides are 3, 4, 7
Expected Result: 14 '''
side_1 = 3
side_2 = 4
side_3 = 7
perimeter = side_1 + side_2 + side_3
print(f"{perimeter}")

# Anna - correct

'''
8. Write a Python program to check whether a specified value is
contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False '''
specified_value1 = 3
group1 = [1, 5, 8, 3]
specified_value2 = -1
group2 = [1, 5, 8, 3]
is_contained1 = specified_value1 in group1
is_contained2 = specified_value2 in group2
print(f"{specified_value1} is in {group1}: {is_contained1}")
print(f"{specified_value2} is in {group2}: {is_contained2}")

# Anna - correct Good

'''
9.	Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49 '''
# Example_1
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
result = (x + y) * (x + y)
print("({} + {}) ^ 2 = {}".format(x, y, result))
# Example_2
x = 4
y = 3
result = (x + y) * (x + y)
print("({} + {}) ^ 2 = {}".format(x, y, result))

# Anna - correct Good

''' 10. Write a Python program which converts float values to integer, and sum
 of two values, then result print with reversed order.
Test Data: x = 2,5 , y = 13.75
Expected Output: 51 '''
x = 2.5
y = 13.75
sum_result = int(x) + int(y)
print(f"Sum: {sum_result}, Reversed: {str(sum_result)[::-1]}")

# Anna - correct Good

# Good job An jan
