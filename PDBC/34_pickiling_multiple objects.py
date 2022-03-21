import pickle
class employe:
    def __init__(self,eno,ename):
        self.eno=eno
        self.ename=ename

    def display(self):
        print(self.eno)
        print(self.ename)

f=open('emp.ser','wb')
num=int(input('enter the number employess :'))

for i in range(num):
    eno=int(input("enter emp number :"))
    ename=(input("enter emp name :"))
    e=employe(eno,ename)
    pickle.dump(e,f)
    # print(i+1,'Dumped')
print('done')

f=open('emp.ser','rb')

while True:
    try:
        x=pickle.load(f)
        x.display()
    except EOFError:
        print('done')
        break

        

    