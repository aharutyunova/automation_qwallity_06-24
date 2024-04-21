
# 1 Write a Python program to sum all the items in a list.
# mylist = [1, 2, 3, 3, 4, 5]

mylist = [1, 2, 3, 3, 4, 5]
print(sum(mylist))

# Anna - correct

# 2 Write a Python program to remove duplicates from a list.
# mylist = [1, 2, 3, 3, 4, 5]

mylist = [1, 2, 3, 3, 4, 5]
unique_set = set(mylist)
print(unique_set)

# Anna - correct

# 3 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.
# mylist = [1, 2, 3, 3, 4, 5]

mylist = [1, 2, 3, 3, 4, 5]
remove = [0, 4, 5]

mylist = [mylist[i] for i in range(len(mylist)) if i not in remove]

print("Print without removed int:", mylist)

# Anna - correct, interesting solution

# 4 Write a Python program to get the difference between the two lists.
# mylist = [1, 2, 3, 3, 4, 5]
# mylist2 = [1, 2, 7]

# int 7 does not print ?

mylist = [1, 2, 3, 3, 4, 5]
mylist2 = [1, 2, 7]

mylist3 = set(mylist) - set(mylist2)

print(mylist3)

# Anna - in case you wnat to get all values which are exists in one list and not in the second, you should also get

#  set(mylist2) - set(mylist)
# And as final result get all result from first and second sets

# 5 Write a Python program to convert a tuple to a dictionary.-
# mytuple = ('green', 'red', 'black', 'blue')

mytuple = ('green', 'red', 'black', 'blue')
dict = (mytuple)
print(dict)

# Anna - in this case you didn't convert dictionary to the tuple, for converting you should write
# dict(enumerate(mytuple))- will discuss enumarate tomorrow

# 6 Write a Python program to add a key to a dictionary.
# mydict = { "a": "1","b": "2","c": "3"}

mydict = { "a": "1","b": "2","c": "3"}
mydict["d"] = 4

print(mydict)

# Anna - correct

# 7 Write a Python program to remove a key from a dictionary.
# mydict = { "a": "1","b": "2","c": "3"}

# 1 exemple

mydict = { "a": "1","b": "2","c": "3"}
del mydict["a"]
print(mydict)

# 2 exemple

mydict = { "a": "1","b": "2","c": "3"}
mydict.pop("b")
print(mydict)

# Anna - correct

# 8 Write a Python program to get the maximum and minimum value in a dictionary.
# mydict = { "a": "1","b": "2","c": "3"}

# 1 max
mydict = { "a": "1","b": "2","c": "3"}
new = max(mydict)
print(mydict[new])



# 2 min
mydict = { "a": "1","b": "2","c": "3"}
new = min(mydict)
print(mydict[new])

# Anna - you should get max/min of dictionary values, so the solution was max(list(mydict.values())) the same for the min

# 9 Write a Python program to create a union of sets.
# set1 = {1, 2, 3, 4, 5}
# set2 = {1, "b", "c", "d", "e"}

# 1 exemple: added new set

set1 = {1, 2, 3, 4, 5}
set2 = {1, "b", "c", "d", "e"}

set3 = set1.union(set2)
print(set3)


# 2 exemple: merge in to set1

set1 = {1, 2, 3, 4, 5}
set2 = {1, "b", "c", "d", "e"}

set1.update(set2)
print(set1)

# Anna - correct

# 10 Write a Python program to create a difference of two sets and print output. 
# set1 = {1, 2, 3, 4, 5}
# set2 = {1, "b", "c", "d", "e"}

set1 = {1, 2, 3, 4, 5}
set2 = {1, "b", "c", "d", "e"}

set3 = set1 - set2
print(set3)

# Anna - correct

# Good job, please pay attention on task 5 and task 8 comments