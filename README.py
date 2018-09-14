import random
x= random.sample(range(1,50),20)
y= random.sample(range(1,100),20)
z=[i for i in x if i in y]

print(x)
print(y)
print(z)
