import mysql.connector as mc

con=mc.connect(host="localhost",database='university',user='root',password='')
cursor=con.cursor()
eid=input("enter your id : ")
ename=input("enter your name :")
esal=input("enter your sal : ")

sql="insert into emp1(eid,ename,esal) VALUES (%s,%s,%s)"
data=[(eid,ename,esal)]
cursor.executemany(sql,data)
con.commit()
print("Data inserted...")

choice=("if u want to insert one more row or not (y/n)")



    

