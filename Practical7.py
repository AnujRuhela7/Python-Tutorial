n = int(input("Enter a Number : "))
for i in range(1,n+1):
    print(" "*(n-i),end=' ')
    print(str(i)*i +' ',sep=' ')