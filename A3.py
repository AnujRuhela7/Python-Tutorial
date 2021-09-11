L1 = eval(input("Enter List Items : "))
a = int(input("Enter List Item : "))
count = 0
for i in range(len(L1)):
    if(a==L1[i]):
        count = count + 1
print("Frequency of ",a," : ",count)    
