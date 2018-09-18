x = int(input(' Please choose how many fibonacci numbers you want to display '))

fib = [1,1]
for i in range (2, x):
    fib.append(fib[i-1] + fib[i-2])

print (fib)
