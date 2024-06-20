from tkinter import *
from tkinter import messagebox

def simpleinterest():
    try:
        principal = float(p.get())
        time = float(t.get())
        rate = float(r.get())
        si = (principal * time * rate) / 100
        res.delete(0, END)
        res.insert(0, str(si))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

window = Tk()
frame = Frame(window)
frame.place(x=600, y=100)

pLabel = Label(frame, text="PRINCIPAL=", font=('Arial', 10, 'bold'), bg='white', fg='black')
pLabel.grid(row=0, column=0)
p = Entry(frame, width=8)
p.grid(row=0, column=1)

tLabel = Label(frame, text="RATE=", font=('Arial', 10, 'bold'), bg='white', fg='black')
tLabel.grid(row=1, column=0)
t = Entry(frame, width=8)
t.grid(row=1, column=1)

rLabel = Label(frame, text="TIME=", font=('Arial', 10, 'bold'), bg='white', fg='black')
rLabel.grid(row=2, column=0)
r = Entry(frame, width=8)
r.grid(row=2, column=1)

resLabel = Label(frame, text="RESULT=", font=('Arial', 10, 'bold'), bg='white', fg='black')
resLabel.grid(row=3, column=0)
res = Entry(frame, width=5)
res.grid(row=3, column=1)

button = Button(frame, text="simpleinterest", command=simpleinterest)
button.grid(row=6, column=1)
window.mainloop()
