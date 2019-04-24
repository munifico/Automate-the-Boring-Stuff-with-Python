import copy
a = [1,2,3,4]
b = copy.copy(a)
c = copy.deepcopy(a)

print(id(a), id(a[0]))
print(id(b), id(b[0]))
print()
c[0] = 5
print(id(a), id(a[0]))
print(id(c), id(c[0]))