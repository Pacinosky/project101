#LEARNING HOW TO REVERSE A STRING
#METHOD 1

string='call me python.'
print('how to reverse this string:',string)
#split function splits a string into a list of strings
string=string.split()
print(string)
#reverse the string 
string=string[::-1]
print(string)
#convert list to string using the join function
string=' '.join(string)
#use replace function to replace an alphabet or symbol
#capitalize string using upper function
print('method 1')
print('reversed string:',string.replace('.','!').upper())
print('..............................')
#METHOD TWO
String='call me python.'
print('method 2')
print('reversed string:',' '.join(String.split()[::-1]).replace('.','!').upper())
print('\n\n')



print('reversing string using function \n METHOD 3')
#function to reverse a given string
def reverse_sentence(string):
    return ' '.join(string.split()[::-1])
sentence=input('write a sentence: ')
print(reverse_sentence(sentence))

print('METHOD 4 \n reversing each word in string')
#reverse each word in a every string
def reverse_sentence(string):
    
    string=string.split()
    result=[]
    for word in string:
        result.append(word[::-1])
    return ' '.join(result)
words=input('enter a sentence: ')
print(reverse_sentence(words))

    