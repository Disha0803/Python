#Inside Constructor(Declare Using Self)
# class Student:
#     def __init__(self):
#         self.name='rahul'
#         self.roll=28
#         self.age=23
#         self.mark=89
# s1=Student()
# print(s1.__dict__)

# Inside Instance Method(Declare Using Reference Variable)
# class Demo:
#     def __init__(self):
#         self.x=90
#         self.y=100
#     def fun1(self):
#         self.z=500         #Instance method
#     def fun2(self):
#         self.k='abc'
# d1=Demo()
# print(d1.__dict__)
# d1.fun1()
# print(d1.__dict__)
# d1.fun2()
# print(d1.__dict__)

# Outside Class(Declare Using Reference Variable)
# class demo:
#     def __init__(self):
#         self.x=90
#         self.y=100
#         self.z=150
#     def fun1(self):
#         self.a=777
#         self.b=888
# d1=demo()
# d1.fun1()
# d1.c=5000
# print(d1.__dict__)

# Access instance variable inside class
# Self Keyword
# class demo:
#     def __init__(self):
#         self.x=90
#         self.y=100
#         self.z=150
#     def fun1(self):
#        print(self.x)
#        print(self.y)
#        print(self.z)
# d1=demo()
# d1.fun1()
# print(d1.__dict__)

# Delete
# Self
# class demo:
#     def __init__(self):
#         self.x=90
#         self.y=100
#         self.z=150
#     def fun1(self):
#        self.a=777
#        self.b=888
#        del self.z
# d1=demo()
# d1.fun1()    
# print(d1.a,d1.b,d1.x,d1.y,d1.z)   # 'demo' object has no attribute 'z'

# Delete
# Reference
# class demo:
#     def __init__(self):
#         self.x=90
#         self.y=100
#         self.z=150
#     def fun1(self):
#        self.a=777
#        self.b=888
# d1=demo()
# d1.fun1()    
# del d1.z
# print(d1.a,d1.b,d1.x,d1.y,d1.z)   # 'demo' object has no attribute 'z'

# Instance Variable will differ from object to object(Proof)

# class demo:
#     def __init__(self):
#         self.x=90
#         self.y=100
#         self.z=150
# d1=demo()
# print(d1.x,d1.y,d1.z)
# print(d1)  #0x00000142A545FD90
# d2=demo()
# print(d2.x,d2.y,d2.z)
# print(d2)  #0x00000142A545FD30
# d3=demo()
# print(d3.x,d3.y,d3.z)
# print(d3)  #0x00000142A545FCA0

class demo:
    def __init__(self):
        self.x=90
        self.y=100
        self.z=150
d1=demo()
print(d1.x,d1.y,d1.z)
d2=demo()
d2.x=111
d2.y=333
d2.z=555
print(d2.x,d2.y,d2.z)
d3=demo()
d3.x=222
d3.y=444
d3.z=666
print(d3.x,d3.y,d3.z)

# 90 100 150
# 111 333 555
# 222 444 666