a = int(input("Enter 1st number = "))
b = int(input("Enter 2nd number = "))
while b!=0 :
    a,b = b,a%b
print("GCD = ",a)

'''
Euclidean Algorith

a=10
b=25       GCD = 5

a,b = 25,10
a,b = 10,5
a,b = 5,0
'''

