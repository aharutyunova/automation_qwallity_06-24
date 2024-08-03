# # 1 Write a Python program to sum all the items in a list.
# mylist = [1, 2, 3, 3, 4, 5]

# print("Let's build the list, all the elements of which need to be added.")
# elements_count = int(input("How many elements the list should contain: "))
# my_list = []
# while elements_count > 0:
#     list_element = int(input("Import list element: "))
#     my_list.append(list_element)
#     elements_count -= 1
# sum_of_elements = 0
# for i in my_list:
#     sum_of_elements += i
# print("The sum of the elements of the resulting list will be:")
# print(sum_of_elements)

# # Anna - very complex solution :) Good enough but I expect only sum(any list) :)

# # 2 Write a Python program to remove duplicates from a list.
# # mylist = [1, 2, 3, 3, 4, 5]

# print("Let's build the list")
# elements_count = int(input("How many elements the list should contain: "))
# my_list = []
# while elements_count > 0:
#     list_element = int(input("Import list element: "))
#     my_list.append(list_element)
#     elements_count -= 1
#     new_list = list(set(my_list))
# print("The list containing duplicates", my_list)
# print("The list without duplicates", new_list)

# Anna - here will be more simple to convert list to the set

# 3 Write a Python program which print a specified list after removing
# the 0th, 4th and 5th elements.
# mylist = [1, 2, 3, 3, 4, 5]

print("Let's build the list")
elements_count = int(input("How many elements the list should contain: "))
my_list = []
while elements_count > 0:
    list_element = int(input("Import list element: "))
    my_list.append(list_element)
    elements_count -= 1
new_list = my_list[1:4] + my_list[6:]
print("The resulting list will be:", new_list)

# Anna - why you need my_list[6:] part here? 

print("Let's build the list")
elements_count = int(input("How many elements the list should contain: "))
my_list = []
while elements_count > 0:
    list_element = int(input("Import list element: "))
    my_list.append(list_element)
    elements_count -= 1
my_list.pop(5)
my_list.pop(4)
my_list.pop(0)
print("The resulting list will be:", my_list)

# Anna the result is correct but solution more than enouth for this case 

# 4 Write a Python program to get the difference between the two lists.
# mylist = [1, 2, 3, 3, 4, 5]
# mylist2 = [1, 2, 7]

print("Let's build the first list")
elements_count = int(input("How many elements first list should contain:"))
my_list_1 = []
while elements_count > 0:
    list_element = int(input("Import list element: "))
    my_list_1.append(list_element)
    elements_count -= 1
print("Let's build the second list")
elem_count_2 = int(input("How many elements second list should contain:"))
my_list_2 = []
while elem_count_2 > 0:
    list_element_2 = int(input("Import list element: "))
    my_list_2.append(list_element_2)
    elem_count_2 -= 1
difference_between_two_lists = []
for i in my_list_1:
    if i not in my_list_2:
        difference_between_two_lists.append(i)

print("The difference between the two lists:")
print(list(set(difference_between_two_lists)))


# Anna - you just coyld convert lists to the set and get difference. Not all solutions should be long and use loopsm if else etx
#  Good solution not always long solution, it should be as simple as possible

# 5 Write a Python program to convert a tuple to a dictionary.
# mytuple = ('green', 'red', 'black', 'blue')

my_tuple = ("green", "red", "black", "blue")
my_dict = dict(enumerate(my_tuple))
print("The resulting Dictionary will be։", my_dict)
# Anna - correct


# 6 Write a Python program to add a key to a dictionary.
# mydict = {
#  "a": "1",
#  "b": "2",
#  "c": "3"
# }

# my_dict = {
#  "a": "1",
#  "b": "2",
#  "c": "3"
# }
# my_dict["d"] = "4"
# print("The new Dictionary will be:", my_dict)

# Anna-correct

# 7 Write a Python program to remove a key from a dictionary.
# mydict = {
#  "a": "1",
#  "b": "2",
#  "c": "3"
# }

# my_dict = {
#  "a": "1",
#  "b": "2",
#  "c": "3"
# }
# my_dict.pop("a")


# print("The new Dictionary will be:", my_dict)


# Anna -correct

# 8 Write a Python program to get the maximum and minimum
# value in a dictionary.
# mydict = {
#  "a": "1",
#  "b": "2",
#  "c": "3"
# }

# mydict = {
#  "a": "1",
#  "b": "2",
#  "c": "3"
# }
# my_list = list(mydict.values())
# my_list.sort()
# print("The minimum value of the Dictionary:", my_list[0])
# print("The maximum value of the Dictionary:", my_list[-1])


# Anna -correct

# 9 Write a Python program to create a union of sets.
# set1 = {1, 2, 3, 4, 5}
# set2 = {1, "b", "c", "d", "e"}

# my_set_1 = {1, 2, 3, 4, 5}
# my_set_2 = {1, "b", "c", "d", "e"}
# new_set = my_set_1.union(my_set_2)
# print("The union of two sets:", new_set)


# Anna -correct

# 10 Write a Python program to create a difference of two sets
# and print output.
# set1 = {1, 2, 3, 4, 5}
# set2 = {1, "b", "c", "d", "e"}

# my_set_1 = {1, 2, 3, 4, 5}
# my_set_2 = {1, "b", "c", "d", "e"}
# my_list = []
# for i in my_set_1:
#     if i not in my_set_2:
#         my_list.append(i)
# print("The difference between the two given sets.", set(my_list))

# my_set_1 = {1, 2, 3, 4, 5}
# my_set_2 = {1, "b", "c", "d", "e"}
# new_set = my_set_1.difference(my_set_2)
# print("The difference between the two given sets.", new_set)


# Anna -correct

# Lian jan you use really very complex logic and that's good you can build so logically strong steps,
#  but in case solution could be done in 2 lines, don't try make it more difficult.
# Because when you start automate test cases you will be need to write logic for bug application, 
# and if any simple case will take 15 lines of code, your big logic will be a huge. So try keep balance between complexity and simple solutions :)
# Generally everything is very good and strong background is visible
