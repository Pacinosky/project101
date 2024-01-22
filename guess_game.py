from random import *
#this is a number guessing game
#the secret number is 9 
#user is asked to enter a number 3 times
#if user guess correctly game is ended
secret_number=9
guess_count=0
guess_limit=3
while guess_count<guess_limit :
    guess=int(input('enter a number: '))
    guess_count+=1
    
    #condition if user guess is equal to secret number
    if guess == secret_number:
        print('you guessed corrected')
        print('You won, game ended')
        break
    #if user guess wrongly ,let user guess again. 
    #user has only 3 tries
    else:
        print('you guessed wrongly, Try again!!!')
print(f'you guessed {guess_count} times')


