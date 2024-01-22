from random import *
#this is a number guessing game
#the secret number is 9 
#user is asked to enter a number 3 times
#if user guess correctly game is ended
number=9
count=0
limit=3
while count<limit :
    guess=int(input('enter a number: '))
    count+=1
    if guess == number:
        print('you guessed corrected')
        print('You won, game ended')
        break

    else:
        print('try again')
print(f'you guessed {count} times')


