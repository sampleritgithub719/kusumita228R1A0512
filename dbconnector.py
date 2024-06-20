import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="kusumita@777"
)
mycur=conn.cursor()
if(mycur) :
    print("Success")
else :
    print("Problem in database")

q = "use customerdata"
mycur.execute(q)
query = "create table studentdb(name varchar(100),rollno varchar(100))"
mycur.execute(query)
window.mainloop()