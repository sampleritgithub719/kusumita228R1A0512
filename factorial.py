from tkinter import *
from tkinter import messagebox

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def check_number():
    try:
        input_num = int(a.get())
        if input_num < 0:
            messagebox.showerror("Error", "Please enter a non-negative integer.")
        else:
            result_text = factorial(input_num)
            res.delete(0, END)
            res.insert(0, result_text)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

window = Tk()
frame = Frame(window)
frame.place(x=600, y=100)

aLabel = Label(frame, text="NUMBER=               ", font=('Arial', 10, 'bold'), bg='white', fg='black')
aLabel.grid(row=0, column=0)
a = Entry(frame, width=20)
a.grid(row=0, column=1)

resLabel = Label(frame, text="FACTORIAL OF A NUMBER=", font=('Arial', 10, 'bold'), bg='white', fg='black')
resLabel.grid(row=2, column=0)
res = Entry(frame, width=20)
res.grid(row=2, column=1)

button = Button(frame, text="FACTORIAL", command=check_number)
button.grid(row=4, column=1)

window.mainloop()
