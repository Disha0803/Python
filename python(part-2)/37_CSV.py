# import csv
# with open('StudentDetails.csv','w') as s:
#     w=csv.writer(s)
#     w.writerow(['SID','SNAME','SROLL','SADDR'])
#     while True:
#         sid=int(input('Enter student id'))
#         sname=input("Enter student name")
#         sroll=int(input('Enter student roll no'))
#         saddr=input("Enter student address")
#         w.writerow([sid,sname,sroll,saddr])
#         print("1 row inserted successfully")
#         choice=input("Do you want to enter more rows?? [y|n]")
#         if choice=='n':
#             break
# print("Thank you")

import csv
f=open("StudentDetails.csv",'r')
r=csv.reader(f)
print(r)
x=list(r)
# print(x) #nested list
for line in x:
    for word in line:
        print(word,'\t\t',end='')
    print()