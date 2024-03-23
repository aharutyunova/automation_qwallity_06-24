#2.	Write a Python function, which will get few numbers from keyboard, return to sum of them

def sum_input_numbers():
    
    list_numbers = []
    while True:
        num = input('input number: ')
        if  num.isalpha():
            break
        else:
            list_numbers.append(float(num))

    return sum(list_numbers)


print('The sum of inputed numbers is: ', sum_input_numbers())