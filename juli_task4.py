#1.	Write a Python program to calculate the length of a string.
#my_string = ‘Here is string for your exercise!’

my_string = "Here is string for your exercise!"
print("lenght =" ,len(my_string))

#2.	Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
#Expected Result : 'w3ce'
#Sample String : 'w3'7
#Expected Result : 'w3w3'

str0 = "Barev Dzez"
print(str0[0] + str0[1] + str0[len(str0)-2] + str0[len(str0)-1])

#3.	Write a Python program to add 'ing' at the end of a given string.
#Sample String : 'abc'
#Expected Result : 'abcing'

str1 = "Hello"
print(str1 + "ing")

#4.	Write a Python program to replace ‘cut’ word to ‘dog’
#Sample String : 'I have a cat and I love it'
#Expected Result : 'I have a dog and I love it'

old_str = "I have a cat and I love it"
new_str = old_str.replace("cat", "dog")
print(new_str)

#5.	Write a Python program to reverse 123  to 321 in text.
#Sample String : ‘I have 123 books’
#Expected Result : 'I have 321 books'

str2 = "I have 123 books"
new_str3 = str2.replace("123",''.join(reversed("123")))
print(new_str3)

# 6.	Replace all occurrence of word five to one.
# Sample String : "five five was a race horse, two two was one too."
# Expected Result "one one was a race horse, two two was one too."

str3 = "five five was a race horse, two two was one too."
new_str3 = str3.replace("five","one")
print(new_str3)

# 7.	Write a Python program to which will print the triangle perimeter․
# Triangle sides are 3, 4, 7
# Expected Result: 14

a = 3
b = 4
c = 7
print(a + b + c)

# 8.	Write a Python program to check whether a specified value is contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

array = [1, 5, 8, 3]
print(5 in array)

array2 = [1, 5, 8, 3]
print(-1 in array2)

# 9.	Write a Python program to solve (x + y) * (x + y). 
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49

x = 4
y = 3
print((x + y)**2)

# 10.Write a Python program which converts float values to integer, and sum of two values, then result print with reversed order.
# Test Data: x = 2,5 , y = 13.75
# Expected Output: 51

x = 2.5
y = 13.75
sum = str(int(x) + int(y))
new_sum = ''.join(reversed(sum))
print(new_sum)
















