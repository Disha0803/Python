import mysql.connector as mc
con=mc.connect(host="localhost",database='universityy',user='root',password='')
cursor=con.cursor()
cursor.execute("update emp set esal=esal+5000")
con.commit()
print('emp salary 5000 increases')