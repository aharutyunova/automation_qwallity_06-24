# 1.Write a Python program to calculate the length of a string
# my_string = ‘Here is string for your exercise!’ 
my_string = "Here is string for my exercise!"
y = len(my_string)
print(y)


# 2.Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
first_string = 'w3resource'
print(first_string[0:2])
print(first_string[8:10])
x = 'w3'
y = 'ce'
print(x+y)
print(x*2)

# 3.Write a Python program to add 'ing' at the end of a given string.
# Sample String : 'abc'
# Expected Result : 'abcing'
first_word = 'abc'
second_word = 'ing'
print(first_word+second_word)

# 4.Write a Python program to replace ‘cat’ word to ‘dog’
# Sample String : 'I have a cat and I love it
# Expected Result : 'I have a dog and I love it'
old_text = 'I have a cat and I love it'
new_text = old_text.replace('cat', 'dog')
print(new_text)

# 5.Write a Python program to reverse 123  to 321 in text.
# Sample String : ‘I have 123 books’
# Expected Result : 'I have 321 books'
book_string = 'I have 123 books'
numeric_value = '123'
print(''.join(reversed(numeric_value)))
old_sentence = 'I have 123 books' 
new_sentence = old_sentence.replace('123', '321')
print(new_sentence)
# Please, show me another solution to reverse only one word in the sentence))

# 6.Replace all occurrence of word five to one.
# Sample String : "five five was a race horse, two two was one too."
# Expected Result "one one was a race horse, two two was one too."
old_version = "five five was a race horse, two two was one too."
new_version = old_version.replace('five five', 'one one')
print(new_version)

# 7.Write a Python program to which will print the triangle perimeter․
# Triangle sides are 3, 4, 7
# Expected Result: 14
a = 3
b = 4
c = 7
print(a+b+c)

         
# 9.Write a Python program to solve (x + y) * (x + y). 
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49       
x = 4 
y = 3 
z = (x+y)
print(z)
print(z**2)

# 10.Write a Python program which converts float values to integer, and sum of two values, then result print with reversed order.
# Test Data: x = 2,5 , y = 13.75
# Expected Output: 51
x = 2.5
y = 13.75
z = int(x) + int(y)
print(z)
z = '15'
print(''.join(reversed(z)))

# 8.Write a Python program to check whether a specified value is contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False 

def list_function():
  list_1 = [1, 5, 8, 3] 
  h = 3 
if h in list_1:
       print(true)
    else 
       print(false) 
    e = -1 
if e in list_1
        print(true)
    else
         print(false)

# I was not able to write a code for this task that would work))