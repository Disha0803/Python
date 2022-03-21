# x=10
# if x==0
#     print('hello')

# x=10
# if x==10:
#     print('hello')
#         print('Hi')


# a=10
# b=0
# c=a/b
# print(c)

# l=[10,20,30,40]
# print(l[5])


# print(10/2)
# print(10/5)
# print(10/0) #ZeroDivisionError: division by zero
# print(20/4)
# print(100/10)


# print('surendra'+10)

# print(10/2)
# print(10/5)
# print(10/0) #ZeroDivisionError: division by zero
# print(20/4)
# print(100/10)


# print(10/2)
# print(10/5)
# try:
#     print(10/0) 
# except ZeroDivisionError:
#     print('U CANT DIVIDE WITH ZERO')
# print(20/4)
# print(100/10)


# print(10/2)
# print(10/5)
# try:
#     print(10/0) 
# except ZeroDivisionError:
#     print('u cant dive with 0')
# print(20/4)
# print(100/10)


# class Test:
#     def __init__(self):
#         self.a=10

# t=Test()
# print(t.x)


# qn:
# name=input('Enter ur name')
# a=10
# b=int(input('enter b value'))

# print('------')
# print(name)
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print(a/5)
# print('thank you')


# try with multiple except 
# try:
#     a=int(input('Enter a value'))
#     b=int(input('Enter b value'))
#     print(a/b)
# except ZeroDivisionError:
#     print('U cant divide by zero')
# except ValueError:
#     print('Hi provide int value only')


# flow of try-block
# try:
#     print('Hello')
#     print('Hy')
#     print(10/0)
#     print('Thank U')
#     print('Thank U')
# except ZeroDivisionError:
#     print('OOO')
#     print('ZZZ')

# print('Again Thank U')


# EX2 :
# try:
#     print('Hello')
#     print('Hy')
#     print(10/0)
#     print('Thank U')
#     print('Thank U')
# except ValueError:
#     print('OOO')
#     print('ZZZ')

# print('Again Thank U')


# try:
#     print('Hello')
#     print('Hy')
#     print(10/0)
#     print('Thank U')
#     print('Thank U')
# except ValueError:
#     print('OOO')
#     print('ZZZ')

# print('Again Thank U')


# EX3

# try:
#     print('Hello')
   
# except ZeroDivisionError:
#     print(10/0)

# print('Again Thank U')


# ex 4
# try:
#     print(10/0)
# except ZeroDivisionError:
#     try:
#         print(10/0)
#     except ZeroDivisionError:
#         print('Hi')

# print('Again Thank U')


# ex 5:
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print(10/0)

# print('Again Thank U')


# exception information 
# try:
#     print(10/0)
# except ZeroDivisionError as obj:
#     print(obj)
#     print(obj.__class__)
#     print(obj.__class__.__name__)

# try with multiple except block 
# try:
#     a=int(input('enter a value'))
#     b=int(input('enter b value'))
#     print(a/b)
# except ZeroDivisionError as z:
#     print(z)
# except ValueError as v:
#     print(v)


# ex 1:

# try:
#     a=int(input('enter a value'))
#     b=int(input('enter b value'))
#     print(a/b)
# except BaseException:
#     print('hi')



# try:
#     a=10
#     b=0
#     print(a/b)
# except ArithmeticError:
#     print('ae')
# except ZeroDivisionError:
#     print('ze')


# try:
#     a=10
#     b=0
#     print(a/b)
# except NameError:
#     print('ae')
# except ZeroDivisionError:
#     print('ze')

# One except block that can handle mutiple exception
# try:
#     a=int(input('enter a value'))
#     b=int(input('enter b value'))
#     print(a/b)
# except(ZeroDivisionError,ValueError):
#     print('hi')

# exception info.
# try:
#     a=int(input('enter a value'))
#     b=int(input('enter b value'))
#     print(a/b)
# except(ZeroDivisionError,ValueError) as obj:
#     print(obj)


# default exception block 
# try:
#     a=int(input('enter a value'))
#     b=int(input('enter b value'))
#     print(a/b)
# except ZeroDivisionError:
#     print('ze')
# except:
#     print('Plz give valid input')


# try:
#     a=int(input('enter a value'))
#     b=int(input('enter b value'))
#     print(a/b)
# except:
#     print('Plz give valid input')
# except ZeroDivisionError:
#     print('ze')

#Finally Block:

# try:
#     print('Hi')
# except:
#     print('hello')
# finally:
#     print('thank u')


# try:
#     print(10/0)
# except ZeroDivisionError:
#     print('hello')
# finally:
#     print('thank u')




# try:
#     print(10/0)
# except ValueError():
#     print('hello')
# finally:
#     print('thank u')


# _exit(0)
# ---------
# import os
# try:
#     print('hello')
#     print('hi')
#     os._exit(0)
# except ValueError:
#     print('by')
# finally:
#     print('thank u')


# try:
#     print('hello')
#     print('hi')
# except ValueError:
#     print('by')
# finally:
#     try:
#         print(10/0)
#     except ZeroDivisionError:
#         print('Handled')


# flow of execution try except finally

# try:
#     print('1')
#     print('2')
#     print('3')
#     print('4')
# except ValueError:
#     print('5')
# finally:
#     print('6')
   

# try:
#     print('1')
#     print('2')
#     print(10/0)
#     print('4')
# except ZeroDivisionError:
#     print('5')
# finally:
#     print('6')
   
# try:
#     print('1')
#     print('2')
#     print('3')
#     print('4')
# except ZeroDivisionError:
#     print(10/0)
# finally:
#     print('6')

# try:
#     print('1')
#     print('2')
#     print('3')
#     print('4')
# except ZeroDivisionError:
#     print('5')
# finally:
#     print(10/0)


#nested try-except finally 

# try:
#     print('1')
#     try:
#         print(10/0)
#     except ZeroDivisionError:
#         print('2')
#     finally:
#         print('3')
# except:
#     print('4')
# finally:
#     print('5')



# try:
#     print(10/0)
#     try:
#         print(10/0)
#     except ZeroDivisionError:
#         print('2')
#     finally:
#         print('3')
# except ZeroDivisionError:
#     print('4')
# finally:
#     print('5')



# try:
#     print('1')
#     try:
#         print('1.1')
#     except ZeroDivisionError:
#         print('2')
#     finally:
#         try:
#             print('3')
#         except ZeroDivisionError:
#             print('3.3')
#         finally:
#             print('22.9')
# except ZeroDivisionError:
#     print('4')
# finally:
#     print('5')



# try:
#     print('1')
#     try:
#         print(10/0)
#     except ValueError:
#         print('2')
#     finally:
#         try:
#             print('3')
#         except ZeroDivisionError:
#             print('3.3')
#         finally:
#             print('22.9')

# except:
#     pri
    

# try:
#     print('1')
#     print('2')
#     print('3')
#     print('3.3')
#     print('3.3.3')
#     try:
#         print('4')
#         print('5')
#         print('6')
#         print('6.6')
#         print('6.6.6')
#     except ZeroDivisionError:
#         print('7')
#         print('7.7')
#         print('7.7.7')
#     finally:
#         print('8')
#         print('9')
#         print('9.9')
#         print('9.9.9')
# except ZeroDivisionError:
#     print('10')
#     print('10.10')
#     print('10.10.10')
# finally:
#     print('11')
#     print('12')
#     print('12.12')
#     print('12.12.12')





# try:
#     print(10/0)
#     print('2')
#     print('3')
#     print('3.3')
#     print('3.3.3')
#     try:
#         print('4')
#         print('5')
#         print('6')
#         print('6.6')
#         print('6.6.6')
#     except ZeroDivisionError:
#         print('7')
#         print('7.7')
#         print('7.7.7')
#     finally:
#         print('8')
#         print('9')
#         print('9.9')
#         print('9.9.9')
# except ZeroDivisionError:
#     print('10')
#     print('10.10')
#     print('10.10.10')
# finally:
#     print('11')
#     print('12')
#     print('12.12')
#     print('12.12.12')
    


# try:
#     print('1')
#     print('2')
#     print('3')
#     print('3.3')
#     print('3.3.3')
#     try:
#         print(10/0)
#         print('5')
#         print('6')
#         print('6.6')
#         print('6.6.6')
#     except ZeroDivisionError:
#         print(10/0)
#         print('7.7')
#         print('7.7.7')
#     finally:
#         print('8')
#         print('9')
#         print('9.9')
#         print('9.9.9')
# except ZeroDivisionError:
#     print('10')
#     print('10.10')
#     print('10.10.10')
# finally:
#     print('11')
#     print('12')
#     print('12.12')
#     print('12.12.12')


# try:
#     print('1')
#     print('2')
#     print('3')
#     print('3.3')
#     print('3.3.3')
#     try:
#         print(10/0)
#         print('5')
#         print('6')
#         print('6.6')
#         print('6.6.6')
#     except ZeroDivisionError:
#         print(10/0)
#         print('7.7')
#         print('7.7.7')
#     finally:
#         print('8')
#         print('9')
#         print('9.9')
#         print('9.9.9')
# except ValueError:
#     print('10')
#     print('10.10')
#     print('10.10.10')
# finally:
#     print('11')
#     print('12')
#     print('12.12')
#     print('12.12.12')



# try:
#     print('1')
#     print('2')
#     print('3')
#     print('3.3')
#     print('3.3.3')
#     try:
#         print(10/0)
#         print('5')
#         print('6')
#         print('6.6')
#         print('6.6.6')
#     except ZeroDivisionError:
#         print(10/0)
#         print('7.7')
#         print('7.7.7')
#     finally:
#         print(10/0)
#         print('9')
#         print('9.9')
#         print('9.9.9')
# except ValueError:
#     print('10')
#     print('10.10')
#     print('10.10.10')
# finally:
#     print('11')
#     print('12')
#     print('12.12')
#     print('12.12.12')


# try:
#     print('1')
#     print('2')
#     print('3')
#     print('3.3')
#     print('3.3.3')
#     try:
#         print(10/0)
#         print('5')
#         print('6')
#         print('6.6')
#         print('6.6.6')
#     except ZeroDivisionError:
#         print(10/0)
#         print('7.7')
#         print('7.7.7')
#     finally:
#         print(10/0)
#         print('9')
#         print('9.9')
#         print('9.9.9')
# except ValueError:
#     print('10')
#     print('10.10')
#     print('10.10.10')
# finally:
#     print(10/0)
#     print('12')
#     print('12.12')
#     print('12.12.12')


#else block in try-except-finally 
# try:
#     print('1')
#     print('2')
# except ZeroDivisionError:
#     print('3')
# else:
#     print('I m else block')

# v  

# try:
#     print('1')
#     print(10/0)
# except ZeroDivisionError:
#     print('3')
# else:
#     print('I m else block')
# finally:
#     print('Im finally block')


# try:
#     print('1')
# except ZeroDivisionError:
#     print('3')
# else:
#     print('I m else block')
# finally:
#     print('Im finally block')

try:
    print('1')
except ZeroDivisionError:
    print('3')
else:
    print('I m else block')
    print('Im finally block')



# try:
# 	print('1')

# try:
# 	print('1')
# except:
#     print('2')

# try:
# 	pass
# except:
#     print('2')

# try:
# 	pass
# except:
#     pass


# try:
# 	pass
# except:
#     pass
# else:
#     print('hi')


# try:
# 	pass
# except:
#     pass
# else:
#     pass


# try:
# 	pass
# else:
#     pass

# try:
# 	pass
# finally:
#     pass

# except:
#     print('1')

# finally:
#     print('1')

# except:
#     print('1')
# else:
#     pass

# try:
#     pass
# else:
#     pass
# finally:
#     pass

# try:
#     pass

# finally:
#     pass

# try:
#     pass
# except ZeroDivisionError:
#     pass
# except ValueError:
#     pass

# try:
#     pass
# except ZeroDivisionError:
#     pass
# except ValueError:
#     pass
# else:
#     pass


# try:
#     pass
# except ZeroDivisionError:
#     pass
# except ValueError:
#     pass
# else:
#     pass
# else:
#     pass


# try:
#     pass
# except ZeroDivisionError:
#     pass
# except ValueError:
#     pass
# if:
#     pass
# else:
#     pass

# try:
#     if 6==5:
#         print(10)
#     else:
#         print(5)
# except ZeroDivisionError:
#     pass
# except ValueError:
#     pass
# else:
#     pass


# try:
#     if 6==5:
#         print(10)
#     else:
#         print(5)
# except ZeroDivisionError:
#     pass
# except ValueError:
#     pass
# finally:
#     pass
# finally:
#     pass


# try:
#     print('hello')
# print('hy')
# except ZeroDivisionError:
#     pass
# except ValueError:
#     pass
# finally:
#     pass


# try:
#     print('hello')

# except ZeroDivisionError:
#     pass
# print('hy')
# except ValueError:
#     pass
# finally:
#     pass



# try:
#     print('hello')

# except ZeroDivisionError:
#     pass
# except ValueError:
#     pass
# finally:
#     pass
# print('hy')


# try:
#     print('hello')
# except ZeroDivisionError:
#     pass
# try:
#     pass
# finally:
#     pass
# print('hy')


# try:
#     print('hello')
# except ZeroDivisionError:
#     pass
# else:
#     print('22')


# try:
#     print('hello')
# except ZeroDivisionError:
#     pass
# if 5==5:
#     print('99')
# else:
#     print('22')


# try:
#     print('hello')
# except ZeroDivisionError:
#     pass
# if 5==5:
#     print('99')
# else:
#     print('22')
# finally:
#     pass


