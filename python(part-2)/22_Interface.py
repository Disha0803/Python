from abc import*
class DBInterface(ABC):
    @abstractmethod
    def connect(self):
        pass
    def disconnect(self):
        pass
class Oracle(DBInterface):
    def connect(self):
        print("Connecting to Oracle Database")
    def disconnect(self):
        print("Disconnecting from Oracle Database")
class MySql(DBInterface):
    def connect(self):
        print("Connecting to MySql Database")
    def disconnect(self):
        print("Disconnecting from MySql Database")
dBName=input("Enter the Database Name that you want to connect")
classname=globals()[dBName] #String to class name
obj=classname()
obj.connect()
obj.disconnect() 