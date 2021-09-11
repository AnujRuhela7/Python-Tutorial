L = eval(input("Enter list elements : "))
print(L)
M=[]
N=[]
a = 5
x = len(L) - a
y = len(L) 
for i in range(5):
    M.append(L[i]**2)
for j in range(x,y):
    N.append(L[j]**2)
A = M + N 
print("New List : ",A)

