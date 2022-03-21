class father:
    def fun1(self):
        print("Father method 1")
    def fun2(self):
        print("Father method 2")
    def fun(self):
        print("Common method Father")
class mother:
    def fun3(self):
        print("Mother method 1")
    def fun4(self):
        print("Mother method 2")
    def fun(self):
        print("Common method Mother")
class son(father,mother):
    # def fun1(self):
    #     print("Son method")
    pass
class son2(mother,father):
    pass
obj=son()
obj.fun1()
obj.fun2()
obj.fun3()
obj.fun4()
obj.fun()


obj2=son2()
obj2.fun()