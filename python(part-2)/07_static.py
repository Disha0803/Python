# class Demo:
#     a=90
#     def __init__(self):
#         self.b=100
# d1=Demo()
# d2=Demo()
# d3=Demo()
# print(d1.a,d1.b)
# print(d2.a,d2.b)
# print(d3.a,d3.b)
# d1.b=500
# print(d1.a,d1.b)
# print(d2.a,d2.b)
# Demo.a=9999
# print(d1.a,d1.b)
# print(d2.a,d2.b)

# class Demo:
#     x=90
# d1=Demo()
# print(d1.__dict__) //{} 

# class Demo:
#     def fun1(self):
#         Demo.x=190
#         self.x=100
# d1=Demo() 
# d1.fun1()
# print(d1.__dict__) //{'x': 100}

# Constructor

# class Demo:
#     def __init__(self):
#         Demo.x=90
#         self.x=90
# d1=Demo()
# print(d1.__dict__)

# class Demo:
#     @classmethod
#     def fun1(cls):
#         cls.x=90
#         Demo.y=500
# d1=Demo()
# d1.fun1()
# print(d1.__dict__) //{}

# class Demo:
#     @staticmethod
#     def fun1(cls):
#         Demo.x=90
# d1=Demo()
# # d1.fun1()
# print(d1.__dict__) //{}
