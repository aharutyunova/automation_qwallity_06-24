
# 1 Write a Python program to sum all the items in a list.
mylist = [1, 2, 3, 3, 4, 5]

print(sum(mylist))

# 2 Write a Python program to remove duplicates from a list.
mylist = [1, 2, 3, 3, 4, 5]
print(list(dict.fromkeys(mylist)))

# 3 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.
mylist = [1, 2, 3, 3, 4, 5]

del(mylist[0])
del(mylist[3])
del(mylist[3])
print(mylist)


# 4 Write a Python program to get the difference between the two lists.
mylist = [1, 2, 3, 3, 4, 5]
mylist2 = [1, 2, 7]

x = set(mylist)
y = set(mylist2)

print(x.difference(y))
print(y.difference(x))

# 5 Write a Python program to convert a tuple to a dictionary.-
mytuple = ('green', 'red', 'black', 'blue')

print(dict(enumerate(mytuple)))

# 6 Write a Python program to add a key to a dictionary.
mydict = { 
 "a": "1",
 "b": "2",
 "c": "3"
}

print(mydict.keys())

# 7 Write a Python program to remove a key from a dictionary.
mydict = { 
 "a": "1",
 "b": "2",
 "c": "3"
}
del mydict["a"]
print(mydict)

# 8 Write a Python program to get the maximum and minimum value in a dictionary.
mydict = { 
 "a": "1",
 "b": "2",
 "c": "3"
}

print("Maximum value =",max(mydict.values()))
print("Minumum value =",min(mydict.values()))

# 9 Write a Python program to create a union of sets.
set1 = {1, 2, 3, 4, 5}
set2 = {1, "b", "c", "d", "e"}

print(set1.union(set2))
print(set2.union(set1))

# 10 Write a Python program to create a difference of two sets and print output. 
set1 = {1, 2, 3, 4, 5}
set2 = {1, "b", "c", "d", "e"}

print(set1.difference(set2))
print(set2.difference(set1))
