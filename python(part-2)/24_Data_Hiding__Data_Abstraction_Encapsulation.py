class Account:
    __accBal=1000
    def m1(self,sCode):
        if sCode==0000:
            print(Account.__accBal)
        else:
            print("You are not a valid person")
t=Account()
t.m1(0000)