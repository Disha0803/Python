import os
# result=os.getcwd()
# print(result)
#------------------create a sub dir. in our current working dir.--------------------------
# os.mkdir('new dir')
#------------------create a sub dir. in our current working dir.-------------------------- 
# os.mkdir('new dir/latestone')
#------------------create multiple dirs. at a tym-----------------------------------------
# os.makedirs('aaa/bbb/ccc/ddd')
#---------------------------------------remove dir----------------------------------------
# os.rmdir('new dir/latestone')
#--------------------------------remove multiple dirs-------------------------------------
# os.removedirs('aaa/bbb/ccc/ddd')

# os.makedirs('aaa/bbb/ccc/ddd')
# os.rmdir('ccc') #FileNotFoundError: [WinError 2] The system cannot find the file specified: 'ccc'
# os.rmdir('aaa') #OSError: [WinError 145] The directory is not empty: 'aaa'
#---------------------------rename--------------------------------------------------------
# os.rename('new dir','hello')
#-----------------------------------------------------------------------------------------
# os.rmdir('hello')
# os.removedirs('aaa/bbb/ccc/ddd')
#-----------------------------to know the content of dir----------------------------------
# print(os.listdir("."))
#-----------------------------to get max info abt a file----------------------------------
data=os.stat('D:PYTHON/python(part-2)')
print(data)