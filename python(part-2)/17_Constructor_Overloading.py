class Demo:
    def __init__(self):
        print("hello")
    def __init__(self,a):
        self.a=a
        print(self.a)
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(self.a)
        print(self.b)
# d=Demo() #TypeError: __init__() missing 2 required positional arguments: 'a' and 'b'
# d=Demo(10) #TypeError: __init__() missing 1 required positional argument: 'b'
d=Demo(10,20)
