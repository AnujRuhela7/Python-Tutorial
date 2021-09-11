s = input()
L = []
for i in range(len(s)):
    L.append(s[i])
i = 0
if(L[i]==L[i+1]):
    print('false')
else:
    print('true')