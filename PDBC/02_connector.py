#create a table
import mysql.connector as mc
con=mc.connect(host="localhost",database='universityy',user="root",password='')
cursor=con.cursor()
sql="insert into emp(eid,ename,esal) VALUES(%s,%s,%s)"
data=[(101,'rahul',25000),(102,'Priyanka',25000),(103,'Jack',35000)]
cursor.executemany(sql,data)
print('data inserted successfully')