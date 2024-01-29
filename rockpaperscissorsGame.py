import random

#this is a game between a player and computer.
#the game is called rock,paper and scissors.
#first make a player choice and computer list
user1 = input(" What's your name? ")

player_choice=['rock','paper', 'scissors']
computer_choice=['Rock','Paper','Scissors']
#set up variables for player and computer scores and possible draw games
player1_score=0
computer_score=0
draws=0
#define an infinite loop and accept input from player and computer
#by assigning player choice to player input and printing out the choice
#by assigning computer list to computer and printing out the choice
#dont forget to convert to lower case.
while True:
    player1 = input(f'%s, Make a choice {player_choice}\n choose one: '%user1).lower()
    computer = random.choice(computer_choice).lower()
    #Game rules rock>paper ,paper>scissors and scissors >rock
#Use if statement to setup and check conditions are true and declare the winner.
    
    if player1=='rock' and computer=='paper'or player1=='paper' and computer=='scissors' or player1=='scissors' and computer=='rock':
        print(f'{user1} won')
        player1_score+=1
        #print(f'player1 won the game {player1_score} times')
        if input('Do you want to play another game, yes or no?\n').lower() == 'yes':
            continue
        else:
            print('game over.')
            break

    elif computer=='rock' and player1=='paper'or computer=='paper' and player1=='scissors' or computer=='scissors' and player1=='rock':
        print('\n computer won')
        computer_score += 1
        #print(f'computer won the game, {computer_score} times')
        if input('Do you want to play another game, yes or no?\n').lower() == 'yes':
            continue
        else:
            print('Game over.')
            break
    #CONDITION IF BOTH COMPUTER AND USER1 MAKE THE SAME CHOICE
    else:
        print('ITS A TIE, PLAY AGAIN')
        draws+=1
        #print(f'this is a draw, game: {draws}')
        print('\n PLAY AGAIN')
    print(f'{user1} chose {player1} and computer chose {computer}')
    print(f'game won by computer = {computer_score }  \n game won by {user1} = {player1_score}  \nnumber of drawn game = {draws}')



