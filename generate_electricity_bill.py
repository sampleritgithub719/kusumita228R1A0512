from tkinter import *
from tkinter import messagebox


def calculate_bill():
    try:
        # Get user inputs
        name = name_entry.get()
        address = address_entry.get()
        units = float(units_entry.get())

        # Define tariff rates
        # You can adjust these rates based on your region or electricity provider
        # For example, cost_per_unit may vary based on slab rates
        fixed_charge = 100  # Fixed charge in Rs.
        cost_per_unit = 10  # Cost per unit in Rs.

        # Calculate total charges
        total_units_charge = units * cost_per_unit
        total_bill = fixed_charge + total_units_charge

        # Display the bill
        bill_text = f"Name: {name}\nAddress: {address}\n\nUnits Consumed: {units}\nUnit Charge: Rs. {total_units_charge:.2f}\nFixed Charge: Rs. {fixed_charge:.2f}\nTotal Bill: Rs. {total_bill:.2f}"
        messagebox.showinfo("Electricity Bill", bill_text)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid inputs for units consumed.")


# Create the main window
window = Tk()
window.title("Electricity Bill Generator")

# Create and place labels and entry widgets for user input
name_label = Label(window, text="Name:")
name_label.grid(row=0, column=0, sticky="e")
name_entry = Entry(window)
name_entry.grid(row=0, column=1)

address_label = Label(window, text="Address:")
address_label.grid(row=1, column=0, sticky="e")
address_entry = Entry(window)
address_entry.grid(row=1, column=1)

units_label = Label(window, text="Units Consumed:")
units_label.grid(row=2, column=0, sticky="e")
units_entry = Entry(window)
units_entry.grid(row=2, column=1)

# Create a button to calculate the bill
calculate_button = Button(window, text="Calculate Bill", command=calculate_bill)
calculate_button.grid(row=3, columnspan=2)

# Start the GUI application
window.mainloop()
