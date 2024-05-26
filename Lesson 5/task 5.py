# 1 Write a Python program to sum all the items in a list.
# mylist = [1, 2, 3, 3, 4, 5]

my_list = [1, 2, 3, 3, 4, 5]
sum_total = sum(my_list)
print(sum_total)

# Anna - correct

# 2 Write a Python program to remove duplicates from a list.
# mylist = [1, 2, 3, 3, 4, 5]

my_list = [1, 2, 3, 3, 4, 5]
print(list(set(my_list)))

# Anna - correct

# 3 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.
# mylist = [1, 2, 3, 3, 4, 5]

mylist = [1, 2, 3, 3, 4, 5]
del mylist[:1]
del mylist[3:5]
print(mylist)

# Anna - correct

#another way of solving this task
mylist = [1, 2, 3, 3, 4, 5]
modified_list = mylist[1:4] + mylist[6:]
print(modified_list)

# Anna - why you need  mylist[6:] part in this solution?

# 4 Write a Python program to get the difference between the two lists.
# mylist = [1, 2, 3, 3, 4, 5]
# mylist2 = [1, 2, 7]

mylist = [1, 2, 3, 3, 4, 5]
mylist2 = [1, 2, 7]

x = set(mylist)
y = set(mylist2)
difference = x - y
result = list(difference)
print(result)

# Anna - correct

# another way of solving this task

mylist = [1, 2, 3, 3, 4, 5]
mylist2 = [1, 2, 7]
mylist = set(mylist)
mylist2 = set(mylist2)
result = mylist.difference(mylist2)
print(result)
# Anna - correct


# 5 Write a Python program to convert a tuple to a dictionary.-
# my_tuple = ('green', 'red', 'black', 'blue')

my_tuple = ('green', 'red', 'black', 'blue')
mydict = {value: index for index, value in enumerate(my_tuple)}
print(mydict)

# Anna - we didn't discuss for yet, but solution is correct


# another solution to this task
my_tuple = ("green", "red", "black", "blue")
my_tuple_2 = (1, 2, 3, 4)

if len(my_tuple) == len(my_tuple_2):
    resultDictionary = {my_tuple[i]: my_tuple_2[i] for i, _ in enumerate(my_tuple_2)}
print(resultDictionary)
# Anna - correct, but the most short solution was - print(dict(enumerate((my_tuple))))

# 6 Write a Python program to add a key to a dictionary.
'''
mydict = { 
 "a": "1",
 "b": "2",
 "c": "3"
}
'''
mydict = {
 "a": "1",
 "b": "2",
 "c": "3"
}
mydict["d"] = "4"
print(mydict)

# Anna - correct

# 7 Write a Python program to remove a key from a dictionary.
'''
mydict = { 
 "a": "1",
 "b": "2",
 "c": "3"
}
'''
# Remove key "c" using pop()
mydict = {
 "a": "1",
 "b": "2",
 "c": "3"
}
mydict.pop("c")
print(mydict)

# Anna - correct

# another way of solving this task is removing key "a" using del
mydict = {
 "a": "1",
 "b": "2",
 "c": "3"
}
del mydict["a"]
print(mydict)
# Anna - correct

#  8 Write a Python program to get the maximum and minimum value in a dictionary.
# mydict = {
#  "a": "1",
#  "b": "2",
#  "c": "3"
# }

mydict = {
            "a": "1",
            "b": "2",
            "c": "3"
}
max_value = max(mydict.values())
min_value = min(mydict.values())
print(max_value)
print(min_value)

# Anna - correct

# 9 Write a Python program to create a union of sets.
# set1 = {1, 2, 3, 4, 5}
# set2 = {1, "b", "c", "d", "e"}

set_1 = {1, 2, 3, 4, 5}
set_2 = {1, "b", "c", "d", "e"}
result = set_1.union(set_2)
print(result)

# Anna - correct


# 10 Write a Python program to create a difference of two sets and print output.
# set1 = {1, 2, 3, 4, 5}
# set2 = {1, "b", "c", "d", "e"}

set_1 = {1, 2, 3, 4, 5}
set_2 = {1, "b", "c", "d", "e"}
result = set_1.difference(set_2)
print(result)

# another method of solving this task

set_1 = {1, 2, 3, 4, 5}
set_2 = {1, "b", "c", "d", "e"}
difference = set_1 - set_2
print(difference)

# Anna - both solutions are correct

# Good job :)