from tkinter import *
from tkinter import messagebox

def distance():
    try:
        X1 = int(x1.get())
        Y1 = int(y1.get())
        X2 = int(x2.get())
        Y2 = int(y2.get())
        dis=((X2-X1)**2+(Y2-Y1)**2)**0.5
        res.delete(0, END)
        res.insert(0, str(dis))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

window = Tk()
frame = Frame(window)
frame.place(x=600, y=100)
x1Label = Label(frame, text="X1=", font=('Arial', 10, 'bold'), bg='white', fg='black')
x1Label.grid(row=0, column=0)
x1 = Entry(frame, width=8)
x1.grid(row=0, column=1)

y1Label = Label(frame, text="X2=", font=('Arial', 10, 'bold'), bg='white', fg='black')
y1Label.grid(row=1, column=0)
y1 = Entry(frame, width=8)
y1.grid(row=1, column=1)

x2Label = Label(frame, text="Y1=", font=('Arial', 10, 'bold'), bg='white', fg='black')
x2Label.grid(row=2, column=0)
x2 = Entry(frame, width=8)
x2.grid(row=2, column=1)
y2Label = Label(frame, text="Y2=", font=('Arial', 10, 'bold'), bg='white', fg='black')
y2Label.grid(row=3, column=0)
y2 = Entry(frame, width=8)
y2.grid(row=3, column=1)

resLabel = Label(frame, text="DISTANCE=", font=('Arial', 10, 'bold'), bg='white', fg='black')
resLabel.grid(row=4, column=0)
res = Entry(frame, width=5)
res.grid(row=4, column=1)

button = Button(frame, text="RESULT", command=distance)
button.grid(row=6, column=1)
window.mainloop()
