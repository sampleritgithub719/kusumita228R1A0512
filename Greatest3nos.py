from tkinter import *
from tkinter import messagebox

def greatest():
    try:
        num1 = int(a.get())
        num2 = int(b.get())
        num3 = int(c.get())
        greatest_num = max(num1, num2, num3)
        res.delete(0, END)
        res.insert(0, str(greatest_num))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers")

window = Tk()
frame = Frame(window)
frame.place(x=600, y=100)

aLabel = Label(frame, text="NUM1=", font=('Arial', 10, 'bold'), bg='white', fg='black')
aLabel.grid(row=0, column=0)
a = Entry(frame, width=5)
a.grid(row=0, column=1)

bLabel = Label(frame, text="NUM2=", font=('Arial', 10, 'bold'), bg='white', fg='black')
bLabel.grid(row=1, column=0)
b = Entry(frame, width=5)
b.grid(row=1, column=1)
cLabel = Label(frame, text="NUM3=", font=('Arial', 10, 'bold'), bg='white', fg='black')
cLabel.grid(row=2, column=0)
c = Entry(frame, width=5)
c.grid(row=2, column=1)

resLabel = Label(frame, text="RESULT=", font=('Arial', 10, 'bold'), bg='white', fg='black')
resLabel.grid(row=3, column=0)
res = Entry(frame, width=5)
res.grid(row=3, column=1)

button = Button(frame, text="GREATEST", command=greatest)
button.grid(row=6, column=1)

window.mainloop()
