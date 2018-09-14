print("Let's play Rock, Paper, Scissors")

import random
y = 'yes'
P1_score = 0
Comp_score = 0
while y =='yes':
    x = ['rock','paper','scissors']
    P1 = input('Please choose from rock, paper or scissors ')
    P2 = random.choice(x)
    print('Computer chose ' + P2)
    if P1 == P2:
         print ("It's a tie")
         continue
    elif P1 == 'rock' and P2 == 'scissors'or P1 == 'paper' and P2 == 'rock' or P1 == 'scissors' and P2 == 'paper':
         print ("You win!")
         P1_score += 1
    elif P1 == 'paper' and P2 == 'scissors' or P1 == 'scissors' and P2 == 'rock' or P1 == 'rock' and P2 == 'paper':
         print ("You lose!")
         Comp_score += 1
    else:
        print ("Invalid entry please try again")
    print("Player 1 Score:" + str(P1_score))
    print("Computer Score:" + str(Comp_score))
    if P1_score == 5:
        print ('You beat Computer')
        y = input('Would you like to play again? yes/no ')
        if y == 'yes':
            P1_score=0
            Comp_score=0
            continue
        else:
            break
    if Comp_score == 5:
        print ('Computer beat you')
        y = input('Would you like to play again? yes/no ')
        if y == 'yes':
            P1_score=0
            Comp_score=0            
            continue
        else:
            break
print('Thanks for playing')

    
