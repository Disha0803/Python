class Parent:
    a=50
    b=100
    def __init__(self):
        self.c=555
        self.d=666
class Child(Parent):
    def __init__(self):
        self.c=5555
        self.d=6666
        self.e=9999
class SmallChild(Child):
    def __init__(self):
        pass
c=Child()
print(c.c)
print(c.d)
print(c.e)
sc=SmallChild()
print(sc.e)
print("hello")