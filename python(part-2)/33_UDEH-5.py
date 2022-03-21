class num(Exception):
    def __init__(self,x):
        self.msg=x
try:
    for i in range(1,5001):
        if i==4500:
            raise num("Too many numbers already printed")
        else:
            print(i)
except num as n:
    print(n)