n = int(input("Enter the number of lines you want to print : "))
a = 1
for i in range(1,n+1) :
    for j in range(n,0,-1) :
        print(a+i,end=' ')
    print()

