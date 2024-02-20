import random
from tkinter import *
from tkinter import ttk


#this is a two dice roll which when you click the roll dice button,
#roll two dice randomly and display results

#define function for rolling a dice and display result  using if condtions
def roll_dice():
    #value = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']
    dice1= ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    dice2 = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    
    result=random.choice(dice1)
    result2=random.choice(dice2)
    label.configure(text=result+result2)
    label.pack()
    if (result=='\u2680') and result2=='\u2680' or '\u2681'or '\u2682'or '\u2683' or '\u2684'or '\u2685':
        label3=Label(root,text=f'You rolled  {result} and {result2} \n Roll the dice again? ',font=('Consolas',30))
        label3.place(x=150,y=400)
    elif(result=='\u2681' and result2=='\u2680' or '\u2681'or '\u2682'or '\u2683' or '\u2684'or '\u2685'):
        label3=Label(root,text=f'You rolled  {result} and {result2} \n Roll the dice again? ',font=('Consolas',30))
        label3.place(x=150,y=450)
    elif(result=='\u2682' and result2=='\u2680' or '\u2681'or '\u2682'or '\u2683' or '\u2684'or '\u2685'):
        label3=Label(root,text=f'You rolled  {result} and {result2} /n Roll the dice again? ',font=('Consolas',30))
        label3.place(x=150,y=450)
    elif(result=='\u2683' and result2=='\u2680' or '\u2681'or '\u2682'or '\u2683' or '\u2684'or '\u2685'):
        label3=Label(root,text=f'You rolled  {result} and {result2} \n Roll the dice again? ',font=('Consolas',30))
        label3.place(x=150,y=450)
    elif(result=='\u2684' and result2=='\u2680' or '\u2681'or '\u2682'or '\u2683' or '\u2684'or '\u2685'):
        label3=Label(root,text=f'You rolled  {result} and {result2} \n Roll the dice again? ',font=('Consolas',30))
        label3.place(x=150,y=450)
    elif(result=='\u2685' and result2=='\u2680' or '\u2681'or '\u2682'or '\u2683' or '\u2684'or '\u2685'):
        label3=Label(root,text=f'You rolled  {result} and {result2} \n Roll the dice again? ',font=('Consolas',30))
        label3.place(x=150,y=450)

#create a window 
root =Tk()
root.geometry('550x500')
root.title('PASINO Roll Dice')

#create a label to print result
label =Label(root, text='', font=('Consolas', 260))

#Label to welcome you to the game
label2 =Label(root, text='Welcome to PASINO Online Python Dice roll. Click to roll the dice!', font=('Consolas',15))
label2.place(x=50,y=350)

#create a button called roll dice 
button =Button(root, text='roll dice', foreground='red', command=roll_dice)
button.pack()
root.mainloop()


