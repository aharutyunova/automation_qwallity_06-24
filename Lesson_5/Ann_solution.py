# 1 Write a Python program to sum all the items in a list.
mylist = [1, 2, 3, 3, 4, 5]
total = (sum(mylist))
print("Sum all the ite ms in a list:", total)

# 2 Write a Python program to remove duplicates from a list.
mylist = [1, 2, 3, 3, 4, 5]
print("Remove duplicates from a list:", (list(set(mylist))))

# 3 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.
mylist = [1, 2, 3, 3, 4, 5]
remove_indices = [0, 4, 5]
new_list = [mylist[i] for i in range(len(mylist)) if i not in remove_indices]
print(new_list)

# 4 Write a Python program to get the difference between the two lists.
mylist = [1, 2, 3, 3, 4, 5]
mylist2 = [1, 2, 7]
print(list(set(mylist).difference(set(mylist2))))

# 5 Write a Python program to convert a tuple to a dictionary.-
mytuple = ('green', 'red', 'black', 'blue')
my_dict = {index: value for index, value in enumerate(mytuple)}
print(my_dict)

# 6 Write a Python program to add a key to a dictionary.
mydict = {
 "a": "1",
 "b": "2",
 "c": "3"
}
mydict["d"] = "4"
print(mydict)

# 7 Write a Python program to remove a key from a dictionary.
# Solution_1
mydict = {
 "a": "1",
 "b": "2",
 "c": "3"
}
del mydict["a"]
print(mydict)

# Solution_2
mydict = {
 "a": "1",
 "b": "2",
 "c": "3"
}
mydict.pop("a")
print(mydict)

# 8 Write a Python program to get the maximum and minimum value in a dictionary.
mydict = { 
 "a": "1",
 "b": "2",
 "c": "3"
}
print(max(mydict.values(), key=int))
print(min(mydict.values(), key=int))

# 9 Write a Python program to create a union of sets.
set1 = {1, 2, 3, 4, 5}
set2 = {1, "b", "c", "d", "e"}
union_set = set1.union(set2)
print(union_set)

# 10 Write a Python program to create a difference of two sets and print output. 
set1 = {1, 2, 3, 4, 5}
set2 = {1, "b", "c", "d", "e"}
# Solution_1
set1 = {1, 2, 3, 4, 5}
set2 = {1, "b", "c", "d", "e"}
print(set1.difference(set2))

# Solution_2
set1 = {1, 2, 3, 4, 5}
set2 = {1, "b", "c", "d", "e"}
difference_set = set1 - set2
print(difference_set)
