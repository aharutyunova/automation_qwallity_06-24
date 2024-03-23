
def fibonacci(N):
    list_fib = []
    a = 0
    list_fib.append(a)
    b = 1
    list_fib.append(b)
    n = 2
    c = a + b
    while c < N:
        list_fib.append(c)
        a = b
        b = c
        c = a + b
        n = n + 1
    return list_fib

    

    