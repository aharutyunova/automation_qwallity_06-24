def fibonacci(n):
    if 0 <= n <= 1:
        return n
    n_minus1, n_minus2 = 1, 0

    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result
    return result


for i in range(11):
    print(i, fibonacci(i))
