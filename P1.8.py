'''L = eval(input("Enter list elements : "))
print(L)
M = L
print("Copy of list = ",M)'''
L = eval(input("Enter list elements : "))
print(L)
M = []
for i in range(len(L)):
    M.insert(i,L[i])
print("Clone of list L : ",M)