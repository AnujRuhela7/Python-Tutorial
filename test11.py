'''L1 = input().split(",")
s1 = set(L1)
print(s1)
l2 = list(s1)
for i in range(0,)'''

'''L1 = input().split(",")
Winner = ""
T1 = 0
T2 = 0
for i in L1:
    for j in L1:
        if (j == i):
                T1 = T1 + 1
    if(T1 > T2):
        Winner = i
        T2 = T1
    T1 = 0    
print(Winner)'''

N = int(input())
L = len(str(bin(N))) - 2
for i in range(N+1):
    i = str(bin(i))[2:]
    l = len(i)
    print(" "*(L-l)+i)