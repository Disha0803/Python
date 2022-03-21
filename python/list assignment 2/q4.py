list=[10,20,20,40,50,40,60,80,60]
l=len(list)-1
temp=list[0]
list[0]=list[l]
list[l]=temp
print(list)