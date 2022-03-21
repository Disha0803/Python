from random import*
alpha1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha2="abcdefghijklmnopqr"
# name=print(choice(alpha1),choice(alpha2),choice(alpha2),choice(alpha2),choice(alpha2),choice(alpha2),sep="")
name=choice(alpha1)+choice(alpha2)+choice(alpha2)+choice(alpha2)+choice(alpha2)
print(name)

student_id="SOA-20410410"
for i in range(2):
    student_id=student_id+str(randint(0,9))
print(student_id)                               

student_email="@gmail.com"
print(name+student_email)

student_mob="+91"
for i in range(0,1):
    student_mob=student_mob+str(randint(6,9))
for i in range(1,10):
    student_mob=student_mob+str(randint(0,9))
print(student_mob)