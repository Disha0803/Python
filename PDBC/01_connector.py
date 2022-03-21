#create a table
import mysql.connector as mc
con=mc.connect(host="localhost",database='universityy',user="root",password='')
cursor=con.cursor()
cursor.execute("Create table emp(eid int(5), ename varchar(10), esal int(10))")
print('Table created successfully...')