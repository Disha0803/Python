list=[5,4,8,10]
print("Original List",list)
t=list[0]
list[0]=list[(len(list))-1]
list[(len(list)-1)]=t
print("New List",list)