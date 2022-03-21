class Student:
    """This class contains info abt Students"""
    # def __init__(self):
    #     self.name="Disha"
    #     self.roll=34
    #     self.age=21
    #     self.email="mdishabls@gmail.com"
    # def printData(self):
    #     print(self.name)
    #     print(self.age)
    #     print(self.roll)
    #     print(self.email)

    def __init__(self,name,age,roll,email):
        self.name=name
        self.roll=roll
        self.age=age
        self.email=email
    def printData(self):
        print(self.name)
        print(self.age)
        print(self.roll)
        print(self.email)

print(Student.__doc__)
s=Student('Sibun',19,21,'sibun@gmail.com')
s.printData()
s=Student('Sweety',34,21,'sweety@gmail.com')
s.printData()
s=Student('Suraja',51,19,'suraja@gmail.com')
s.printData()