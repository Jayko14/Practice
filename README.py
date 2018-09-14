print('Welcome to the guessing game')
print('Type quit to leave at any time')
import random
x = random.randint (1,10)
guess=0
y=0
while y != x:
    y = input('Please pick a number between 0 and 10 ')
    if y == 'quit':
        print('Thanks for playing')
        break
    y = int(y)
    if y<= 0 or y>= 10:
        print('Invalid entry')
    elif y > x:
        print('Your guess is too high!')
        guess += 1
    elif y < x:
        print('Your guess is too low!')
        guess += 1
    else:
        print('Your guess is correct!')
        guess += 1
        print('Number of guesses:' + str(guess))
        break
       
    
