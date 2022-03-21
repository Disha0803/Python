class factnum(Exception):
    def __init__(self,x):
        self.msg=x
num=int(input("Enter a number to find out the factorial"))
try:
    if num>30:
        raise factnum("Can't find factorial of number greater than 30")
    else:
        fact=1
        for i in range(1,(num+1)):
            fact=fact*i
        print(fact)
except factnum as fn:
    print(fn)