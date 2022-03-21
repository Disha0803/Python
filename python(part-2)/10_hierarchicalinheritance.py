class father:
    def fun(self):
        print("Father Property")
class son(father):
    pass
class daughter(father):
    pass
obj=son()
obj2=daughter()
obj.fun()
obj2.fun() 