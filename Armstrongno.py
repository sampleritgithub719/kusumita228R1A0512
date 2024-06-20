from tkinter import *
from tkinter import messagebox

def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    total = 0
    for digit in num_str:
        total += int(digit) ** num_digits
    return total == num

def check_armstrong():
    try:
        num = int(entry.get())
        if is_armstrong(num):
            messagebox.showinfo("Armstrong Check", f"{num} is an Armstrong number")
        else:
            messagebox.showinfo("Armstrong Check", f"{num} is not an Armstrong number")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

window = Tk()
window.title("Armstrong Number Checker")

frame = Frame(window)
frame.pack(padx=20, pady=20)

label = Label(frame, text="Enter a number:")
label.grid(row=0, column=0)

entry = Entry(frame)
entry.grid(row=0, column=1)

button = Button(frame, text="Check", command=check_armstrong)
button.grid(row=1, column=0, columnspan=2)

window.mainloop()
