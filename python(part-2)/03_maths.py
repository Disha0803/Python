class math:
    def __init__(self,a,b):
        self.add=a+b
        self.sub=a-b
        self.mul=a*b
        self.div=a/b
    def printData(self):
        print(self.add)
        print(self.sub)
        print(self.mul)
        print(self.div)

a=math(10,5)     
a.printData()   