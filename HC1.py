A = list(map(int,input().split()))
A1 = []
for i in range(len(A)):
    a = A[i]
    for j in range(len(A)):
        if(a==A[j]):
            pass
        else:
            b = a&A[j]
            A1.append(b)
print(max(A1))