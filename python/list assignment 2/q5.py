list=[1,2,3,4,5,6,7,8,9,11,12,13,15]
print("The missing numbers are:")
j=1
for i in list:
    for j in list:
        if(j-i!=1):
            print(j-1)
        else:
            continue