from sqlite3 import connect
import mysql.connector as mc
con=mc.connect(host="localhost",database="SOA_University",user="root",password='')
Cursor=con.cursor()
Cursor.execute("Create table emp(eid int(5),ename varchar(20),esal int(10))")
print("Table created successfully")