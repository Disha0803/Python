# fib = {1: 1, 2: 1, 3: 2, 4: 3}
# print(fib.get(4, 0) + fib.get(7, 5))

# print("{0}{1}{0}".format("abra", "cad"))
# def fib(x):
#   if x == 0 or x == 1:
#     return 1
#   else: 
#     return fib(x-1) + fib(x-2)
# print(fib(4))

# from itertools import product
# a={1, 2}
# print(len(list(product(range(3), a))))

# nums = {1, 2, 3, 4, 5, 6}
# nums = {0, 1, 2, 3} & nums
# nums = filter(lambda x: x > 1, nums)
# print(len(list(nums)))

# def power(x, y):
#   if y == 0:
#     return 1
#   else:
#     return x * power(x, y-1)
		
# print(power(2, 3))

# import re
# match =r"(a)(b(?:c)(d)(?:e))"
# len(match.groups())

# a, b, c, d, *e, f, g = range(20)
# print(len(e))

# for i in range(10):
#    if i > 5:
#       print(i)
#       break
# else:
#    print("7")

# try:
#   print(1)
#   print(1 + "1" == 2)
#   print(2)
# except TypeError:
#   print(3)
# else:
#   print(4)


# for i in range(10):
#   try: 
#     if 10 / i == 2.0:
#       break
#   except ZeroDivisionError:
#     print(1)
#   else:
#     print(2)

from os import remove


data = [7, 5, 6.9, 1, 8, 42, 33, 128, 1024, 2, 8, 11, 0.4, 1024, 66, 809, 11, 8.9, 1.1, 3.42, 9, 100, 444, 78]
#your code goes here
# \79788725992462Sunita Mohanty2462
# [7,5,6,9,1,8,42,33,128,1024,2,8,11,0.4,1024,66,889,11,8.9,1.1,3.42,9,100,444,78]
# #your code goes here 
min=data[0]
max=data[0]
for i in data:
    if i<min:
        min=i
    if i>max:
        max=i
data.remove(min)
data.remove(max)
sum=0
for i in data:
    sum+=i
print(sum)