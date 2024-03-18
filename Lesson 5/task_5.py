
# 1 Write a Python program to sum all the items in a list.
mylist = [1, 2, 3, 3, 4, 5]
sum_mylist = 0
for i in mylist:
   sum_mylist += i
print (sum_mylist)
#another sulution
'''mylist = [1, 2, 3, 3, 4, 5]
print(sum(mylist))
'''
# 2 Write a Python program to remove duplicates from a list.
mylist = [1, 2, 3, 3, 4, 5]
myset = list(set(mylist))
print (myset)

# 3 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.
mylist = [1, 2, 3, 3, 4, 5]
mylist.pop(5)
mylist.pop(4)
mylist.pop(0)
print(mylist)
# 4 Write a Python program to get the difference between the two lists.
mylist1 = [1, 2, 3, 3, 4, 5]
mylist2 = [1, 2, 7]
diflist = []
for i in mylist1:
   if i not in mylist2:
        diflist.append(i)
for j in mylist2:
    if j not in mylist1:
        diflist.append(j)
print (diflist)
#another solution if you mean difference method of sets
mySet1 = set(mylist1)
mySet2 = set(mylist2)
dif = list(mySet1.difference(mySet2)) + list(mySet2.difference(mySet1))
print (dif)

# 5 Write a Python program to convert a tuple to a dictionary.-
mytuple = ('green', 'red', 'black', 'blue')
print(dict(enumerate(mytuple)))

# 6 Write a Python program to add a key to a dictionary.
mydict = { 
 "a": "1",
 "b": "2",
 "c": "3"
}
mydict["key"] = '4'
print (mydict)

# 7 Write a Python program to remove a key from a dictionary.
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
mylist =list(mydict.values()) 
print('minimum value is', sorted(mylist)[0])
print('maximum value is', sorted(mylist)[-1])

# 9 Write a Python program to create a union of sets.
set1 = {1, 2, 3, 4, 5}
set2 = {1, "b", "c", "d", "e"}
print(set1.union(set2))

# 10 Write a Python program to create a difference of two sets and print output. 
set1 = {1, 2, 3, 4, 5}
set2 = {1, "b", "c", "d", "e"}
print(set1.difference(set2))
