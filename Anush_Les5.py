# 1 Write a Python program to sum all the items in a list.
mylist = [1, 2, 3, 3, 4, 5]
new_sum = sum(mylist)
print(new_sum)

# result` 18



# 2 Write a Python program to remove duplicates from a list.
mylist = [1, 2, 3, 3, 4, 5]


no_dub = set(mylist)
print(no_dub)
print(list(no_dub))
 
# 3 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.
mylist = [1, 2, 3, 3, 4, 5]

mylist_1 = mylist[1] + mylist[2] + mylist[3]
print(mylist_1) 
 
# 4 Write a Python program to get the difference between the two lists.
mylist = [1, 2, 3, 3, 4, 5]
mylist2 = [1, 2, 7]

x = set(mylist)
y = set(mylist2)
print(list(x.difference(y)))
 
 
# 5 ????????????????????????????????



# 6 Write a Python program to add a key to a dictionary.
mydict = { 
 "a": "1",
 "b": "2",
 "c": "3"
}

mydict["d"] = "4"
mydict["e"] = "5"
print(mydict)


# 7 Write a Python program to remove a key from a dictionary.
mydict = { 
 "a": "1",
 "b": "2",
 "c": "3"
}

print(mydict.pop("a"))
print(mydict)

# 8 Write a Python program to get the maximum and minimum value in a dictionary.

mydict = { 
    "a": "1",
    "b": "2",
    "c": "3"
}

max1 = max(mydict.values())
min1 = min(mydict.values())

print(max1)
print(min1)

# 9 Write a Python program to create a union of sets.
set1 = {1, 2, 3, 4, 5}
set2 = {1, "b", "c", "d", "e"}

x = set1.union(set2)
print(x)


# 10 Write a Python program to create a difference of two sets and print output. 
set1 = {1, 2, 3, 4, 5}
set2 = {1, "b", "c", "d", "e"}


x = set1.difference(set2)
print(x)



