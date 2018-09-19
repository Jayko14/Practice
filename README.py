import random

x = [1,1,1,1,1,2,2,2,2,3,5,5,4,5,3,7,7,8,6,5,7,8,9,7,5,4,2]
y = []
x = set(x)
x = list(x)
print(x)

for i in x:
    if i not in y:
        y.append(i)
print(y)


a= [1,1,2,3,5,7,13,21,34,55,89]
b = range(1,13)

c = [i for i in a if i in b]
print(c)

a= [1,1,2,3,5,7,13,21,34,55,89]
b = range(13)
c = []
for i in a:
    c.append(i)
for i in b:
    c.append(i)
c = set(c)
c = set(a)
print(c)
