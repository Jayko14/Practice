#random list duplication
a = [1,1,2,3,5,8,13,21,34,55,89]
b = range(1,14)

c = []

for i in a:
    if i in b:
        if i not in c:
            c.append(i)

print (c)
