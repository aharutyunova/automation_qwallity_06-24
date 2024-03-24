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


# Anna comment - I didn't expect you write code )) you just need to describe in diagram )
    # But anyway code logic is correct. Maybe it is a bit longer, but anyway
    # taking into account that we didn't discuss it everything is very good :)


mydict = {
    "a": "1",
    "b": "2",
    "c": "3"
}
mydict.update({"d": "4"})
print(mydict)

mydict.update({'key3': 'geeks'})
print(mydict)