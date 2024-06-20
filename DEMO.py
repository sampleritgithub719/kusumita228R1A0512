
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

# Function to create the database table if it doesn't exist
def createTable():
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='kusumita@777',
                                      database='percentile_data')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS percentiles (
                        name TEXT,
                        id TEXT,
                        rank INTEGER,
                        total_participants INTEGER,
                        percentage REAL
                        )''')
        conn.commit()
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        cursor.close()
        conn.close()

# Function to calculate the percentile
def getPercentile():
    try:
        students = int(total_participantField.get())
        rank = int(rankField.get())
        result = round((students - rank) / students * 100, 3)
        messagebox.showinfo("Percentile Result", f"The percentile is: {result}%")

        # Save data to MySQL database
        conn = mysql.connector.connect(host='localhost', user='root', password='kusumita@777',
                                      database='percentile_data')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO percentiles (name, id, rank, total_participants, percentage) VALUES (%s, %s, %s, %s, %s)",
                      (nameField.get(), idField.get(), rank, students, result))
        conn.commit()
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        cursor.close()
        conn.close()

# Function to retrieve data from the database
def showData():
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='kusumita@777', database='percentile_data')

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM percentiles")
        rows = cursor.fetchall()

        # Display data in a pop-up messagebox
        if rows:
            data_str = "\n".join(
                [f"Name: {row[0]}, ID: {row[1]}, Rank: {row[2]}, Total Participants: {row[3]}, Percentage: {row[4]}%" for row in rows])
            messagebox.showinfo("Data", data_str)
        else:
            messagebox.showinfo("Data", "No data available.")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        cursor.close()
        conn.close()

# Function to clear the contents of all text entry boxes
def Clear():
    nameField.delete(0, END)
    idField.delete(0, END)
    rankField.delete(0, END)
    total_participantField.delete(0, END)
    percentileField.delete(0, END)

# Driver Code
if __name__ == "__main__":
    # Create a GUI window
    gui = Tk()

    # Create the database table
    createTable()

    # Load the image using PIL
    try:
        pil_image = Image.open("background.jpg")
    except FileNotFoundError:
        messagebox.showerror("Error",
                             "Image file not found. Please make sure 'education.jpg' is in the same directory as this script.")
        gui.destroy()
        exit()

    background_image = ImageTk.PhotoImage(pil_image)

    # Create a Canvas widget
    canvas = Canvas(gui, width=background_image.width(), height=background_image.height())
    canvas.pack(fill="both", expand=True)

    # Display the image on the canvas
    canvas.create_image(0, 0, image=background_image, anchor="nw")

    # Set the name of tkinter GUI window
    gui.title("Rank Based- Percentile Calculator")

    # Set the configuration of GUI window
    gui.geometry(f"{background_image.width()}x{background_image.height()}")

    # Define widget widths for alignment
    entry_width = 200
    label_width = 150
    button_width = 150
    vertical_spacing = 50
    button_spacing = 20

    # Define starting x and y positions
    start_x = 50
    start_y = 50

    # Create the widgets
    name = Label(gui, text="Name", bg="white")
    nameField = Entry(gui)
    id_label = Label(gui, text="ID", bg="white")
    idField = Entry(gui)
    rank = Label(gui, text="Rank", bg="white")
    rankField = Entry(gui)
    total_participant = Label(gui, text="Total Participants", bg="white")
    total_participantField = Entry(gui)
    find = Button(gui, text="Find Percentile", fg="black", bg="white", command=getPercentile)
    clear = Button(gui, text="Clear", fg="Black", bg="white", command=Clear)
    percentile = Label(gui, text="Percentile", bg="white")
    percentileField = Entry(gui)
    show_data_btn = Button(gui, text="Show Data", fg="Black", bg="white", command=showData)

    # Place the widgets on the canvas, line by line
    current_y = start_y
    canvas.create_window(start_x, current_y, window=name, anchor="nw")
    canvas.create_window(start_x + label_width, current_y, window=nameField, width=entry_width, anchor="nw")

    current_y += vertical_spacing
    canvas.create_window(start_x, current_y, window=id_label, anchor="nw")
    canvas.create_window(start_x + label_width, current_y, window=idField, width=entry_width, anchor="nw")

    current_y += vertical_spacing
    canvas.create_window(start_x, current_y, window=rank, anchor="nw")
    canvas.create_window(start_x + label_width, current_y, window=rankField, width=entry_width, anchor="nw")

    current_y += vertical_spacing
    canvas.create_window(start_x, current_y, window=total_participant, anchor="nw")
    canvas.create_window(start_x + label_width, current_y, window=total_participantField, width=entry_width,
                         anchor="nw")

    current_y += vertical_spacing
    canvas.create_window(start_x, current_y, window=find, width=button_width, anchor="nw")

    current_y += vertical_spacing + button_spacing
    canvas.create_window(start_x, current_y, window=percentile, anchor="nw")
    canvas.create_window(start_x + label_width, current_y, window=percentileField, width=entry_width, anchor="nw")

    current_y += vertical_spacing + button_spacing
    canvas.create_window(start_x, current_y, window=clear, width=button_width, anchor="nw")

    current_y += vertical_spacing + button_spacing
    canvas.create_window(start_x, current_y, window=show_data_btn, width=button_width, anchor="nw")

    # Prevent




    gui.background_image = background_image

    # Start the GUI
    gui.mainloop()
