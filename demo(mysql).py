import mysql.connector
mydb=mysql.connector.connect(host="localhost",username="root",password="kusumita@777",database="mydb")
mycurs=mydb.cursor()
#mycurs.execute("create database mydb")
#mycurs.execute("show databases")
#
#mycurs.execute("show tables")
#mycurs.execute("create table users(name varchar(50),email varchar(50),password varchar(50))")
sql="insert into users(name,email,password)values(%s, %s ,%s)"
val=("gita","abc@gmail.com","888")
#mycurs.execute(sql,val)
#print(mycurs)
mycurs.execute("select * from users")
for i in mycurs:
    print(i)
