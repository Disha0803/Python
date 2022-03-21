class Student:
    def __init__(self):
        self.name="Disha"
        self.age=21
        self.roll=2041041034
    def display(self):
        print(self.name)
        print(self.age)
        print(self.roll)
    class DOB:
        def __init__(self):
            self.dd=27
            self.mm=11
            self.yy=2000
        def display(self):
            print(self.dd,end="/")
            print(self.mm,end="/")
            print(self.yy)
s=Student()
s.display()
# d=s.DOB()
# d.display()
d1=Student().DOB()
d1.display()
print(d1.mm) #11