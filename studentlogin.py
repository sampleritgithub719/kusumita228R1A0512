from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import ImageTk
def saveData():

    conn=mysql.connector.connect(host="localhost", user="root", password="kusumita@777", database="customerdata")
    if(usernameEntry.get()==''or emailEntry.get()==''or passwordEntry.get()==''):
      messagebox.showerror('Error',"all fields are mandatary")
    else:
        mycur=conn.cursor()
    sql='insert into student(username,email,password)values(%s,%s ,%s)'
    mycur.execute(sql,(usernameEntry.get(),passwordEntry.get(),emailEntry.get()))
    conn.commit()
window = Tk()
#window.geometry('925x500+300+200')
#window.resizable(False,False)
#background =ImageTk.PhotoImage(file='C:\\Users\Bkusm\Desktop\\download.jpg')

#blabel=Label(window,image=background)
#blabel.grid()
# Add widgets and set up your GUI here
frame = Frame(window)
frame.place(x=600,y=100)

# Create a label widget and place it in the frame using grid geometry manager
usernameLabel = Label(frame, text="Name",font=('Arial',15,'bold'), bg='white', fg='black')
usernameLabel.grid(row=0, column=0)
usernameEntry = Entry(frame, width=30)
usernameEntry.grid(row=0, column=1)


emailLabel = Label(frame,text="Roll No",font=('Arial',15,'bold'),bg='white',fg='black')
emailLabel.grid(row=2, column=0)
emailEntry = Entry(frame, width=30)
emailEntry.grid(row=2, column=1)


passwordLabel = Label(frame, text="Password",font=('Arial',15,'bold'),bg='white',fg='black')
passwordLabel.grid(row=1, column=0)
passwordEntry = Entry(frame,width=30)
passwordEntry.grid(row=1,column=1)

button=Button(frame,text="submit" ,command=saveData)
button.grid(row=4, column=1)
window.mainloop()