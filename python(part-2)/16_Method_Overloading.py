# class Demo:
#     def m1(self):
#         print("hello")
#     def m1(self,x):
#         self.x=x
#         print(self.x)
#     def m1(self,a,b):
#         self.a=a
#         self.b=b
#         print(self.a)
#         print(self.b)
# d=Demo()
# d.m1(10) #TypeError: m1() missing 1 required positional argument: 'b'
# d.m1(10,20)

#Handling Overloaded Method
#Using default argument
# class Demo:
#     def mul(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             print(a+b+c)
#         if a!=None and b!=None:
#             print(a+b)
#         if a!=None:
#             print(a)
#         else:
#             print("Please provide atleast one argument")
# d=Demo()
# d.mul(10,20)
# d.mul(10,20,30)
# d.mul(10)
# d.mul()

#Using Variable number argument
class Demo:
    def add(self,*a):
        result=0
        for i in a:
            result=result+i
        print(result)
d=Demo()
d.add(10,20,30,40,50)