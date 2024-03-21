'''
2.	Write a Python program that accepts a string and calculate the number of digits and letters.  
Sample Data: Python 3.2
Expected Output:
Letters 6
Digits 2
'''
print('input data string with letters and digits: ')
data = input()
letters = 0
digits = 0
for i in data:
    if i.isalpha():
        letters = letters + 1
    elif i.isdigit():
        digits = digits + 1
    else:
        pass
print(f'data: {data} - has {letters} letters and {digits} digits')

# Anna - correct