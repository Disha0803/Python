# class Test:
#     def __init__(self):
#         self.a=10 #Public
#         print(self.a)
# t=Test()
# print(t.a)
#---------------------------------------------
# class Test:
#     def __init__(self):
#         self.__a=10 #Private
#         print(self.__a)
# t=Test()
# print(t.__a) #Error
#---------------------------------------------
# class Test:
#     def __init__(self):
#         self._a=10 #Protected
#         print(self._a)
# class Demo(Test):
#     def __init__(self):
#         super().__init__()
# d=Demo()
#----------------------------------------------
class Test:
    _x=10 #Protected type
class Test1(Test):
    def __init__(self):
        print(Test._x)
t1=Test1()
print(Test._x) #Protected is still not available in Python, this is just a naming convention