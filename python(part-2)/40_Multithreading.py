# import threading
# print('Disha') #Disha
# print(threading.current_thread().getName()) #MainThread
#---------------------------------------------------------------
#1...Creating a thread without using any class
# from threading import*
# def printDAta():
#     for i in range(1,5):
#         print("Thread-1")
# printDAta()
# for i in range(1,5):
#     print("Main Thread")
#----------------------------------
# from threading import*
# def printData():
#     for i in range(1,5):
#         print("Thread-1")
# t=Thread(target=printData)
# t.start()
# for i in range(1,5):
#     print("Main-Thread")
#------------------------------------------------------------------------------
#2...Creating a thread by extending thread class
# from threading import*
# class MyThread(Thread):
#     def run(self):
#         for i in range(5):
#             print("Thread-1")
# t=MyThread()
# t.start()
# for i in range(5):
#     print("Main Thread")
#------------------------------------------------------------------------------
#3...Creating a thread w/o extending thread class
# from threading import*
# class Test:
#     def printData(self):
#         for i in range(5):
#             print("Thread-1")
# obj=Test()
# t=Thread(target=obj.printData)
# t.start()
# for i in range(5):
#     print("Main Thread")
#------------------------------------------------------------------------------
#Code-4(w/o using multithreading)
# from threading import*
# import time
# def db(nums):
#     for i in nums:
#         time.sleep(2)
#         print(2*i)
# def sq(nums):
#     for i in nums:
#         time.sleep(2)
#         print(i*i)
# list=[10,20,30,40,50]
# x=time.time()
# db(list)
# sq(list)
# print("Total time= ",time.time()-x)
#------------------------------------------------------------------------------
#Code-5(using multithreading)
from threading import*
import time
def db(nums):
    for i in nums:
        time.sleep(2)
        print(2*i)
def sq(nums):
    for i in nums:
        time.sleep(2)
        print(i*i)
list=[10,20,30,40,50]
x=time.time()
t1=Thread(target=db,args=(list,))
t2=Thread(target=sq,args=(list,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Total time= ",time.time()-x)