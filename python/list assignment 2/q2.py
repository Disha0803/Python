list1=[10,20,20,40,50,60,80,60]
list2=[20,20,40,50,60,80,60]
for i in range(len(list1)):
    for j in range(len(list2)):
        if(list1[i]==list2[i]):
            del(list1[i])
print(list)