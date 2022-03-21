from threading import*
import time

def printdata_1():
    for i in range(10):
        print("rahul",i)

t1=Thread(target=printdata_1)
t1.start()
t1.join()

def printdata_2():
    for i in range(10):
        print("jini",i)
t2=Thread(target=printdata_2)
t2.start()

def printdata_3():
    time.sleep(6)
    for i in range(3):
        print("priyanka",i)

t3=Thread(target=printdata_3)
t3.start()

time.sleep(10)
for i in range(3):
        print("suraj",i)


