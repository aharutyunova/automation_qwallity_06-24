# 1 Write a Python program to sum all the items in a list.
mylist = [1, 2, 3, 3, 4, 5]
print(sum(mylist))

# Anna - correct

# 2 Write a Python program to remove duplicates from a list.
mylist = [1, 2, 3, 3, 4, 5]
duplicate =(list(set(mylist)))
print(duplicate)

# Anna - correct

# 3 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.
mylist = [1, 2, 3, 3, 4, 5]
del mylist[0] 
del mylist [3] # 4-1 = 3
del mylist [2] # 5-1-1 = 3 why index 2 in this line
print(mylist)


# 4 Write a Python program to get the difference between the two lists.
mylist = [1, 2, 3, 3, 4, 5]
mylist2 = [1, 2, 7]
difference = list(set(mylist) - set(mylist2))
print(difference)

# Anna - correct

# 5 Write a Python program to convert a tuple to a dictionary.-
my_tuple = ('green', 'red', 'black', 'blue')
list_1 = enumerate(my_tuple)
print(dict(enumerate(my_tuple)))

# Anna - correct

# 6 Write a Python program to add a key to a dictionary.
mydict = {
    "a": "1",
    "b": "2",
    "c": "3"
}
mydict.update({"d": "4"})
print(mydict)

dict.update({'key3': 'geeks'})
print(dict)

# Anna corerct only in line 46/47 maybe you mean mydict instead of dict


# 7 Write a Python program to remove a key from a dictionary.
mydict = {
    "a": "1",
    "b": "2",
    "c": "3"
}

del mydict["a"]
print(mydict)

# Anna - correct

# 8 Write a Python program to get the maximum and minimum value in a dictionary.
mydict = {
    "a": "1",
    "b": "2",
    "c": "3"
}
print(min(mydict))
print(max(mydict))

# Anna - here you need get min/max of dict values, so correct solution is min(list(mydict.values())) / max(list(mydict.values()))

# 9 Write a Python program to create a union of sets.
set1 = {1, 2, 3, 4, 5}
set2 = {1, "b", "c", "d", "e"}
set_mix = set1.union(set2)
print(set_mix)

# Anna - correct

# 10 Write a Python program to create a difference of two sets and print output.
set1 = {1, 2, 3, 4, 5}
set2 = {1, "b", "c", "d", "e"}

set_difference = set1.intersection(set2)
print(set_difference)


# Anna - why intersection not difference?

# Anna - Generally almost all tasks are correct :)