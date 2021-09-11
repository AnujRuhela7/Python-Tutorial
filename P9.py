n = int(input("Enter the number of lines you want to print : "))
for i in range(1,n+1) :
    for j in range(i) :
        print(2**(i-j-1),end=" ")
    print()

'''

1
2 1
4 2 1
8 4 2 1
16 8 4 2 1
32 16 8 4 2 1
64 32 16 8 4 2 1
128 64 32 16 8 4 2 1

'''