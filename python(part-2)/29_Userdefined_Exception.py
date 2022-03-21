class VeryYoung(Exception):
    def __init__(self,x):
        self.msg=x
class VeryOld(Exception):
    def __init__(self,x):
        self.msg=x
age=int(input("Enter ur age to check you are eligible or not"))
try:
    if age<18:
        raise VeryYoung("HEllo wait upto 18 years")
    if age>26:
        raise VeryOld("Sorry ur age is crossed")
except VeryYoung as x:
    print (x)
except VeryOld as y:
    print(y)