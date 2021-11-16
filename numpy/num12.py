a = [1, 2, 3]
a[2] = 4
print(a)

del a[1]
print(a)
del a[1:]
print(a)

b = [1, 2, 3, 4, 5]
b.append(6)
print(b)
b.append([7, 8, 9])
print(b)

c = [1, 2, 3, 4, 5]
c.reverse()
print(c)
print(c.index(3))
