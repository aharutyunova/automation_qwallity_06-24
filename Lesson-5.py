# 1 Write a Python program to sum all the items in a list.
my_list = [1, 2, 3, 3, 4, 5]
total = 0
for number in my_list:
     total += number
print(total)


# 2 Write a Python program to remove duplicates from a list.
mylist = [1, 2, 3, 3, 4, 5]
print(set(mylist))




# 3 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.

mylist = [1, 2, 3, 3, 4, 5]
del mylist[:1]
del mylist[3:5]
print(mylist)


# 4 Write a Python program to get the difference between the two lists.

mylist = [1, 2, 3, 3, 4, 5]
mylist2 = [1, 2, 7]
difference = tuple(set(mylist) - set(mylist2))
print(difference)


# 5 Write a Python program to convert a tuple to a dictionary.-
mytuple = ('green', 'red', 'black', 'blue')
dict = dict(enumerate(mytuple))
print(dict)


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
del mydict["c"]
print(mydict)


#  8 Write a Python program to get the maximum and minimum value in a dictionary.
mydict = {
"a": "1",
"b": "2",
"c": "3"
 }
min = min(mydict.values())
max = max(mydict.values())
print(min)
print(max)


# 9 Write a Python program to create a union of sets.
set1 = {1, 2, 3, 4, 5}
set2 = {1, "b", "c", "d", "e"}
myres = set1.union(set2)
print(myres)


# 10 Write a Python program to create a difference of two sets and print output.
set1 = {1, 2, 3, 4, 5}
set2 = {1, "b", "c", "d", "e"}
myres = set1.difference(set2)
print(myres)