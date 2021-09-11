L1 = eval(input("Enter 1st list elements : "))
L2 = eval(input("Enter 2nd list elements : "))
print(L1)
print(L2)
length1 = len(L1)
length2 = len(L2)
for i in range(length1):
    for j in range(length2):
        if L1[i] == L2[j]:
            k=1
            break
        else:
            k=0


if k == 1 :
    print("True")
elif k == 0 : 
    print("False")  