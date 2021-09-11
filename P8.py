n = int(input("Enter the number of lines you want to print : "))
for i in range(1,n+1) :
    for j in range(i) :
        print(i-j,end=" ")
    print()

'''

1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1 
6 5 4 3 2 1 
7 6 5 4 3 2 1

'''