'''This is Hamest's fibonachi program
Program works withe the following logic
You enther the valid number N of list Elements, and the program return you the fibonachi list with N elements.'''


def fibonachi(n):
    if n <= 0:
        print("Invalid value")
    else:
        a = [0, 1]
        i = 2
        while n >= 3:
            a.insert(i, a[i-1] + a[i-2])
            n = n-1
            i = i+1
        print(a)


print("Please enter the number you want to see the fibonachi elements list")
fibonachi(int(input()))

# Anna - I didn't expect you wrute the code :) Just describe the logic via 
# diagram all words. But anyway code is totally correct!!!
