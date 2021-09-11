L = list(map(int,input().split()))
L1 = []
for i in range(len(L)):
    L1.append(~L[i])
s = sum(L1)
if s%10==0:
    print('YES')
else:
    print('NO')