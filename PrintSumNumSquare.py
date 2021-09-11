sum = 0
n = int(input("Enter how many number you want to print : "))
for n in range(n):
    sum += (n+1)**2
    print((n+1)**2,sep='+',end=' ')
print("\nSum = ",sum)
