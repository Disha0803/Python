class Parent:
    def fun1(self):
        print("Hi.... this is Parent")  
class Child(Parent):
    def fun2(self):
        print("Hi...this is Child")
obj=Child() 
obj.fun1()
obj.fun2()