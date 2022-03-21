# class Student:
#     def __init__(self,age):
#         self.age=age
# s1=Student(25)
# s2=Student(23)
# print(s1+s2) #TypeError: unsupported operand type(s) for +: 'Student' and 'Student'

#Extra Magic Word
# class Student:
#     def __init__(self,age):
#         self.age=age
#     def __add__(self,other):
#         return self.age+other.age
# s1=Student(25)
# s2=Student(23)
# print(s1+s2)

# class Student:
#     def __init__(self,age):
#         self.age=age
#     def __sub__(self,other):
#         return self.age-other.age
# s1=Student(25)
# s2=Student(23)
# print(s1-s2)

# class Employee:
#     def __init__(self,name,eid):
#         self.name=name
#         self.eid=eid
#     def __gt__(self,other):
#         return self.eid>other.eid
# e1=Employee('rahul',150)
# e2=Employee('Priyanka',122)
# print(e1>e2)
# print(e1<e2)

# class Employee:
#     def __init__(self,name,eid,esal):
#         self.name=name
#         self.eid=eid
#         self.esal=esal
# class Workingdays:
#     def __init__(self,days):
#         self.days=days
#     def __mul__(self,other):
#         return self.days*other.esal
# e=Employee('Priyanka',120,500)
# w=Workingdays(26)
# print(w*e)

class Employee:
    def __init__(self,name,eid,esal):
        self.name=name
        self.eid=eid
        self.esal=esal
    def __mul__(self,other):
        return self.esal*other.days
class Workingdays:
    def __init__(self,days):
        self.days=days
e=Employee('Priyanka',120,500)
w=Workingdays(26)
print(e*w)