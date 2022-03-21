class name(Exception):
    def __init__(self,x):
        self.msg=x
try:
    n=input("Enter your name: ")
    for i in n:
        if (i>='a' and i<='z'):
            pass
        else:
            raise name("Name can contain only alphabets")
except name as n:
    print(n)