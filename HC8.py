N,M = map(int,input().split('x'))
count = 0
for i in range(1,N+1):
    for j in range(1,M+1):
        if((i+j)%2!=0):
            count += 1
        else: 
            pass
print(count)
    