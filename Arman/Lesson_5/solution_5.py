# 1 Write a Python program to sum all the items in a list.
my_list_one = [1, 2, 3, 3, 4, 5]
temp = 0
for number in my_list_one:
    temp += number
print(f"Sum all items in a list is: {temp}")

# Anna - you could use sum , but your solution more detailed :) - Correct

# 2 Write a Python program to remove duplicates from a list.

# 2.1 Solution 1
my_list_two = [1, 2, 3, 3, 4, 5]
no_duplicates_list = list(set(my_list_two))
print(f"No duplicates in the list solution 1: {no_duplicates_list}")

# 2.2 Solution 2
no_duplicate = []
for number in my_list_two:
    if number not in no_duplicate:
        no_duplicate.append(number)
print(f"No duplicates in the list solution 2: {no_duplicate}")

# Anna - first solution more simple and practical

# 3 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.
my_list_three = [1, 2, 3, 3, 4, 5]
indices_to_remove = [0, 4, 5]
result_list = []
for index, value in enumerate(my_list_three):
    if index not in indices_to_remove:
        result_list.append(value)
print(result_list)

# Anna - good solution

# 4 Write a Python program to get the difference between the two lists.
my_list_four = [1, 2, 3, 3, 4, 5]
my_list_five = [1, 2, 7]
difference_list = []
for number in my_list_four:
    if number not in my_list_five:
        difference_list.append(number)
print(f"Difference list: {difference_list}")

# Anna - correct, you also could convert lists to the set and get difference of that sets

# 5 Write a Python program to convert a tuple to a dictionary.-
my_tuple = ('green', 'red', 'black', 'blue')
to_dictionary = dict(enumerate(my_tuple))
print(to_dictionary)

# Anna - correct

# 6 Write a Python program to add a key to a dictionary.
my_dict = {"a": "1", "b": "2", "c": "3", "d": 4, "e": 5, "f": 6}
print(my_dict)

# Anna - to show add step you could have in the code something like
#  my_dict[k] = 10

# 7 Write a Python program to remove a key from a dictionary.
my_dict_two = {
    "a": "1",
    "b": "2",
    "c": "3"
}
for key in my_dict_two.keys():
    if key == "b":
        del my_dict_two[key]
        break
print(my_dict_two)

# Anna - correct and complex solution for more simple way you could use del my_dict_two["a"]

# 8 Write a Python program to get the maximum and minimum value in a dictionary.
my_dict_three = {
    "a": "1",
    "b": "2",
    "c": "3"
}
number_list = list(my_dict_three.values())
minimum_value = min(number_list)
maximum_value = max(number_list)
print(f"Minimum value in the list is: {minimum_value} \n"
      f"Maximum value in the list is: {maximum_value}")

# Anna - correct

# 9 Write a Python program to create a union of sets.
set_one = {1, 2, 3, 4, 5}
set_two = {1, "b", "c", "d", "e"}
sets_union = set_one.union(set_two)
print(sets_union)

# Anna - correct

# 10 Write a Python program to create a difference of two sets and print output.

# 10.1 Solution 1
set_three = {1, 2, 3, 4, 5}
set_four = {1, "b", "c", "d", "e"}
sets_difference = []
for item in set_three:
    if item not in set_four:
        sets_difference.append(item)
print(sets_difference)

# 10.2 Solution 1
difference = set_three - set_four
print(f"Difference between set_three and set_four: {difference}")

# Anna -  second solution more simple

# Very good as usual :) Only wherever you can use more simple solutions give preference to it
