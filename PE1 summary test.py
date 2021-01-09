# PE1 - Summary test

#6
dct = {'one':'two', 'three':'one', 'two': 'three'}
v = dct['three']

for k in range (len(dct)):
    v = dct[v]

print(v)
print()

#8
def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)

print(fun(0, 3))
print()

#13
list = [i for i in range(-1,-2)]
print(list)
print()

#14
dct = {}
dct['1'] = (1,2)
dct['2'] = (2,1)

for x in dct.keys():
    print(dct[x][1], end = "")
print()

#16
list = [[x for x in range (3)] for y in range (3)]

for r in range(3):
    for c in range(3):
        if list[r][c] % 2 != 0:
            print (list[r][c])
print()

#26
a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)
print()

#29
lst = [1, 2]

for v in range(2):
    lst.insert(-1, lst[v])
print(lst)
print()

#24
dd = {"1": "0", "0": "1"}

for x in dd.vals():
    print(x, end = "")
    """ the code is erroneous (the dict object has no vals() method)"""
    





