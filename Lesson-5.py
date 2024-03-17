# 1 Write a Python program to sum all the items in a list.
my_list = [1, 2, 3, 3, 4, 5]
total = 0
for number in my_list:
     total += number
print(total)

# Anna you wrote in a biy difficult way, you could write just print(sum(my_list))


# 2 Write a Python program to remove duplicates from a list.
mylist = [1, 2, 3, 3, 4, 5]
print(set(mylist))

# Anna - correct, will be better to bring result back to the list  - list(set(mylist))

# 3 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.

mylist = [1, 2, 3, 3, 4, 5]
          0  0  1  2  3  4
del mylist[:1]
del mylist[3:5]
print(mylist)

# Anna - correct

# 4 Write a Python program to get the difference between the two lists.

mylist = [1, 2, 3, 3, 4, 5]
mylist2 = [1, 2, 7]
difference = tuple(set(mylist) - set(mylist2))
print(difference)

# Anna - correct, why you don't return result as a list and return as a tuple

# 5 Write a Python program to convert a tuple to a dictionary.-
mytuple = ('green', 'red', 'black', 'blue')
dict = dict(enumerate(mytuple))
print(dict)

# Anna - could be as a solution

# 6 Write a Python program to add a key to a dictionary.
mydict = {
 "a": "1",
 "b": "2",
 "c": "3"
}
mydict["d"] = "4"
mydict["e"] = "5"
print(mydict)

# Anna - correct

# 7 Write a Python program to remove a key from a dictionary.
mydict = {
    "a": "1",
    "b": "2",
    "c": "3"
}
del mydict["c"]
print(mydict)

# Anna -correct

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

# Anna correct

# 9 Write a Python program to create a union of sets.
set1 = {1, 2, 3, 4, 5}
set2 = {1, "b", "c", "d", "e"}
myres = set1.union(set2)
print(myres)

# Anna - correct

# 10 Write a Python program to create a difference of two sets and print output.
set1 = {1, 2, 3, 4, 5}
set2 = {1, "b", "c", "d", "e"}
myres = set1.difference(set2)
print(myres)

# Anna - Coorect

# Mariam jan very good, hope you understand all solutions. In case some solutions are not clear for you lets discuss them