# 1 Write a Python program to sum all the items in a list.
# mylist = [1, 2, 3, 3, 4, 5]


def sum_of_the_list():
    n = int(input("Please enter the valid integer number : the count of new creating list's elemets\n"))
    print(f"Please Enter {n} integer elements")
    my_list = []
    i = 0
    while (n > 0):
        my_inp = int(input())
        my_list.insert(i, my_inp)
        n = n-1
        i = i+1
    print("This is your list", my_list)
    print("The sum of yor list elements is ", sum(my_list))


# 2 Write a Python program to remove duplicates from a list.
# mylist = [1, 2, 3, 3, 4, 5]
    

def remove_dublicates():
    n = int(input("Please enter the valid integer number : the count of new creating list's elemets\n"))
    print(f"Please Enter {n} integer elements")
    my_list = []
    i = 0
    while (n > 0):
        my_inp = int(input())
        my_list.insert(i, my_inp)
        n = n-1
        i = i+1
    print("This is your list", my_list)
    print("None dublicated list is ", list(set(my_list)))


# 3 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.
# mylist = [1, 2, 3, 3, 4, 5]

def remove_specific_elements():
    n = int(input("Please enter the valid integer number : the count of new creating list's elemets\n"))
    print(f"Please Enter {n} integer elements")
    my_list = []
    i = 0
    while (n > 0):
        my_inp = int(input())
        my_list.insert(i, my_inp)
        n = n-1
        i = i+1
    print("This is your list", my_list)
    m = int(input("Please enter the count of elements you want to remove from the list\n"))
    if (m > len(my_list)):
        print(f"The list you create do not have {m} elements, which you want to remove")
    else:
        print(f"Please Enter {m} intex you want to remove\n PS indexing starts with 0")
        my_indexes = []
        k = 0
        while (m > 0):
            my_indexes_el = int(input())
            if my_indexes_el < 0 or my_indexes_el >= len(my_list):
                print(f"The list you create do not have element with {my_indexes_el} index")
            else:
                my_indexes.insert(k, my_indexes_el)
                m = m-1
                k = k+1
    print("This is the indexes list you want to remove from your list", my_indexes)
    my_indexes = sorted(my_indexes)
    first_shift = 0
    for c in my_indexes:
        if first_shift == 0:
            my_list.remove(my_list[c])
            first_shift = first_shift + 1
        else:
            my_list.remove(my_list[c-first_shift])
            first_shift = first_shift + 1
    print("This is the new list\n", my_list)


# 4 Write a Python program to get the difference between the two lists.
# mylist = [1, 2, 3, 3, 4, 5]
# mylist2 = [1, 2, 7]

def diff_lists():
    n1 = int(input("Please enter the valid integer number : the count of new creating  fist list's elemets\n"))
    print(f"Please Enter {n1} integer elements")
    my_list1 = []
    i1 = 0
    while (n1 > 0):
        my_inp1 = int(input())
        my_list1.insert(i1, my_inp1)
        n1 = n1-1
        i1 = i1+1
    print("This is your fist list", my_list1)
    n2 = int(input("Please enter the valid integer number : the count of new creating second list's elemets\n"))
    print(f"Please Enter {n2} integer elements")
    my_list2 = []
    i2 = 0
    while (n2 > 0):
        my_inp2 = int(input())
        my_list2.insert(i2, my_inp2)
        n2 = n2-1
        i2 = i2+1
    print("This is your second list", my_list2)
    my_set1 = set(my_list1)
    my_set2 = set(my_list2)
    print("This is the diff of this 2 lists\n PS The dublicates in own list are removed\n", list(my_set1.difference(my_set2)) + list(my_set2.difference(my_set1)))


# 5 Write a Python program to convert a tuple to a dictionary.-
# mytuple = ('green', 'red', 'black', 'blue')
    
def tuple_to_dict():
    n = int(input("Please enter the valid even integer number : the count of new creating tuple's elemets\n"))
    if n % 2 == 1:   
        print("Not even number\n")
    else:
        print(f"Please Enter {n} string elements")
        my_tuple = []
        i = 0
        while (n > 0):
            my_inp = input()
            my_tuple.insert(i, my_inp)
            n = n-1
            i = i+1
    real_tuple = tuple(my_tuple)
    print("This is your tuple", real_tuple)
    real_dict = {}
    h = 0
    my_iter = len(real_tuple)
    while my_iter > 0:
        real_dict[real_tuple[h]] = real_tuple[h+1]
        h = h + 2
        my_iter = my_iter - 2
    print("Convertes dectionary is\n", real_dict)


# 6 Write a Python program to add a key to a dictionary.
# mydict = {
#  "a": "1",
#  "b": "2",
#  "c": "3"
# }

def add_key_to_dict():
    my_start_dict = {"a": "1", "b": "2", "c": "3"}
    print("This is your starting dictionary\n", my_start_dict)
    starting = True
    while starting:
        my_key = input("Please add the new key to start dictonary\n")
        my_val = input("Please add the value of the following key\n")
        my_start_dict[my_key] = my_val
        print("To repeat adding new keys please input yes, in other cases program will ext")
        if input() == "yes":
            starting = True
        else:
            starting = False
    print("Your new dictionary is\n", my_start_dict)

# 7 Write a Python program to remove a key from a dictionary.
# mydict = { 
# "a": "1",
# "b": "2",
# "c": "3"
#}
    

def removing_key():
    my_start_dict = {"a": "1", "b": "2", "c": "3"}
    print("This is your starting dictionary\n", my_start_dict)
    starting = True
    while starting:
        my_key = input("Please add the key you want to remove\n")
        if not (my_key in my_start_dict.keys()):
            print(f"In your dictionary there is no {my_key} key")
        else:
            del my_start_dict[my_key]
        print("To repeat removing keys please input yes, in other cases program will ext")
        if input() == "yes":
            starting = True
        else:
            starting = False
        if len(my_start_dict) == 0:
            print("Your dictionary now is empty, you remove all items of the starting dicionary")
            break
    print("Your new dictionary is\n", my_start_dict)

# 8 Write a Python program to get the maximum and minimum value in a dictionary.
# mydict = { 
# "a": "1",
# "b": "2",
# "c": "3"
#}


def max_min_val_of_dict():
    my_start_dict = {"a": "100", "b": "200", "c": "-300", "d": "50"}
    print("This is your starting dictionary\n", my_start_dict)
    max_val = int(list(my_start_dict.values())[0])
    min_val = int(list(my_start_dict.values())[0])
    for k in my_start_dict.values():
        if int(k) > max_val:
            max_val = int(k)
        elif int(k) < min_val:
            min_val = int(k)
    print(f" Max vlue is {max_val}\n", f"Min value is {min_val}")

# 9 Write a Python program to create a union of sets.
# set1 = {1, 2, 3, 4, 5}
# set2 = {1, "b", "c", "d", "e"}


def union_of_set():
    my_set1 = {1, 2, 3, 4, 5}
    my_set2 = {1, "b", 3, "c", "d", "e"}
    print("This is your starting sets\n", my_set1, "\n", my_set2)
    print("This is the union of given sets\n", my_set1 | my_set2)


# 10 Write a Python program to create a difference of two sets and print output. 
# set1 = {1, 2, 3, 4, 5}
# set2 = {1, "b", "c", "d", "e"}


def diff_of_set():
    my_set1 = {1, 2, 3, 4, 5}
    my_set2 = {1, "b", "c", "d", "e"}
    print("This is your starting sets\n", my_set1, "\n", my_set2)
    print("This is the difference of given sets\n", my_set1 - my_set2, "from first set\n", my_set2 - my_set1, "from second set")


# sum_of_the_list()
# remove_dublicates()
# remove_specific_elements()
# diff_lists()
# tuple_to_dict()
# add_key_to_dict()
# removing_key()
# max_min_val_of_dict()
# union_of_set()
# diff_of_set()