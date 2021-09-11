L1 = eval(input("Enter 1st list elements : "))
L2 = eval(input("Enter 2nd list elements : "))
print(L1)
print(L2)
L = []
for i in range(len(L1)):
    L.append(L1[i]-L2[i])
print("New List : ",L)