L1 = eval(input("Enter List Items : "))
sum = 0
for i in range(len(L1)):
    sum = sum + L1[i]
    L1[i] = sum
print(L1)