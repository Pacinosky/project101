#import random and string modules
import random
import string

print('''
HOW TO GENERATE A RANDOM PASSWORD''')
print('................................')

#define a function to define generate password 
def generate_password(password_length):
    password='' #create an empty string for password

#use random module to generate random characters from string module
    alphabets=random.sample(string.ascii_letters,5)
    numbers=random.sample(string.digits,4)
    punctuation=random.sample(string.punctuation,3)
    #print(''.join(alphabet))
    #print(''.join(numbers))
    #print(''.join(punctuation))
    
    #use for loop to randomly generate pasword after 
    #receiving input of length of password
    character=alphabets+numbers+punctuation
    
    
    for letter in range(password_length):

        password=''.join(random.sample(character,password_length))

    return password

password_length=int(input('Enter length of password' '\n' '>>>'))
print(f'Generated {password_length} characters password is;')
print(generate_password(password_length))
