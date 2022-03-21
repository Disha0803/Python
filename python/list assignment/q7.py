list1=[[10,20,30],[40,50,60],[70,80,90]]
list3=[]
list2=[[21,21,23],[31,32,33],[61,62,63]]

for i in range(len(list1)):
    for j in range(len(list1[i])):
      list3.append(list1[i][j]+list2[i][j])
print(list3)