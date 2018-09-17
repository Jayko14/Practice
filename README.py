num = int(input('Please choose a number greater than 2 '))

x = [i for i in range(2,num) if num % i == 0]

if num > 1:
    if len(x) == 0:
        print('prime')
    else:
        print('not prime')
else:
    print('not prime')

