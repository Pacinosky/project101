

def Madlip(verb_word,adjective_word,noun_word,noun1_word): 
    sentence=f'''
This is a story of a {noun} in the university.
The school cafeteria has really {adjective} food.
Just thinking about it makes my stomach {verb}.
            '''
    return sentence
verb=input('enter a verb: ')
adjective=input('enter an adjective: ')
noun=input('enter a noun: ')
noun1=input('enter a noun: ')
print(Madlip(verb,adjective,noun,noun1))

    
