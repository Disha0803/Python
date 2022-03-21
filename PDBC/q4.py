import mysql.connector as mc

con=mc.connect(host="localhost",database='university',user='root',password='')
cursor=con.cursor()
sid=input("Enter your id")
sql=("delete from student sid")
cursor.executemany(sql,sid)
con.commit()
print('dlt the data')