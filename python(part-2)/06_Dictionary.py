# dict={
#     'dog':'animal',
#     'cat':'me'
# }
# w=input("enter a word")
# m=input("enter its meaning")
# d={w:m}
# di={}
# di.update(d)
# w=input("enter a word")
# m=input("enter its meaning")
# d={w:m}
# di.update(d)
# s=input("Enter word")
# print(di)
# for i in di.keys():
#     if i==s:
#         print(i,"--->",di[i])





class Dictionary:
    def __init__(self,key,value):
        self.key=key
        self.value=value
    def fun(self,key,value):
        print(self.key,"--->",self.value)
di={}
while True:
    
    w=input("enter a word: ")
    m=input("enter its meaning: ")
    d={w:m}
    di.update(d)
    obj=Dictionary(w,m)
    
    ch=input("Do u want to add more words? (Y/N): ")
    ch=ch.upper()
    if(ch=='N'):
        break
s=input("Enter a word for which u want the meaning: ")
for i in di.keys():
        if i==s:
            obj.fun(i,d[i])
        # else:
        #     print("NOt found")
                