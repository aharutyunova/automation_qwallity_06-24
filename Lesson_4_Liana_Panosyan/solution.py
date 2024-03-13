# 1.	Write a Python program to calculate the length of a string.
my_string = 'Here is string for your exercise!'

my_string = "Here is string for your exercise!"
print("The length of the given string is ", len(my_string))

# Anna - correct

# 2.	Write a Python program to get a string made of the first 2 and the
# last 2 chars from a given a string.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'

# my_string = input("Enter your string: ")
# print(my_string[0:2] + my_string[-2::])

# Anna - correct


# 3.	Write a Python program to add 'ing' at the end of a given string.
# Sample String : 'abc'
# Expected Result : 'abcing'

# sample_string = input("Enter your string: ")
# print("Expected string is ", sample_string + "ing")

# Anna - correct


# 4.	Write a Python program to replace ‘cut’ word to ‘dog’
# Sample String : 'I have a cut and I love it'
# Expected Result : 'I have a dog and I love it'

# given_string = "I have a cut and I love it"
# new_string = given_string.replace("cut", "dog")
# print(new_string)

# Anna - correct


# 5.	Write a Python program to reverse 123  to 321 in text.
# Sample String : ‘I have 123 books’
# Expected Result : 'I have 321 books'

# my_string = "I have 123 books"
# my_list = my_string.split()
# print("New string:", my_list[0], my_list[1], my_list[2][::-1], my_list[3])

# Anna - correct. You could also get 123 from the stirng reverce it and replace old value with new one


# 6.	Replace all occurrence of word five to one.
# Sample String : "five five was a race horse, two two was one too."
# Expected Result "one one was a race horse, two two was one too."

# sample_string = "five five was a race horse, two two was one too."
# expected_result = sample_string.replace("five", "one")
# print(expected_result)

# Anna - correct

# 7.	Write a Python program to which will print the triangle perimeter․
# Triangle sides are 3, 4, 7
# Expected Result: 14

# first_side = int(input("Enter the first side of the triangle։ "))
# second_side = int(input("Enter the second side of the triangle։ "))
# third_side = int(input("Enter the third side of the triangle: "))
# perimeter = first_side + second_side + third_side
# print("The perimeter of the triangle will be equal:")
# print(f"{first_side} + {second_side} + {third_side} =", perimeter)



# first_side = float(input("Enter the first side of the triangle։ "))
# second_side = float(input("Enter the second side of the triangle։ "))
# third_side = float(input("Enter the third side of the triangle: "))
# perimeter = first_side + second_side + third_side
# print("The perimeter of the triangle will be equal:")
# print(f"{first_side} + {second_side} + {third_side} =", perimeter)

# Anna - correct

# 8.	Write a Python program to check whether a specified value
# is contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

# given_list = [1, 5, 8, 3]
# specified_value = int(input("Enter a value: "))
# if specified_value in given_list:
#     print("True")
# else:
#     print("False")

# Anna - correct
    
# 9.	Write a Python program to solve (x + y) * (x + y).
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49

# x = int(input("x = "))
# y = int(input("y = "))
# print(f"({x} + {y}) ^ 2) = ", (x+y) ** 2)

# Anna - correct

# 10.Write a Python program which converts float values to integer,
# and sum of two values, then result print with reversed order.
# Test Data: x = 2,5 , y = 13.75
# Expected Output: 51

# x = float(input("Enter x: "))
# y = float(input("Enter y: "))
# sum_of_two_values = int(x) + int(y)
# result = str(sum_of_two_values)
# print("Expected Output:", result[::-1])

# Anna - correct, very good job Liana jan
