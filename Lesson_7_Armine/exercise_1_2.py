#1. Write a Python function to find the maximum value of given list(write algorithm).

x = [2, 5, 6, 8, 9, 2, 4]
def max_value_function(x):
    sort_list = list(sorted(x))
    max_value = (sort_list[-1])
    print(max_value)
    
max_value_function([100, 45, 678, 1, 3, 5, 100, 4567, 85000, 7, 8, 4])



#2.	Write a Python function, which will get few numbers from keyboard, return to sum of them

# first solution
def Random_numbers(*args):
    print(sum(args))


Random_numbers(3, 5, 6, 8, 5)
    

#Second solution, but please correct me, why it works wrong((
def sum_calculation():
    random_numbers = input("please input only numbers:")
    if random_numbers:
        random_numbers.split()
        random_numbers_2 = int(random_numbers)
        print(sum(random_numbers_2))

        return random_numbers_2
    else: 
        print("No value to sum")

       
result = sum_calculation()
#third solution, again something is not correct)
def sum_calculation():
    random_numbers = input("Please input only numbers: ")
    if random_numbers:
        num_list = [int(num) for num in random_numbers.split()]
        sum_of = sum(num_list)
        print("The sum of the numbers is:", sum_of)  
        return sum_of
    else:
        print("No value to sum")

result = sum_calculation()

# Anna - the solutions are correct, one note, in case you request for random number, and all numbers could be integer,
# you could convert to float not integer





        


