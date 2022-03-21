class typeofkey(Exception):
    def __init__(self,x):
        self.msg=x
dict={2:"one",3:"two",4:"three"}
d=input("Enter elements in a dictionary:- ")
for key ,value in dict:
    if type(key)!=int:
        raise typeofkey("Key must be of int type")
    