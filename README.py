# Practice
a = range(1,e.randint(1,100))
b = range(1,f.randint(1,100))

c = []

for i in b:
    if i in a:
        if i not in c:
            c.append(i)

print(c)
