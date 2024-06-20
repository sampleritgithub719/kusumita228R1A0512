import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

root = tk.Tk()
root.title("Management")

connection = sqlite3.connect('management.db')

TABLE_NAME = "management_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"
STUDENT_TESTS = "student_tests"
STUDENT_UNITS = "student_units"

connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " +
                   STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER, " +
                   STUDENT_TESTS + " TEXT, " + STUDENT_UNITS + " TEXT);")

appLabel = tk.Label(root, text="Student Management System", fg="#06a099", width=35)
appLabel.config(font=("Sylfaen", 30))
appLabel.grid(row=0, columnspan=2, padx=(10,10), pady=(30, 0))

nameLabel = tk.Label(root, text="Enter your name", width=40, anchor='w',
                     font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0),
                                                pady=(30, 0))
collegeLabel = tk.Label(root, text="Enter your college", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))
phoneLabel = tk.Label(root, text="Enter your phone number", width=40, anchor='w',
                      font=("Sylfaen", 12)).grid(row=3, column=0, padx=(10,0))
addressLabel = tk.Label(root, text="Enter your address", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=4, column=0, padx=(10,0))
testLabel = tk.Label(root, text="Select your tests", width=40, anchor='w',
                     font=("Sylfaen", 12)).grid(row=5, column=0, padx=(10,0))
unitLabel = tk.Label(root, text="Select your units", width=40, anchor='w',
                     font=("Sylfaen", 12)).grid(row=6, column=0, padx=(10,0))

nameEntry = tk.Entry(root, width = 30)
collegeEntry = tk.Entry(root, width = 30)
phoneEntry = tk.Entry(root, width = 30)
addressEntry = tk.Entry(root, width = 30)

nameEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))
collegeEntry.grid(row=2, column=1, padx=(0,10), pady = 20)
phoneEntry.grid(row=3, column=1, padx=(0,10), pady = 20)
addressEntry.grid(row=4, column=1, padx=(0,10), pady = 20)

testVars = []
tests = ['Test 1', 'Test 2', 'Test 3', 'Test 4', 'Test 5']
for i, test in enumerate(tests):
    var = tk.BooleanVar()
    testVars.append(var)
    test_checkbox = tk.Checkbutton(root, text=test, variable=var, font=('Arial', 12, 'bold'))
    test_checkbox.grid(row=i + 5, column=1, padx=10, pady=5, sticky='w')

unitVars = []
units = ['Unit 1', 'Unit 2', 'Unit 3', 'Unit 4', 'Unit 5']
for i, unit in enumerate(units):
    var = tk.BooleanVar()
    unitVars.append(var)
    unit_checkbox = tk.Checkbutton(root, text=unit, variable=var, font=('Arial', 12, 'bold'))
    unit_checkbox.grid(row=i + 6, column=1, padx=10, pady=5, sticky='w')

def takeNameInput():
    global nameEntry, collegeEntry, phoneEntry, addressEntry
    global TABLE_NAME, STUDENT_NAME, STUDENT_COLLEGE, STUDENT_ADDRESS, STUDENT_PHONE, STUDENT_TESTS, STUDENT_UNITS
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)
    collegeName = collegeEntry.get()
    collegeEntry.delete(0, tk.END)
    phone = int(phoneEntry.get())
    phoneEntry.delete(0, tk.END)
    address = addressEntry.get()
    addressEntry.delete(0, tk.END)
    tests_selected = ', '.join([tests[i] for i, var in enumerate(testVars) if var.get()])
    units_selected = ', '.join([units[i] for i, var in enumerate(unitVars) if var.get()])
    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
                       STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", " +
                       STUDENT_PHONE + ", " + STUDENT_TESTS + ", " +
                       STUDENT_UNITS + " ) VALUES ( '"
                       + username + "', '" + collegeName + "', '" +
                       address + "', " + str(phone) + ", '" +
                       tests_selected + "', '" + units_selected + "' ); ")
    connection.commit()
    messagebox.showinfo("Success", "Data Saved Successfully.")

def destroyRootWindow():
    root.destroy()
    secondWindow = tk.Tk()
    secondWindow.title("Display results")
    appLabel = tk.Label(secondWindow, text="Student Management System", fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()
    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four", "five", "six")
    tree.heading("one", text="Student Name")
    tree.heading("two", text="College Name")
    tree.heading("three", text="Address")
    tree.heading("four", text="Phone Number")
    tree.heading("five", text="Tests")
    tree.heading("six", text="Units")
    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    i = 0
    for row in cursor:
        tree.insert('', i, text="Student " + str(row[0]),
                    values=(row[1], row[2], row[3], row[4], row[5], row[6]))
        i = i + 1
    tree.pack()

button = tk.Button(root, text="Take input", command=lambda :takeNameInput())
button.grid(row=7, column=0, pady=30)

displayButton = tk.Button(root, text="Display result", command=lambda :destroyRootWindow())
displayButton.grid(row=7, column=1)

root.mainloop()
