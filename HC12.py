len = int(input())
string = input()
s = []
for i in string:
    s.append(i)
    
Q = int(input())
l = []

for i in range(Q):
    a = int(input())
    l.append(a)
    
for i in range(Q):
    test = s[l[i]-1]
    count = 0
    n = l[i]
    for i in range(n):
        if(test == s[i]):
            count += 1
    print(count-1)
