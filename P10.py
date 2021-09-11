n = int(input("Enter the number of lines you want to print :"))
for i in range(n+1) :
    for j in range(i) :
        print(2**j,end=' ')
    for k in range(i+1) :
        print(2**(i-k),end=' ')
    print()        

'''

1 
1 2 1
1 2 4 2 1
1 2 4 8 4 2 1
1 2 4 8 16 8 4 2 1
1 2 4 8 16 32 16 8 4 2 1 
1 2 4 8 16 32 64 32 16 8 4 2 1
1 2 4 8 16 32 64 128 64 32 16 8 4 2 1

'''