class grandfather:
    def fun1(self):
        print("I am grandfather")
class father(grandfather):
    def fun2(self):
        print("I am father")
class son(father):
    def fun3(self):
        print("I am son")
class grandson(son):
    def fun4(self):
        print("I am grandson")
# obj=son()
obj=grandson()
obj.fun4()
obj.fun3()
obj.fun2()
obj.fun1()