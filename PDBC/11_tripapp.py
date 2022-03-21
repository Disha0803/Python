from 10_Trip import *
while True:
    print("Pls enter any choice")
    print("Press 1 for: Insertion")
    print("Press 2 for: Updation")
    print("Press 3 for: Deletion")
    print("Press 4 for: Display")
    print("Press 5 for: Exit")
    choice=int(input("Enter your choice[1 | 2 | 3 | 4 | 5]"))
    if choice==1:
        redgno=input("Enter your id")
        name=input("Enter your name")
        sourceloc=input("Enter your source location")
        destloc=input("Enter you destination")
        obj.insert_data(redgno,name,sourceloc,destloc)