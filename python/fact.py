def fact(num):
    if num==0:
        result=1
    else:
        result=num*fact(num-1)
    return result
a=fact(int(input('Enter a number ')))
print(a)