from tkinter import *
import mysql.connector
from tkinter import messagebox

def saveData():
    global usernameEntry, rollEntry
    print("Save Data function called")  # Debug print
    try:
        print("Username:", usernameEntry.get())  # Debug print
        print("Roll No:", rollEntry.get())  # Debug print
        conn = mysql.connector.connect(host="localhost", user="root", password="kusumita@777", database="customerdata")
        if usernameEntry.get() == '' or rollEntry.get() == '':
            messagebox.showerror('Error', "Name and Roll No are mandatory")
        else:
            mycur = conn.cursor()
            tests_selected = [str(int(test_var.get())) for test_var in test_vars]
            unit_tests_selected = [str(int(unit_test_var.get())) for unit_test_var in unit_test_vars]

            sql = 'INSERT INTO info(name, rollno, unit1_tests) VALUES (%s, %s, %s)'
            mycur.execute(sql, (usernameEntry.get(), rollEntry.get(), ', '.join(tests_selected)))
            conn.commit()

            messagebox.showinfo('Success', 'Data saved successfully')
            record_label.config(text="Record Submitted: " + ("Yes" if record_yes_var.get() else "No"))
    except mysql.connector.Error as err:
        messagebox.showerror('Error', f"Error: {err}")
    finally:
        if conn.is_connected():
            conn.close()

window = Tk()
window.title("Record Submission")
frame = Frame(window)
frame.pack(pady=20)

# Labels and Entries
labels_entries = [("NAME", 0), ("ROLL NO", 1)]
for label_text, row in labels_entries:
    label = Label(frame, text=label_text, font=('Arial', 15, 'bold'))
    label.grid(row=row, column=0, padx=10, pady=5)
    entry = Entry(frame, width=30)
    entry.grid(row=row, column=1, padx=10, pady=5)
    if label_text == "NAME":
        usernameEntry = entry
    else:
        rollEntry = entry

# Labels for test checkboxes
test_label = Label(frame, text="Test", font=('Arial', 15, 'bold'))
test_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

# Checkboxes
test_vars = []
tests = ['unit1', 'unit2', 'unit3', 'unit4', 'unit5']
for i, test in enumerate(tests):
    var = BooleanVar()
    test_vars.append(var)
    test_checkbox = Checkbutton(frame, text=test, variable=var, font=('Arial', 12, 'bold'))
    test_checkbox.grid(row=i + 3, column=0, padx=10, pady=5, sticky=W)

# Labels for unit checkboxes
unit_label = Label(frame, text="Unit", font=('Arial', 15, 'bold'))
unit_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

# Checkboxes for unit tests
unit_test_vars = []
unit_tests = ['unit-1', 'unit-2', 'unit-3', 'unit-4', 'unit-5']
for i, unit_test in enumerate(unit_tests):
    var = BooleanVar()
    unit_test_vars.append(var)
    unit_test_checkbox = Checkbutton(frame, text=unit_test, variable=var, font=('Arial', 12, 'bold'))
    unit_test_checkbox.grid(row=i + 3, column=2, padx=10, pady=5, sticky=W)

# Labels for "Yes" or "No" checkboxes
record_label = Label(frame, text="Record Submitted", font=('Arial', 15, 'bold'))
record_label.grid(row=len(tests) + 4, column=0, padx=10, pady=5, sticky=W)

# Checkboxes for "Yes" or "No" for record submitted
record_yes_var = BooleanVar()
record_no_var = BooleanVar()

record_yes_checkbox = Checkbutton(frame, text="Yes", variable=record_yes_var, font=('Arial', 12, 'bold'))
record_yes_checkbox.grid(row=len(tests) + 4, column=1, padx=10, pady=5, sticky=W)

record_no_checkbox = Checkbutton(frame, text="No", variable=record_no_var, font=('Arial', 12, 'bold'))
record_no_checkbox.grid(row=len(tests) + 4, column=2, padx=10, pady=5, sticky=W)

# Submit Button
button = Button(window, text="Submit", command=saveData, font=('Arial', 12, 'bold'))
button.pack(pady=10)

window.mainloop()
