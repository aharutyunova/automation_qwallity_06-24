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

# sum_of_the_list()
# remove_dublicates()
# remove_specific_elements()
