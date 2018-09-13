import random
while True:
    x = ['rock','paper','scissors']
    P1 = input('Please choose from rock, paper or scissors ')
    P2 = random.choice(x)
    print('Computer chose ' + P2)
    if P1 == P2:
        print ("It's a tie")
    elif P1 == 'rock' and P2 == 'scissors':
        print ("You win!")
    elif P1 == 'paper' and P2 == 'rock':
        print ("You win!")
    elif P1 == 'scissors' and P2 == 'paper':
        print ("You win!")
    else:
        print ("You lose!")
        break        

