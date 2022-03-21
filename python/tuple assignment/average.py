t=input("Enter a tuple")
list=t.split(",")
t=tuple(list)
s=0
for i in t:
    s=s+int(i)
avg=s/len(t)
print("Average= ",avg)