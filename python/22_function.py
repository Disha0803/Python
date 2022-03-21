# a=90

# def fun1():
#       print(a)
      
# def fun2():
#       a=100
#       print(a)
      
# fun1()
# fun2()



#-------------

# def fun1():
#       a=90
#       print(a)
      
# def fun2():
      
#       print(a)#name 'a' is not defined
      
# fun1()
# fun2()


#-------------
# def fun1():
#       a=90
#       print(a)
      
# def fun2():
#       fun1()
      
 
# fun1()
# fun2()


#----------

# a=10
# def fun1():
#       global a
#       a=999
#       print(a)
      
# def fun2():
#       print(a)
      
# fun1()
# fun2()


#-------------
#globals() 
# a=10 #global

# def fun1():
#       a=999 #local 
#       print(a) #999
#       #how t0 access global variable here
#       print(globals()['a'])   
# fun1()

#-----------------

#Recursion 
# If a function call itself is called as recusion

# def fun1():
#       fun1() # function calling itself 

# find out the factorial of a number using recusrion 

# def fact(num):
#       if num==0:
#             result=1
#       else:
#             result=num*fact(num+1)
#       return result
      
# a=fact(6)
# print(a)

#Lambda Expression /Function 

# a=lambda num:num*num

# print(a(5))
# print(a(6))
# print(a(3))


# a=lambda num:num

# print(a(5))
# print(a(6))
# print(a(3))


#take 2 numbers as an argument then find out the large number using lambda 

# x=lambda a,b: a if a>b else b
# print(x(4,5))