# print(10/2)
# print(10/4)
# print(10/0) #ZeroDivisionError: division by zero
# print(20/4) #Not executed
# print(100/10) #Not executed
#----------------------------------------------SOLUTION---------------------------------------------------
# print(10/2)
# print(10/4)
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Can't divide by zero") 
# print(20/4) 
# print(100/10)
#---------------------------------------------------------------------------------------------------------
#if b=0, by default a/2, a=10 (given)
# b=int(input('Enter the value of b: '))
# a=10
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print(a/2)
#----------------------------------------------------------------------------------------------------------
#try multiple except 
# try:
#     a=int(input('Enter the value of a: '))
#     b=int(input('Enter the value of b: '))
#     print(a/b)
# except ZeroDivisionError:
#     print("Division by zero is not possible")
# except ValueError:
#     print("Please Enter a Number")
#----------------------------------------------------------------------------------------------------------
# d={"one":1,"two":2,"three":3}
# try:
#     key=input("Enter a key for which you want to see the value: ")
#     print(d[key])
# except KeyError:
#     print("No such key exists")
#-----------------------------------------------------------------------------------------------------------
# list=[25,69,'disha',16,'google']
# try:
#     x=int(input("Enter a position: "))
#     print("Value:",list[x])
# except IndexError:
#     print("No such index exists")
#------------------------------------------------------------------------------------------------------------
try:
    a=int(input("Enter the value of a"))
    b=int(input("Enter the value of b"))
except Exception:
    print("Invalid input")
print("Hey there")