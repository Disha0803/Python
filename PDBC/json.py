import json
student={'name':'rahul','age':23,'addr':'bbsr','isEnggStd':True,'howmanyhouseinbbsr':None}
# print(type(student))
jsondata=json.dumps(student)
print(jsondata)
print(type(jsondata))