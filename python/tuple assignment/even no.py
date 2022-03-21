t=input("Enter a tuple")
list=t.split(",")
t1=tuple(list)
print("Even numbers are:")
for i in t1:
    if(int(i)%2==0):
        print(i)