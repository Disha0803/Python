import mysql.connector as mc
class Trip:
    def __init__(self):
        self.con=mc.connect(host="localhost", database="Trip", user="root", password='')
    def create_table(self):
        sql="Create table PassengerList(redgno int(11), name varchar(30),sourceloc varchar(20), destloc varchar(20))"
        cursor=self.con.cursor()
        cursor.execute(sql)
        print("Table created")
    def insertion(self,redgno,name,sourceloc,destloc):
        sql="insert into PassengerList(redgno,name,sourceloc ,destloc) VALUES(%s,%s,%s,%s)"
        data=[(redgno,name,sourceloc,destloc)]
        cursor=self.con.cursor()
        cursor.executemany(sql,data)
        self.con.commit()
        print("Data inserted successfully")
    def updation(self,redgno,name,sourceloc,destloc):
        sql="update PassengerList set name=%s, sourceloc=%s, destloc=%s"
        val=[("Disha",'bbsr','ctc')]
        cursor=self.con.cursor()
        cursor.executemany(sql,val)
        self.con.commit()
        print("Data updated successfully")
    def deletion(self,redgno):
        sql="delete from PassengerList where redgno=%s"
        val=[(redgno)]
        cursor=self.con.cursor()
        cursor.executemany(sql,val)
        self.con.commit()
        print("Data deleted successfully")
    def display(self):
        sql="select * from PassengerList"
        cursor=self.con.cursor()
        cursor.executemany(sql)
        self.con.commit()
        print("Data deleted successfully")
    
obj=Trip()
# obj.create_table()
# obj.insertion(101,'priyanka','bbsr','ctc')