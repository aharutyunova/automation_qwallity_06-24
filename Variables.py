# 1.	Write a Python program to calculate the length of a string.
# my_string = ‘Here is string for your exercise!’

my_string = 'Here is string for your exercise!'
string_length = len(my_string)
print(string_length) 

# Anna - correct

# 2.Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'

sample_str = "w3resource"
expected_res = sample_str[0:2]+sample_str[-2:]
print(expected_res)
sample_str = "w3"
expected_res = sample_str[0:2]+sample_str[-2]
print(expected_res)

# Anna - for the second case the same combination  sample_str[0:2]+sample_str[-2:]


# 3. Write a Python program to add 'ing' at the end of a given string.
# Sample String : 'abc'
# Expected Result : 'abcing 

sample_str = "abc"
expected_res = sample_str+"ing"
print(expected_res)


# Anna - correct

# 4.	Write a Python program to replace ‘cut’ word to ‘dog’
# Sample String : 'I have a cut and I love it'
# Expected Result : 'I have a dog and I love it'

sample_str = "I have a cut and I love it"
expected_res = sample_str.replace("cut", "dog")
print(expected_res)


# Anna - correct

# 5.	Write a Python program to reverse 123  to 321 in text.
# Sample String : ‘I have 123 books’
# Expected Result : 'I have 321 books'

sample_str = "I have 123 books"
expected_res = sample_str.replace("123", "321")
print(expected_res)


# Anna - correct

# 6.	Replace all occurrence of word five to one.
# Sample String : "five five was a race horse, two two was one too."
# Expected Result "one one was a race horse, two two was one too."

sample_str = "five five was a race horse, two two was one too"
expected_res = sample_str.replace("five", "one")
print(expected_res)


# Anna - correct

# 7.	Write a Python program to which will print the triangle perimeter․
# Triangle sides are 3, 4, 7
# Expected Result: 14

tr_side_1 = 3
tr_side_2 = 4
tr_side_3 = 7
tr_perimeter = tr_side_1 + tr_side_2 + tr_side_3
print(tr_perimeter)


# Anna - correct

# 8. Write a Python program to check whether a specified value is contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False


test_data = [1, 5, 8, 3]
res_1 = "True" if 3 in test_data else "False"
res_2 = "True" if -1 in test_data else "False"
print(res_1, res_2)


# Anna - correct very good

# 9.	Write a Python program to solve (x + y) * (x + y). 
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49

x = 4
y = 3
print((x+y)**2)


# Anna - correct

# Mariam jan very good!!!


