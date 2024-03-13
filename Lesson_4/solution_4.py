'''
1.	Write a Python program to calculate the length of a string.
my_string = ‘Here is string for your exercise!’
'''
my_string = "Here is string for your exercise!"
len_of_str = len(my_string)
print(len_of_str)

'''
2.	Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
Sample String : "w3resource"
Expected Result : "w3ce"
Sample String : "w3"
Expected Result : "w3w3"
'''
sample_str_1 = "w3resource"
expected_res_1 = sample_str_1[0:2] + sample_str_1[-2:]
print(expected_res_1)

sample_str_2 = "w3"
expected_res_2 = sample_str_2[0:2] + sample_str_2[-2:]
print(expected_res_2)

'''
3.	Write a Python program to add "ing" at the end of a given string.
Sample String : "abc"
Expected Result : "abcing"
'''
sample_str = "abc"
expected_res = sample_str + "ing"
print(expected_res)

'''
4.	Write a Python program to replace ‘cut’ word to ‘dog’
Sample String : "I have a cut and I love it"
Expected Result : "I have a dog and I love it"
'''
sample_str_4 = "I have a cut and I love it"
expected_res_4 = sample_str_4.replace("cut", "dog")
print(expected_res_4)

'''
5.	Write a Python program to reverse 123  to 321 in text.
Sample String : ‘I have 123 books’
Expected Result : "I have 321 books"
'''
sample_str_5 = "I have 123 books"
expected_res_5 = sample_str_5.replace("123", "321")
print(expected_res_5)

'''
6.	Replace all occurrence of word five to one.
Sample String : "five five was a race horse, two two was one too."
Expected Result "one one was a race horse, two two was one too."
'''
sample_str_6 = "five five was a race horse, two two was one too."
expected_res_6 = sample_str_6.replace("five", "one")
print(expected_res_6)

'''
7.	Write a Python program to which will print the triangle perimeter․
Triangle sides are 3, 4, 7
Expected Result: 14
'''
tr_side_a = 3
tr_side_b = 4
tr_side_c = 7
tr_perimeter = tr_side_a + tr_side_b + tr_side_c
print(tr_perimeter)

'''
8.	Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
'''
test_data_8 = [1, 5, 8, 3]
res_8_1 = "True" if 3 in test_data_8 else "False"
res_8_2 = "True" if -1 in test_data_8 else "False"
print(res_8_1, res_8_2)

'''
9.	Write a Python program to solve (x + y) * (x + y). 
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
'''
x = 4
y = 3
res_9 = (x + y) * (x + y)
print(f"(({x} + {y}) ^ 2) = {res_9}")

'''
10.Write a Python program which converts float values to integer, and sum of two values, then result print with reversed order.
Test Data: x = 2,5 , y = 13.75
Expected Output: 51
'''
x = 2.5
y = 13.75
res_10 = int(x) + int(y)
print(res_10)
reversed_res_10 = int(str(int(x) + int(y))[::-1])
print(reversed_res_10)
