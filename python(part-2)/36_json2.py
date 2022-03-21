import json

#json string to python dict (deserlization)
# loads()

# myjsonstring="""
# {
#     "name": "rahul",
#     "age": 23,
#     "addr": "bbsr",
#     "Your a/c balance is zero": false,
#     "howmany cars in rahul's home": null
# }
# """
# # print(type(myjsonstring))

# sdata=json.loads(myjsonstring)

# print(type(sda))


# json to python dict (deserlization)
# load()

with open('std.json','r') as f:
    sdata=json.load(f)

# print(type(sdata))
# print(sdata)

for key,value in sdata.items():
    print(key," ",value)