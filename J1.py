A = eval(input("Enter List Items : "))
B = []
C = []
s = 0
x=y=0
for i in range(len(A)):
    if A[i]==6:
        x = i
    if A[i]==7:
        y = i
if x<y:
    B = A[0:x]
    C = A[y+1:len(A)+1]
    s = sum(B) + sum(C)
    print(s)
else:
    print(sum(A))
