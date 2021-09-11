#Various Operations on Dictionary
d1 = {'Name':'Anuj','Age':18,'Gender':'Male','Contact No.':8449440111}
d2 = dict()
print(type(d1))
print(type(d2))
print(dict(d1.items))
print(d1.values())
print(d1.keys())
d1.pop('Age')
print(d1)