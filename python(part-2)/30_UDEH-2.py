# class OnlyInt(Exception):
#     def __init__(self,x):
#         self.msg=x
# l=list()
# for i in range(1,6):
#     try:
#         i=input("Enter element in a list: ")
#         if (i>='a' and i<='z')or(i>='A' or i<='Z'):
#             raise OnlyInt("Sorry require only int data type")
#         else:
#             l.append(i)
#     except OnlyInt as oi:
#        print(oi)

class OnlyInt(Exception):
    def __init__(self,x):
        self.msg=x
list=[1,52,34]
try:
    for i in list:
        if type(i)!=int:
            raise OnlyInt("Sorry require only int data type")
except OnlyInt as oi:
    print(oi)