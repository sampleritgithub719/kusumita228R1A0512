from tkinter import *
from tkinter import messagebox

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def check_prime():
    try:
        num = int(entry.get())
        if is_prime(num):
            messagebox.showinfo("Prime Check", f"{num} is a prime number")
        else:
            messagebox.showinfo("Prime Check", f"{num} is not a prime number")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

window = Tk()
window.title("Prime Number Checker")

frame = Frame(window)
frame.pack(padx=20, pady=20)

label = Label(frame, text="Enter a number:")
label.grid(row=0, column=0)

entry = Entry(frame)
entry.grid(row=0, column=1)

button = Button(frame, text="Check", command=check_prime)
button.grid(row=1, column=0, columnspan=2)

window.mainloop()
