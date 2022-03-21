list1=[1,2,[6,5]]
l=len(list1)
print(l)
c=0
for i in range(len(list1)):
    for j in range(len(list1[i])):
        c=c+1
print(c)
if(c==l):
    print("List is not nested")
else:
    print("List is nested")