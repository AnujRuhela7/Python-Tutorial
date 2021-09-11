L1 = eval(input("Enter List Items : "))
L2 = []
for i in range(len(L1)) :
    count = 0
    a = L1[i]
    for j in range(len(L1)) :
        if(a == L1[j]):
            count = count + 1
    if(count > 1):
        L2.append(a)
print("Duplicate Elements : ",set(L2))