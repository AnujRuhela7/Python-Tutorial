n = int(input("Enter the number of rows : "))
A = 65
for i in range(1,n+1):
    for j in range(i):
        char = chr(A)
        print(char,end=' ')
        A = A + 1
    print()