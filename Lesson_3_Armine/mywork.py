print("Germany")
print('France')
print('Armenia is the best country in the world')
print("I'm learning python")
print('Welcome to the python classes', end='!\n')
print("Hi everyone, it is sunny day", end="?")
print("I'm a student, and now I'm learning python", end="!\n")
print("America, Japan, contemp\
orary")
print("I a'm studing python and I like it very much, because current\
ly i am searchig job")
print("I like my job", end="!!!\n")
print("Am I QA Engineer", end="?\n")
print("Yes", 6 * "\n")
print("Of course")
print(""" This is paragraph, and we can type long text, 
and there is no nedd to type it with separate prints""")
a = 9 
print(a)
a = "Armine" 
print(a)
a, b, c, d = 4, 6, 3.5, "Armine"
print(a)
print(d)
print(c)
*a, b = 2, 4, 5, 8
print(type(a))
print(type(b))

a = b = c = [2, 4, 6, 9]
print(b)
print(type(a))
b[3] = 7
print(b)

print(a is c)

print(b)

f = 300 
print(f)


def armineFunction(): 
    f = "I am learning python"
    return f 



age = 34 
print(id(age))
print(type(age))
print(age)

e = b = c = [2, 3, 5]
print(b)
b[2] = 100 
print(b)
b[0] = 2000 
print(e)


x = 4
y = 7
z = float(x) + float(y) 
print(z)

x = 22
y = 8
print(x//y)

a = 2
b = 3
print(a**b)
v = 4 
j = 2 
print(v % j)


l = 4
t = 6
print(l > t)
print(l < t)
print(l == t)
print(l != t)
print(l <= t)
print(l >= t)

test_data_8 = [1, 5, 8, 3]
res_8_1 = "True" if 3 in test_data_8 else "False"
res_8_2 = "True" if -1 in test_data_8 else "False"
print(res_8_1, res_8_2)



print(3 in [2, 4, 7, 5])

x = [2,3,5,5]
print(x)
print(id(x))
print(type(x))
x[1] = 10
print(x)

print(id(x))

y = (2, 3, 5, 7, 2)
print(set(y))

s = {3, 6, 8, 8}
print(s)
print(s)

#dic = {"position": "QA", "name": "Poghos", "age": 34}
#print(dic)
#print(dic["position"])

list = ["w", "c", "b", "f", "m", "a"]
list.sort(reverse=True)
print(list)

Armlist = []
Armlist.append('Ani')
Armlist.append('Anna')
Armlist.append('Karine')
Armlist.append('Armine')
print(Armlist)
Armlist.remove('Ani')
print(Armlist)
print(Armlist[0])
del Armlist[1]
print(Armlist)
list4 = [3, 5, 6, 9, 4, 3, 2]
if 10 in list4:
    print(False) 
list4.reverse
print(list4)

tup = (2, 3, 1, 6, 7)
print(tup)
y = len(tup)
print(y)




















