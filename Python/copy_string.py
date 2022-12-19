import copy

a = "Hello world!"
b = a
c = str(a)
d = a[:]
e = a + ""
f = copy.copy(a)
g = copy.deepcopy(a)
h = a[::-1][::-1]


print(a, id(a))
print(b, id(b))
print(c, id(c))
print(d, id(d))
print(e, id(e))
print(f, id(f))
print(g, id(g))
print(h, id(h))