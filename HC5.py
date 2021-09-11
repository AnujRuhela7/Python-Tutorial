s = input("Enter String : ")
a = ''
L = []
if( len(s) % 2 != 0 ):
    print("Odd length.")
else:
    for i in range(len(s)):
        L.append(s[i])
    for i in range(0,len(s),2):
        L[i],L[i+1] = L[i+1],L[i]
    a = a.join(L)
    print(a)
