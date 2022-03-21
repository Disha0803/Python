import pickle
class Emp:
    def __init__(self,eno,ename):
        self.eno=eno
        self.ename=ename
        
    
    def display(self):
        print(self.eno)
        print(self.ename)

# with open("emp.ser",'wb') as f:
#     obj=Emp(1,"suraj")
#     pickle.dump(obj,f)
#     print('success')

with open('emp.ser','rb') as f:
    x=pickle.load(f)
    x.display()