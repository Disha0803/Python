import pickle
class employee:
    def __init__(self,ename,esal):
        self.ename=ename
        self.esal=esal
    def display(self):
        print(self.ename)
        print(self.esal)
# with open('emp.txt','wb') as f:
#     ch=' '
#     while(ch!='n'):
#         ename=input("Enter the employee name: ")
#         esal=int(input("Enter the employee salary: "))
#         obj=employee(ename,esal)
#         pickle.dump(obj,f)
#         ch=input("Do you want to enter more??: y|n: ")
#     print("Successfully pickled")
f=open('emp.txt','rb')
while True:
    try:
        x=pickle.load(f)
        x.display()
    except EOFError:
        print("Done")
        break
    
    