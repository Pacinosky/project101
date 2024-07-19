from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog as fd

app= Tk()
app.title('OSAGEFO GAME')
app.geometry('500x550')


first_pic=ImageTk.PhotoImage(Image.open('warking.jpeg').resize((400,400)))
background_pic=ImageTk.PhotoImage(Image.open('warkin.jpeg').resize((150,150)))



def confirmation_page(message):
    response=BooleanVar()
    response.set(False)

    def action(answerRequest):
        response.set(answerRequest)
        confirmation_frame.destroy()
        

    confirmation_frame=Frame(app, highlightbackground='blue', highlightthickness=2)
    confirmation_frame.grid(pady=20)
    #confirmation_frame.pack_propagate(False)
    #confirmation_frame.configure(width=300 , height=300)
    confirmation_frame.place (x=50, y=100, width=300, height=300)

    
    confirmation_msg=Label(confirmation_frame, text=message, 
                               font=('Bold', 20))
    confirmation_msg.grid(pady=50)
    
    
    confirmation_Yesbutton= Button(confirmation_frame, text='Yes',
                        fg='blue',highlightbackground='blue',highlightthickness=0.5 ,
                        bd=0, command=lambda: action(True))
    confirmation_Yesbutton.place(x=200,y=250)

    confirmation_Cancelbutton= Button(confirmation_frame, text='No',
                        fg='red',highlightbackground='blue',highlightthickness=0.5 ,
                        bd=0, command=lambda: action(False))
    confirmation_Cancelbutton.place(x=50,y=250)

    
    app.wait_window(confirmation_frame)
    return response.get()

def message_page(message):
    message_frame=Frame(app, highlightbackground='blue', highlightthickness=2)
    message_frame.grid(pady=20)
    #confirmation_frame.pack_propagate(False)
    #confirmation_frame.configure(width=300 , height=300)
    message_frame.place (x=50, y=100, width=300, height=300)

    
    message_msg=Label(message_frame, text=message, 
                               font=('Bold', 20))
    message_msg.grid(pady=50)
    
    
    message_button= Button(message_frame, text='X',
                        fg='blue',highlightbackground='blue',highlightthickness=0.5,
                        bd=0, command=lambda: message_frame.destroy())
    message_button.place(x=200,y=10)



def intro_page():
    def forward_to_background():
        intro_frame.destroy()
        app.update()
        backgroundintro_page()

    intro_frame=Frame(app, highlightbackground='blue', highlightthickness=2)
    intro_frame.grid(pady=30)
    intro_frame.pack_propagate(False)
    intro_frame.configure(width=500 , height=500)
    intro_heading=Label(intro_frame, text='INTRODUCTION TO THE OSAGEFO GAME', font=('Bold', 15), bg='blue', fg='white')
    intro_heading.place(x=0,y=0, width=500)


    intro_picture=Label(intro_frame, image=first_pic, )
    intro_picture.place(x=10,y=25, width=400,height=450)

    intro_button= Button(intro_frame, text='>>>',
                        fg='blue',highlightbackground='blue',highlightthickness=0.5 ,
                        bd=0, command=forward_to_background)
    intro_button.place(x=200,y=450)

def backgroundintro_page():
    def forward_to_level1():
        answerRequest=confirmation_page(message='Would you like to play the game?')
        if answerRequest:    
            backgroundintro_frame.destroy()
            app.update()
            level1_page()
        else:
            backgroundintro_frame.destroy()
            app.update()

    backgroundintro_frame=Frame(app, highlightbackground='blue', highlightthickness=2)
    backgroundintro_frame.grid(pady=30)
    backgroundintro_frame.pack_propagate('False')
    backgroundintro_frame.configure(width=500 , height=500)
    backgroundintro_heading=Label(backgroundintro_frame, text='WELCOME TO THE OSAGEFO GAME', font=('Bold', 15), bg='blue', fg='white')
    backgroundintro_heading.place(x=0,y=0, width=500)

    backgroundintro_label=Label(backgroundintro_frame, 
    text=''' 
    Kunta is captured by slave traders and
    transported to America, 
    where he is sold into slavery. 
    Despite his efforts to maintain his African 
    identity and escape, 
    he is brutally punished and eventually
    accepts his new name, 
    Toby, and his life as a slave.
            ''', font=('Bold', 15),)
    backgroundintro_label.place(x=0,y=170, width=300)

    background_picture=Label(backgroundintro_frame, image=background_pic, )
    background_picture.place(x=10,y=25, )

    background_button= Button(backgroundintro_frame, text='PLAY',
                        fg='blue',highlightbackground='blue',highlightthickness=0.5 ,
                        bd=0, command=forward_to_level1)
    background_button.place(x=200,y=450)


def level1_page():
    def backward_to_background():
        Request=message_page(message='this gate is sealed \n Choose another option')
        if Request:
            level1_frame.destroy()
            app.update()
            backgroundintro_page()
            
    def forward_to_level2():
        answerRequest=confirmation_page(message='you enter the gate.\nWould you like to  \ncontinue to the next level?')
        if answerRequest:
            level1_frame.destroy()
            app.update()
            level2_page()

    level1_frame=Frame(app, highlightbackground='blue', highlightthickness=2)
    level1_frame.grid(pady=30)
    level1_frame.pack_propagate('False')
    level1_frame.configure(width=500 , height=500)
    level1_heading=Label(level1_frame, text='LEVEL 1- OSAGEFO GAME', font=('Bold', 15), bg='blue', fg='white')
    level1_heading.place(x=0,y=0, width=500)

    level1_label=Label(level1_frame, 
    text=''' 
    You are at the entrance of the grand 
    arena of the castle. 
    Kunta is sermoned by the slave traders. 
    The governor, 'Oyibo is accused of inciting the youth 
    against the white people who sell the ghanaians as trader.
    He is sent to the grand arena to  
    Kunta has to choose one of the four(4) gates
    to decide his fate. The gates are below:

            ''', font=('Bold', 15),)
    level1_label.place(x=0,y=170, width=500)

    level1_picture=Label(level1_frame, image=background_pic,)
    level1_picture.place(x=10,y=25, )

    level1_button= Button(level1_frame, text='Gate 2',
                        fg='blue',highlightbackground='blue',highlightthickness=0.5 ,bd=0)
    level1_button.place(x=120,y=430)

    level1_button= Button(level1_frame, text='Gate 3',
                        fg='blue',highlightbackground='blue',highlightthickness=0.5 ,bd=0)
    level1_button.place(x=300,y=430)

    level1_button= Button(level1_frame, text='Gate 1',
                        fg='blue',highlightbackground='blue',highlightthickness=0.5 ,
                        bd=0, command=forward_to_level2)
    level1_button.place(x=200,y=420)

    level1_button= Button(level1_frame, text='Gate 4',
                        fg='blue',highlightbackground='blue',highlightthickness=0.5 ,
                        bd=0, command=backward_to_background)
    level1_button.place(x=200,y=450)


    

def level2_page():
    def backward_to_background():
        level2_frame.destroy()
        app.update()
        level1_page()
    
    def forward_to_level3():
        level2_frame.destroy()
        app.update()
        level3_page()

    level2_frame=Frame(app, highlightbackground='blue', highlightthickness=2)
    level2_frame.grid(pady=30)
    level2_frame.pack_propagate('False')
    level2_frame.configure(width=500 , height=500)
    level2_heading=Label(level2_frame, text='LEVEL 2- OSAGEFO GAME', font=('Bold', 15), bg='blue', fg='white')
    level2_heading.place(x=0,y=0, width=500)

    level2_label=Label(level2_frame, 
    text=''' 
    You are also accused of treason and inciting people against 
    the governor.You are therefore sentenced to 'fight to death'
    Every year during the celebration the kings birthday,
    a 'FIGHT TO DEATH' contest is arranged between the best 
    fighter or warrior of the land and another contestant 
    who gets picked by the king. Honestly, the contender 
    does not survive against the warrior, "Racon".

    choose one of the weapons to fight:

            ''', font=('Bold', 15),)
    level2_label.place(x=0,y=170, width=500)

    level2_picture=Label(level2_frame, image=background_pic,)
    level2_picture.place(x=10,y=25, )

    level2_button= Button(level2_frame, text='SPEAR',
                        fg='blue',highlightbackground='blue',highlightthickness=0.5 ,
                        bd=0 ,command=backward_to_background)
    level2_button.place(x=140,y=430)

    level2_button= Button(level2_frame, text='SWORD',
                        fg='blue',highlightbackground='blue',highlightthickness=0.5,
                        bd=0, command=forward_to_level3)
    level2_button.place(x=300,y=430)

    
def level3_page():
    def backward_to_background():
        level3_frame.destroy()
        app.update()
        level2_page()
    
    def forward_to_level3():
        level3_frame.destroy()
        app.update()
        level1_page()




    level3_frame=Frame(app, highlightbackground='blue', highlightthickness=2)
    level3_frame.grid(pady=30)
    level3_frame.pack_propagate('False')
    level3_frame.configure(width=500 , height=500)
    level3_heading=Label(level3_frame, text='LEVEL 3- OSAGEFO GAME', font=('Bold', 15), bg='blue', fg='white')
    level3_heading.place(x=0,y=0, width=500)

    level3_label=Label(level3_frame, 
    text=''' 
    Kunta picked his sword and fought bravely
    with Racon. His determination to survive won him 
    the fight. Although it was not fought on a fair grounds,
    Kunta managed to win. The rules was that you kill your 
    opponent. if you chose not to, there will be consequences.
    will you kill or not kill racon?
            ''', font=('Bold', 15),)
    level3_label.place(x=0,y=170, width=500)

    level3_picture=Label(level3_frame, image=background_pic,)
    level3_picture.place(x=10,y=25, )

    level3_button= Button(level3_frame, text='KILL',
                        fg='blue',highlightbackground='blue',highlightthickness=0.5 ,
                        bd=0 ,command=backward_to_background)
    level3_button.place(x=140,y=430)

    level3_button= Button(level3_frame, text='NOT KILL',
                        fg='blue',highlightbackground='blue',highlightthickness=0.5 ,
                        bd=0, command=forward_to_level3)
    level3_button.place(x=300,y=430)

    



#confirmation_page(message='Would you like to continue\n to the next level?')


intro_page()
app.mainloop()