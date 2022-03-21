list=[30,40,50,60,'helo','hi','Priyanka','Jini']
list2=[]
list3=[]
for i in list:
    if(type(i)==int):
        list2.append(i)
    else:
        list3.append(i)
print(list2)
print(list3)