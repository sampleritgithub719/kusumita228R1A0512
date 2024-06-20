from tkinter import *
from tkinter import messagebox


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def find_gcd_of_divisors():
    try:
        num = int(entry.get())
        if num <= 0:
            messagebox.showerror("Error", "Please enter a positive integer.")
            return

        divisors = [i for i in range(1, num + 1) if num % i == 0]
        if len(divisors) < 2:
            messagebox.showinfo("GCD of Divisors", f"The number {num} has only one divisor, which is {divisors[0]}")
        else:
            gcd_result = divisors[0]
            for divisor in divisors[1:]:
                gcd_result = gcd(gcd_result, divisor)
            messagebox.showinfo("GCD of Divisors", f"The GCD of the divisors of {num} is {gcd_result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")


window = Tk()
window.title("GCD of Divisors Finder")

frame = Frame(window)
frame.pack(padx=20, pady=20)

label = Label(frame, text="Enter a number:")
label.grid(row=0, column=0)

entry = Entry(frame)
entry.grid(row=0, column=1)

button = Button(frame, text="Find GCD of Divisors", command=find_gcd_of_divisors)
button.grid(row=1, column=0, columnspan=2)

window.mainloop()
