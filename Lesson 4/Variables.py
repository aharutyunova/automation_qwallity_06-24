# 1.a code that calculate the length of a string
my_string = "Here is string for your exercise!"
x = len(my_string)
print(x)

# 2.a code that get a string made of the first 2 and the last 2 chars from a given a string.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
sample_string = "w3resource"
print(sample_string[0:2] + sample_string[8:10])

# Sample String : 'w3'
# Expected Result : 'w3w3'
sample_string = "w3"
print(sample_string[0:2] + sample_string[0:2])

# 3.code that adds 'ing' at the end of a given string.
verb = "play"
suffix = "ing"
print(verb + suffix)


# 4.code to replace ‘cat’ word to ‘dog’
sentence = "I have a cat and I love it"
new_sentence = sentence.replace("cat", "dog")
print(new_sentence)


# 5. code that reverses 123  to 321 in text.
sentence = "I have 123 books"
reversed_sentence = sentence.replace("123", "321")
print(reversed_sentence)

# 6. code that replace all occurrence of word five to one.
txt = "five five was a race horse, two two was one too."
new_txt = txt.replace("five", "one")
print(new_txt)


# 7. code that will print the triangle perimeter․
triangle_side1 = 3
triangle_side2 = 4
triangle_side3 = 7
perimeter = triangle_side1 + triangle_side2 + triangle_side3
print(perimeter)


# 8. code that checks whether a specified value is contained in a group of values.
"""Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
"""
value1 = 3
group1 = [1, 5, 8, 3]

value2 = -1
group2 = [1, 5, 8, 3]

print(value1 in group1)
print(value2 in group2)


# 9. code that solves (x + y) * (x + y).
x = 4
y = 3
result = (x + y) ** 2
print(f"({x}+{y})^2 = {result}")

# another solution
x = 4
y = 3
print(f"({x}+{y})^2 = {(x+y)**2}")

# 10. code that converts float values to integer, and sum of two values, then result print with reversed order.
# Test Data: x = 2,5 , y = 13.75
# Expected Output: 51
x = 2.5
y = 13.75

print("".join(reversed(str(int(x)+int(y)))))
