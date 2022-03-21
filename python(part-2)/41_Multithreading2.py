from threading import*
# def t1():
#     for i in range(11):
#         print("rahul")
# def t1():
#     for i in range(11):
#         print("rahul")
# def t1():
#     for i in range(11):
#         print("rahul")


print(current_thread().isDaemon()) #False
current_thread().setDaemon(True) #RuntimeError: cannot set daemon status of active thread
print(current_thread().isDaemon())