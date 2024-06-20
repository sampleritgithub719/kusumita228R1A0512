import sqlite3
con=sqlite3.connect("mydatabase.db")
cur=con.cursor()

#cur.execute("create table if not exists student(name varchar(50),rollno varchar(50),section varchar(50))")
#cur.execute('insert into student values("kusu","512","A")')
#cur.execute('insert into student values("pranu","516","A")')
#cur.execute('insert into student values("mano","531","A")')
#cur.execute('delete from student where rollno=516')
#cur.execute('update student set  name="chottu" where rollno=531')
x=cur.execute('select * from student')
print(x.fetchall())
con.commit()


