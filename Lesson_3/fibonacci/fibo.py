n1 = 0
n2 = 0
fiboN = 10

for i in range(fiboN):
    if i == 0:
        n1 = 0
        print(n1)
    elif i == 1:
        n2 = 1
        print(n2)    
    else:
        res = n1 + n2
        n1 = n2
        n2 = res
        print(res)



# I didn't expect code in this stage )) but it's good you try to find out solution via code also
# In  your solution only last resalt is printed not the sequence
#  I changed the code a bit to get sequence as a printed reslut