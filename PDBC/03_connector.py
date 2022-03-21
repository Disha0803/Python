#retrieve from data
import mysql.connector as mc
con=mc.connect(host="localhost",database='universityy',user="root",password='')
cursor=con.cursor()
cursor.execute("select * from emp")
results=cursor.fetchall()
for i in results:
    print("Eid is: ",i[0])
    print("Eid is: ",i[1])
    print("Eid is: ",i[2])
