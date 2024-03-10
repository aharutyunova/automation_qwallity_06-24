n1 = 1
ntemp = 1
res = 1
fiboN = 10

if fiboN <= 0:
    res = 0
elif fiboN == 1:
    res = 1
else:
    for i in range(2, fiboN):
        res += n1
        n1 = ntemp
        ntemp = res

print(res)
