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

# Anna - the logic is correct, 
# only for exit point will be better to give some other conditions. In case I don't input alpha the cycle willn't end
# You should give any limit of entered numbers, or somehow hint that for stop loop any aptha symbol should be entered

print('The sum of inputed numbers is: ', sum_input_numbers())