#CODE_1
# class Demo:
#     def m1(self):
#         print("I am an instance method from Demo class")
# class Test(Demo):
#     def m1(self):
#         super().m1()
#         print("I am an instance method from Test class")
# t=Test()
# t.m1()

#CODE-2
# class Human:
#     def __init__(self,name,age,email):
#         self.name=name
#         self.age=age    
#         self.email=email
# class Employee(Human):
#     def __init__(self,name,age,email,sal,addr):
#         self.name=name
#         self.age=age    
#         self.email=email
#         super().__init__(name,age,email)
#         self.sal=sal
#         self.addr=addr
#     def printData(self):
#         print(self.name)
#         print(self.age)
#         print(self.email)
#         print(self.sal)
#         print(self.addr)
# e=Employee('Priyanka',23,'priyanka@gmail.com',20000,'BBSR')
# e.printData()

#CODE-3
# class Demo: 
#     s=10
#     t=20
#     u=100
#     def __init__(self):
#         self.v=200
#         self.f=350
#     def m1(self):
#         print("Hello Thank you")
#     @classmethod
#     def m2(self):
#         print("Hyy")
#     @staticmethod
#     def m3():
#         print("Byy")
# class Test(Demo):
#     def __init__(self):
#         super().__init__()
#         print(super().s)
#         print(super().t)
#         print(super().u)
#         super().m1()
#         super().m2()
#         super().m3()
#         print(self.v)
# t=Test()

#CODE-4 (Calling method of a particular super class)
# class A1:
#     def m1(self):
#         print('A1')
# class B1(A1):
#     def m1(self):
#         print('B1')
# class C1(B1):
#     def m1(self):
#         print('C1')
# class D1(C1):
#     def m1(self):
#         print('D1')
#         super().m1() #C1
#         A1.m1(self)  #A1
#         B1.m1(self)  #B1
# d=D1()
# d.m1()

#CODE-5
# class Demo:
#     def __init__(self):
#         print("Hello")
#     def m1(self):
#         print("Instance Method")
#     @classmethod
#     def m2(cls):
#         print("Class method")
#     @staticmethod
#     def m3():
#         print("Static Method")
# class Test(Demo):
#     @classmethod
#     def c1(cls):
#         # super().__init__() #error
#         # super().m1() #error
#         super().m2() #Class method
#         super().m3() #Static Method
# Test.c1()

# -------------------------------------------------
# class Test(Demo):
#     def i1(self):
#         super().__init__()
#         super().m1()
#         super().m2()
#         super().m3()
# t=Test()
# t.i1()

#--------------------------------------------------
# class Test(Demo):
#     def __init__(self):
#         super().__init__()
#         super().m1()
#         super().m2()
#         super().m3()
# t=Test()
# -------------------------------------------------
##### ERROR #####
# class Test(Demo):
#     @staticmethod
#     def m1():
#         super().__init__()
#         super().m1()
#         super().m2()
#         super().m3()
# t=Test()
# t.m1()
#---------------------------------------------------
##### SOLUTION #####
# class Demo:
#     @staticmethod
#     def m1():
#         print("Thank you")
# class Test(Demo):
#     @staticmethod
#     def s1():
#         super(Test,Test).m1()
# Test.s1()

# class Test:
#     def __init__(self):
#         print("Thank you")
#     def m1(self):
#         print("Hyy")
# class Demo(Test):
#     @classmethod
#     def c1(cls):
#         super(Demo,cls).__init__(cls)
#         super(Demo,cls).m1(cls)
# Demo.c1()