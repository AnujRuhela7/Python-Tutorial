'''a = int(input("Enter 1st number = "))
b = int(input("Enter 2nd number = "))
if a == 0:
    print(b)
elif b==0:
    print(a)
else :
    while a!=b :
        if a>b :
            a = a - b
        else :
            b = b - a
    print(a)'''
import math
k = math.gcd(10,5)
print(k)