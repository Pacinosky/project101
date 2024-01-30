from tkinter import *
from datetime import date
from tkinter import messagebox

#In this code, the user enters their date of birth  in separate entry fields for day, month, and year. 
#When the “Calculate Age” button is clicked, the calculate function is called. 
#This function calculates the age based on the current date and the entered birth date, and then displays first, the date of birth below the calculate button.
#Then also displays the  age result in message box.


# write a function to calculate your age in current year.
def calculate():
    try:
        today = date.today()
        birth_year =int(year_entry.get())
        birth_month=int(month_entry.get())
        birth_day=int(day_entry.get())
        if birth_day<=31 and birth_month<=12 and today.year >birth_year:
        #birth_date = date(birth_year, birth_month, birth_day)
            age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
            result_label.config(text=f"Your birth date is {birth_day}/{birth_month}/{birth_year} \n This year {today.year},You're {age} years old")
            day_entry.delete(0,END)
            month_entry.delete(0,END)
            year_entry.delete(0,END)
            messagebox.showinfo(title='Age calculator', message=f'YOUR AGE IN CURRENT YEAR {today.year} is {age}')
    except ValueError:
        messagebox.showinfo(title='Error', message='INVALID INPUT')
# Create and configure the main window
window=Tk()
window.title("Age Calculator")
window.geometry()
window.resizable(0,0)
window.configure(bg='#333333')
# Create birth day label and entry fields with grids
day_label = Label(window,text="Day",bg='#333333',fg='#FFFFFF')
day_label.grid(row=0, column=0, sticky='news')
day_entry = Entry(window, width=5)
day_entry.grid(row=1, column=0, sticky='news', padx=5)

# Create birth month label and entry fields with grids
month_label = Label(window, text="Month",bg='#333333', fg='#FFFFFF')
month_label.grid(row=0, column=1)
month_entry = Entry(window, width=5)
month_entry.grid(row=1, column=1, sticky='news', padx=5)

# Create birth year label and entry fields with grids
year_label = Label(window, text="Year",bg='#333333', fg='#FFFFFF')
year_label.grid(row=0, column=2)
year_entry = Entry(window, width=7)
year_entry.grid(row=1, column=2, sticky='news',padx=5)

# Create calculate button
calculate_button = Button(window, text="Calculate Age",fg='#333333', command=calculate)
calculate_button.grid(row=2, column=0, columnspan=3, pady=20)

# Create result label with grid
result_label =Label(window, text="")
result_label.grid(row=3, column=0, columnspan=6)

# Running the main loop
window.mainloop()

#Note: The assumption is that  age calculator is of  date format  DD/MM/YYYY. You can change it to your preferred date format.
