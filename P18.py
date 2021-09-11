n = int(input("Enter number of rows : "))
a = 0
for i in range(n):
    for j in range(i+1):
        print(a,end=' ')
        a = 2**(i+1)
    print()