from tkinter import *
from tkinter import messagebox


def generate_fibonacci():
    try:
        num_terms = int(entry.get())
        if num_terms <= 0:
            messagebox.showerror("Error", "Please enter a positive integer.")
            return

        fib_sequence = [0, 1]
        while len(fib_sequence) < num_terms:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

        messagebox.showinfo("Fibonacci Sequence",
                            f"The first {num_terms} Fibonacci numbers are:\n{', '.join(map(str, fib_sequence))}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")


window = Tk()
window.title("Fibonacci Sequence Generator")

frame = Frame(window)
frame.pack(padx=20, pady=20)

label = Label(frame, text="Enter the number of terms:")
label.grid(row=0, column=0)

entry = Entry(frame)
entry.grid(row=0, column=1)

button = Button(frame, text="Generate Fibonacci Sequence", command=generate_fibonacci)
button.grid(row=1, column=0, columnspan=2)

window.mainloop()
