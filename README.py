#random list duplication
import random
a = (range(1,random.randint(1,100)))
b = (range(1,random.randint(1,1000)))

c = []

for i in b:
    if i in a:
        if i not in c:
            c.append(i)

print(c)
