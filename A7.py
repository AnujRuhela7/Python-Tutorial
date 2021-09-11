S = input("Enter String : ").split()
#print(list(S))
for i in range(len(S)):
    if(len(S[i])%2==0):
        print(S[i])
