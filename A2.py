L1 = eval(input("Enter List Items : "))
l = len(L1)
L1[0],L1[l-1] = L1[l-1],L1[0]
print(L1)