list=[2,5,-6,7,8,-9,13]
sp=0
sn=0
for i in list:
    if i>=0:
        sp=sp+1
    else:
        sn=sn+1
print("Total number of positive numbers: ",sp)
print("Total number of negative numbers: ",sn)