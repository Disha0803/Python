list=input("Enter a list")
c=0
for i in list:
    if(i!=[]):
        c=1
if(c==1):
    print("List is not empty")
else:
    print("List is empty")