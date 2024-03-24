
def fibinacci():
a = 0
b = 1
series_length = [0, 1, 2, 3, 4, 5, 6, 7]

print(a, b, end=' ')
for i in series_length:
    c = a + b
    a = b
    b = c
    print(c, end=' ')

print("\n")
