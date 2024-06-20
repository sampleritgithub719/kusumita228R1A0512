from tkinter import *
from tkinter import messagebox

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "LEAP YEAR"
    else:
        return "NOT a LEAP YEAR"

def check_year():
    try:
        input_year = int(a.get())
        result_text = is_leap_year(input_year)
        res.delete(0, END)
        res.insert(0, result_text)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for the year.")

window = Tk()
frame = Frame(window)
frame.place(x=600, y=100)

aLabel = Label(frame, text="YEAR=", font=('Arial', 10, 'bold'), bg='white', fg='black')
aLabel.grid(row=0, column=0)
a = Entry(frame, width=20)
a.grid(row=0, column=1)

resLabel = Label(frame, text="RESULT=", font=('Arial', 10, 'bold'), bg='white', fg='black')
resLabel.grid(row=2, column=0)
res = Entry(frame, width=20)
res.grid(row=2, column=1)

button = Button(frame, text="CHECK", command=check_year)
button.grid(row=4, column=1)

window.mainloop()
