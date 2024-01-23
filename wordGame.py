import random 
print('''
This is a word game where the computer 
randomly pick a word for you to guess.
you are to carefully select the right 
alphabets in their respectively positions.
you have 10 tries.
''')

words=['letter','promise','python','java','javascript','php']
word=random.choice(words)   #randomly select a word from list of words
guess=''  #create a variable for an empty string 
number_of_attempts=10 #total number of attempts is 10
while number_of_attempts>0 :
    #set incorrect variable to zero for any wrong guess
    incorrect_guess=0
    #condition for letter in word if letter also in guess
    for alphabet in word:
        if alphabet in guess:
            print(alphabet)
        else:
            print('_')
            incorrect_guess+=1
            
    #set condition if you guess all correctly
    if incorrect_guess==0:
        print('\n you won')
        break    #end the game if you win
    guesses=input('\t enter a letter: ') 
    guess+=guesses
    
    if guesses not in word:
        number_of_attempts-=1
        print(f'you have {number_of_attempts} tries')
    if number_of_attempts==0:
        print('\n you lost')
print('game is over')
               