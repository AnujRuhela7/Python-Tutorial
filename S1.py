s1 = set()
for i in range(2,22,2) :
    s1.add(i)
print(s1)

s2 = set()
for j in range(1,21,2) :
    s2.add(j)
print(s2)
print("--------------------------------------------------------")
print("Union : ",s1|s2)                     #Union
print('--------------------------------------------------------')
print("s1 - s2 : ",s1-s2)                   #Difference
print('--------------------------------------------------------')
print("s2 - s1 : ",s2-s1)                   #Difference
print('--------------------------------------------------------')
print("Intersection : ",s1&s2)              #Intersection
print('--------------------------------------------------------')
print("Symmetric Difference : ",s1^s2)      #Symmetric Difference