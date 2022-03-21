from abc import*
# class Animal(ABC):
#     def noOfLegs(self):
#         pass
# class Tiger(Animal):
#     def noOfLegs(self):
#         return 4
# class Insects(Animal):
#     def noOfLegs(self):
#         return 6
# i=Insects()
# print(i.noOfLegs())
# t=Tiger()
# print(t.noOfLegs())

# ------------------------------------------------- No Output No Error -------------------------------------------------------
# class Test:
#     pass
# t=Test()
# -------------------------------------------------
# class Test(ABC):
#     pass
# t=Test()
#--------------------------------------------------
# class Test(ABC):
#     def m1(self):
#         pass
# t=Test()
# ------------------------------------------------- ERROR -------------------------------------------------------
# class Test(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
# t=Test() #TypeError: Can't instantiate abstract class Test with abstract methods m1
#--------------------------------------------------------------------------------------------
# class Test(ABC):
#     def m1(self):
#         pass
#     @abstractmethod
#     def m2(self):
#         pass
# t=Test() #TypeError: Can't instantiate abstract class Test with abstract methods m2
#--------------------------------------------------------------------------------------------
class Test(ABC):
    @abstractmethod
    def m1(self):
        print("Hello")
t=Test() #TypeError: Can't instantiate abstract class Test with abstract methods m1