# f=open('my.txt','w')
# f.write('disha\n')
# f.write('bhai\n')
# f.write('hi')

# f=open('my.txt','r')
# f.write('disha\n') #io.UnsupportedOperation: not writable
# f.write('bhai\n')
# f.write('hi')

# f=open('my.txt','w')
# list=['10','20','disha','bhai']
# f=open('me.txt','a')
# f.write('bhai\n')
# f.write('hi')

# f=open('me.txt','r+')
# f.write('bhai\n')
# f.write('hi')

# f=open('me.txt','w+')
# f.write('bhai\n')
# f.write('hi')


# f=open('me.txt','a+')
# f.write('bhai\n')
# f.write('hi')


# f=open('me.txt','x') #FileExistsError: [Errno 17] File exists: 'me.txt'
# f.write('bhai\n')
# f.write('hi') 

# f=open('me.txt','a')
# print("File name is",f.name)
# print("File mode is",f.mode)
# print("File is readable",f.readable())
# print("File is writable",f.writable())
# print("File is closed",f.closed)
# f.close()
# print("File is closed",f.closed)

# f=open('demo.txt','r')
# # data=f.read()
# # print(data)
# # data=f.readline()
# # print(data)
# data=f.readlines()
# print(data)
#------------------------------with open-----------------------------------------
# with open('python.txt','w') as f:
#     f.write("Hello I am new text")
#     print("I am closed or not",f.closed)
# print("I am closed or not",f.closed)
#-----------------------------seek() and tell()----------------------------------
# f=open('python.txt','r')
# print(f.tell())
# print(f.read(5))
# print(f.tell())
# f.seek(3)
# print(f.tell())
#--------------------------------file exists or not-----------------------------
# import os,sys
# fname=input("Enter file name that you want to know if it existed or not:")
# if os.path.isfile(fname):
#     print('Yes existed')
# else:
#     print("Not existed")
#     sys.exit(0)
#---------------------------------handling binary data--------------------------
# f=open('bg7.jpg','rb')
# data=f.read()
# f1=open('bg8.jpg','rb+')
# f1.write(data)
# f2=open('bg9.jpg','ab+')
# f2.write(data)
#--------------------------------------------------------------------------------
o=open('bg 6.jpg','rb')
o1=open(r'D:\Python_Pratical\NUMPY\suraj.jpg','wb')
data=o.read()
o1.write(data)
#================================================================================
#---------------------------------number of lines--------------------------------
# import os,sys
# fname=input("Enter file name")
# nooflines=0
# if os.path.isfile(fname):
#     f=open(fname,'r')
#     for line in f:
#         # print(line)
#         nooflines=nooflines+1
#     print(nooflines)
# else:
#     print("Not Existed")
#     sys.exit(0)
#---------------------------------number of words--------------------------------
# import os,sys
# fname=input("Enter file name")
# noofwords=0
# if os.path.isfile(fname):
#     f=open(fname,'r')
#     for line in f:
#         words=line.split()
#         print(words)
#         noofwords=noofwords+len(words)
#     print(noofwords)
# else:
#     print("Not Existed")
#     sys.exit(0)
#---------------------------------number of characters--------------------------------
# import os,sys
# fname=input("Enter file name")
# noofchar=0
# if os.path.isfile(fname):
#     f=open(fname,'r')
#     for line in f:
#         noofchar=noofchar+len(line)
#     print(noofchar)
# else:
#     print("Not Existed")
#     sys.exit(0)