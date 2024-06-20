from tkinter import *
from tkinter import messagebox

def age():
    num = int(a.get())
    if num >= 18:
        messagebox.showinfo("ELIGIBLE OR NOT", "Eligible to vote")
    else:
        messagebox.showinfo("ELIGIBLE OR NOT", "Not Eligible to vote")

window = Tk()
frame = Frame(window)
frame.place(x=600, y=100)

aLabel = Label(frame, text="AGE=", font=('Arial', 10, 'bold'), bg='white', fg='black')
aLabel.grid(row=0, column=0)
a = Entry(frame, width=25)
a.grid(row=0, column=1)

button = Button(frame, text="CHECK", command=age)
button.grid(row=1, column=1)

window.mainloop()
