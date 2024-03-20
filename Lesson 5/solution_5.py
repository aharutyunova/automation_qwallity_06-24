
# 1 Write a Python program to sum all the items in a list.
mylist = [1, 2, 3, 3, 4, 5]
total_sum = sum(mylist)

print("Ex. 1")
print("Sum of mylist = ", total_sum)

# 2 Write a Python program to remove duplicates from a list.
mylist = [1, 2, 3, 3, 4, 5]
new_list = list(set(mylist))

print("\nEx. 2")
print("The old list with duplicate items: ", mylist)
print("The new list with unique items: ", new_list)

# 3 Write a Python program which print a specified list after removing the 0th,
# 4th and 5th elements.
mylist = [1, 2, 3, 3, 4, 5]
modified_list = mylist[1:4] + mylist[6:]

print("\nEx. 3")
print("Modified list:", modified_list)

# 4 Write a Python program to get the difference between the two lists.
mylist_4_1 = [1, 2, 3, 3, 4, 5]
mylist_4_2 = [1, 2, 7]

set_1 = set(mylist_4_1)
set_2 = set(mylist_4_2)

print("\nEx. 4")
print(set_1.difference(set_2))

# 5 Write a Python program to convert a tuple to a dictionary.-
mytuple = ('green', 'red', 'black', 'blue')
result_dict = {index: value for index, value in enumerate(mytuple)}

print("\nEx. 5")
print("Converted dictionary:", result_dict)

# 6 Write a Python program to add a key to a dictionary.
mydict = { 
    "a": "1",
    "b": "2",
    "c": "3"
}

mydict["d"] = "4"

print("\nEx. 6")
print("Updated dictionary:", mydict)

# 7 Write a Python program to remove a key from a dictionary.
mydict = { 
    "a": "1",
    "b": "2",
    "c": "3"
}
mydict.pop('b')

print("\nEx. 7")
print("Updated dictionary:", mydict)

# 8 Write a Python program to get the maximum and minimum value in a
# dictionary.
mydict = {
    "a": "1",
    "b": "2",
    "c": "3"
}
max_value = max(int(value) for value in mydict.values())
min_value = min(int(value) for value in mydict.values())

print("\nEx. 8")
print("Maximum value in the dictionary:", max_value)
print("Minimum value in the dictionary:", min_value)

# 9 Write a Python program to create a union of sets.
set1 = {1, 2, 3, 4, 5}
set2 = {1, "b", "c", "d", "e"}
union_set = set1.union(set2)

print("\nEx. 9")
print("Union of sets:", union_set)

# 10 Write a Python program to create a difference of two sets and print
# output. 
set1 = {1, 2, 3, 4, 5}
set2 = {1, "b", "c", "d", "e"}
difference_set = set1 - set2

print("\nEx. 10")
print("Difference of sets:", difference_set)
