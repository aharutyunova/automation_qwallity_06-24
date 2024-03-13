# 1.	Write a Python program to calculate the length of a string.
# my_string = ‘Here is string for your exercise!’

print(len("Here is string for your exercise!"))


# 2.	Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'


def get_str(text):
    if len(text) < 2:
        return ""
    return text[:2] + text[-2:]


new_str = input("enter a str : ")
print("new string: ", get_str(new_str))


# 3.	Write a Python program to add 'ing' at the end of a given string.
# Sample String : 'abc'
# Expected Result : 'abcing'


text = input("enter a string")

if len(text) < 3:
   print(text)
elif text[-3:] == "ing":
    print(text + "ly")
else: 
    print(text + "ing")



# 4.	Write a Python program to replace ‘cut’ word to ‘dog’
# Sample String : 'I have a cut and I love it'
# Expected Result : 'I have a dog and I love it'
    
sample_str=input("I have a cut and I love it")
changeable_word=input("cut")
replace_word=input("dog")

print(sample_str)

replace_str=sample_str.replace(changeable_word,replace_word)
print(expected_result)




# 5.	Write a Python program to reverse 123  to 321 in text.
# Sample String : ‘I have 123 books’
# Expected Result : 'I have 321 books'


number_str = input("I have 123 books:")

number_str_reversed = number_str[::-1]

print(number_str_reversed)



# 6.	Replace all occurrence of word five to one.
# Sample String : "five five was a race horse, two two was one too."
# Expected Result "one one was a race horse, two two was one too."

filename = input("point6: ")
find = input("five: ")
replace = input("one: ")

with open(filename) as file:
    contents = file.read()
    contents = contents.replace(find,replace)



# 7.	Write a Python program to which will print the triangle perimeter․
# Triangle sides are 3, 4, 7
# Expected Result: 14
    

    first_side_a = float(input("3"))
    second_side_b = float(input("4"))
    third_side_c = float(input("7"))
    p = first_side_a + second_side_b + third_side_c
    print("Perimeter: ", p)

# 8.	Write a Python program to check whether a specified value is contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False
    


def check_value(specified_value, group_of_values):
    return specified_value in group_of_values

specified_value1 = 3
group_of_values1 = [1, 5, 8, 3]
result1 = check_value(specified_value1, group_of_values1)
print(f"{specified_value1} -> {group_of_values1} : {result1}")

specified_value2 = -1
group_of_values2 = [1, 5, 8, 3]
result2 = check_value(specified_value2, group_of_values2)
print(f"{specified_value2} -> {group_of_values2} : {result2}")



# 9.	Write a Python program to solve (x + y) * (x + y). 
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49


x = 4
y = 3

def solve_expression(x, y):
    result = (x + y) * (x + y)
    return result

output = solve_expression(x, y)
print(f"({x} + {y}) ^ 2 = {output}")

# 10.Write a Python program which converts float values to integer, and sum of two values, then result print with reversed order.
# Test Data: x = 2,5 , y = 13.75
# Expected Output: 51


def convert_and_sum(x, y):

    x_int = int(x)
    y_int = int(y)

    result = x_int + y_int

    reversed_result = int(str(result)[::-1])

    return reversed_result

x = 2.5
y = 13.75
output = convert_and_sum(x, y)
print("Expected Output:", output)