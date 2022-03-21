# from zipfile import*
# z=ZipFile('myZipFile.zip','w',ZIP_DEFLATED)
# z.write('demo.txt')
# z.write('python.txt')
# z.close()
# print('Successfully created zip file')

from zipfile import*
z=ZipFile('myZipFile.zip','w',ZIP_STORED)
data=z.namelist()
for x in data:
    print(x)
