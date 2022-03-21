# user defined function 
# def myfun():
#       print('this is my first function')

# myfun()
# myfun()
# myfun()
# myfun()


# def myfun(name):  # parameter / formal arumnet 
#       print(name)
      

# myfun('surendra')  # argument  / actual argumnet 
# myfun(55)
# myfun(45.26)


# def fun(num):
#       print(num*num*num)

# fun(5)
# fun(3)


# def cal(a,b,c,d):
#       return a*b*c*d

# print(cal(10,20,30,40))
# print(cal('priyanka','rahul','scoot','jack'))



# def cal(a,b,c,d):
#       print('hello')
#       print('hello')
#       return a*b*c*d  
     



# print(cal(2,10,20.25,30))


# def even_odd(num):
#       if(num%2==0):
#             print('enen number')
#       else:
#             print('odd number')
            
            
# even_odd(50)
# even_odd(555)    


# def fun():
#       print('hello')       
      
# # fun()
# print(fun())

#python return multiple value 

# def cal(a,b):
#       add=a+b
#       sub=a-b
#       return add,sub,a,b

# i,j,k,l=cal(10,20)

# positional argument 
# def fun(roll,age):
#       print(roll)
#       print(age) 
      
# x=int(input('enter roll'))
# y=int(input('enter age'))

# fun(x,y)



# def fun(roll,age):
#       print(roll)
#       print(age) 
      
# fun(23,23)


#keyword (parameter name ) argument

# def fun(name,wish):
#       print(name)
#       print(wish)
      
# fun(wish='good morning',name='surendra')
# fun(name='surendra',wish='good morning')
# fun('surendra',wish='good morning')
# fun(wish='good morning','surendra') #positional argument follows keyword argument


#default argument 

# def fun(name="unknown"):
#       print('hyy',name)
      
# # fun('surendra')
# # fun()

# def fun(name="unknown",msg="good moring"):
#       print('hyy',name)
#       print(msg)
      

# # # fun()
# fun('rahul','good night')




# def fun(name,msg="hello"):
#       print('hyy',name)
#       print(msg)
      

# fun('rahul')



# def fun(msg="hello",name): #non-default argument follows default argument
#       print('hyy',name)
#       print(msg)
      
# fun('rahul')


# variable length argumnet 

# def add(*n):
#       result=0
#       for i in n:
#             result=result+i
#       print(result)
      
# add(10,20,30)
# add(10,20)
# add(55.55,23,25,89.00)

#variable length argumnet  with positional argumnet 

# def fun(x,*n):
#       print(x)
#       print(n)
      
# fun(10)
# fun(10,50,20,60,40,50,60,40,50,20,30,80)
# fun('rahul',50,20,60,40,50,'priyanka',60,40,50,20,30,80)


# def fun(*n,x):
#       print(x)
#       print(n)
      
# fun(10,20)


# def fun(*n,x):
#       print(x)
#       print(n)
      
# fun(10,x=20)


# def fun(*n,x):
#       print(x)
#       print(n)
      
# fun(x=10,20) #positional argument follows keyword argument

def fun(*kwargs):
      print(kwargs)

fun('priyanka',23,23,'CET')
# fun(name='priyanka',roll=23,age=23,college='CET')


def fun(**kwargs):
      for i,j in kwargs.items():
            print(i,"=",j)


fun(name='priyanka',roll=23,age=23,college='CET')



# def fun(**kwargs):
#       for i in kwargs.values():
#             print(i)


# fun(name='priyanka',roll=23,age=23,college='CET')

# def fun(**kwargs):
#       for i in kwargs.keys():
#             print(i)


# fun(name='priyanka',roll=23,age=23,college='CET')
