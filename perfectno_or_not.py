from tkinter import *
from tkinter import messagebox


def is_perfect(num):
    divisor_sum = sum([i for i in range(1, num) if num % i == 0])
    return divisor_sum == num


def check_perfect():
    try:
        num = int(entry.get())
        if num <= 0:
            messagebox.showerror("Error", "Please enter a positive integer.")
            return

        if is_perfect(num):
            messagebox.showinfo("Perfect Number Check", f"{num} is a perfect number")
        else:
            messagebox.showinfo("Perfect Number Check", f"{num} is not a perfect number")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")


window = Tk()
window.title("Perfect Number Checker")

frame = Frame(window)
frame.pack(padx=20, pady=20)

label = Label(frame, text="Enter a number:")
label.grid(row=0, column=0)

entry = Entry(frame)
entry.grid(row=0, column=1)

button = Button(frame, text="Check", command=check_perfect)
button.grid(row=1, column=0, columnspan=2)

window.mainloop()
