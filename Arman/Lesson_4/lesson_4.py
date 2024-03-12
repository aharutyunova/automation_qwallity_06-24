# 1. Write a Python program to calculate the length of a string.
my_string = "Here is string for your exercise!"
length_of_str = len(my_string)
print(f"Length of a string is {length_of_str}")

'''
2. Write a Python program to get a string made of the first 2 and the last
2 chars from a given a string.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
'''

sample_string = "w3resource"
sample_string_two = "w3"
first_flast_char = sample_string[0:2] + sample_string[-2:]
second_flast_char = sample_string_two[0:2] + sample_string_two[-2:]
print(first_flast_char)
print(second_flast_char)

'''
3. Write a Python program to add 'ing' at the end of a given string.
Sample String : 'abc'
Expected Result : 'abcing'
'''

chars = "abc"
add_ing = chars + "ing"
print(add_ing)

'''
4. Write a Python program to replace ‘cut’ word to ‘dog’
Sample String : 'I have a cut and I love it'
Expected Result : 'I have a dog and I love it'
'''

cut_str = "I have a cut and I love it"
dog_str = cut_str.replace("cut", "dog")
print(dog_str)

'''
# 5. Write a Python program to reverse 123  to 321 in text.
# Sample String : ‘I have 123 books’
# Expected Result : 'I have 321 books'
'''

books_str = "I have 123 books"
str_list = books_str.split()
reverse_number = str_list[2][::-1]
str_list[2] = reverse_number
result_str = " ".join(str_list)
print(result_str)

'''
# 6. Replace all occurrence of word five to one.
# Sample String : "five five was a race horse, two two was one too."
# Expected Result "one one was a race horse, two two was one too."
'''

five_str = "five five was a race horse, two two was one too."
five_to_one = five_str.replace("five", "one")
print(five_to_one)

'''
7. Write a Python program to which will print the triangle perimeter․
Triangle sides are 3, 4, 7
Expected Result: 14
'''

triangle_first_side = int(input("Enter triangle first side: "))
triangle_second_side = int(input("Enter triangle second side: "))
triangle_third_side = int(input("Enter triangle third side: "))
triangle_perimeter = triangle_first_side + triangle_second_side + triangle_third_side
print(triangle_perimeter)

'''
8. Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
'''

numbers_list = [1, 5, 8, 3]
ask_for_number = int(input("Enter a number to check existence in list: "))
if ask_for_number in numbers_list:
    print(True)
else:
    print(False)

'''
9. Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
'''

ask_first_number = int(input("Enter first number: "))
ask_second_number = int(input("Enter second number: "))
result = (ask_first_number + ask_second_number) * (ask_first_number + ask_second_number)
print(result)

'''
10. Write a Python program which converts float values to integer, and sum
of two values, then result print with reversed order.
Test Data: x = 2,5 , y = 13.75
Expected Output: 51
'''

first_float_number = float(input("Enter first float number: "))
second_float_number = float(input("Enter first float number: "))
sum_float_numbers = int(first_float_number) + int(second_float_number)
reversed_result_number = str(sum_float_numbers)[::-1]
print(reversed_result_number)
