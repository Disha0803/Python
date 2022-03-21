list1=[10,20,20,40,5,40,60,80,60]
list2=[55,566,40,10,60,889,635]
print("The common numbers are:")
for i in range(len(list1)):
    for j in range(len(list2)):
        if(list2[j]==list1[i]):
            print(list2[j])            