list=[2,5,6,7,8,9,13]
se=0
so=0
for i in list:
    if i%2==0:
        se=se+1
    else:
        so=so+1
print("Total number of even numbers: ",se)
print("Total number of odd numbers: ",so)