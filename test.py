'''from itertools import product
a = list(map(int,input("Enter 1st List : ").split()))
b = list(map(int,input("Enter 2nd List : ").split()))
print(list(product(a,b)))

x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n ])'''
'''
n = int(input())
arr = list(map(int,input().split()))
sets = set(arr)
arr1 = sorted(list(sets))
print(arr1)
print(arr1[-2])'''
'''
l, u, p, d = 0, 0, 0, 0
s = input("ENter Password : ")
if (len(s) >= 8):
	for i in s:

		# counting lowercase alphabets
		if (i.islower()):
			l+=1			

		# counting uppercase alphabets
		if (i.isupper()):
			u+=1			

		# counting digits
		if (i.isdigit()):
			d+=1			

		# counting the mentioned special characters
		if(i=='@'or i=='$' or i=='_'):
			p+=1		
if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
	print("Valid Password")
else:
	print("Invalid Password")
'''
#row = int(input("Enter the number of rows : "))
#column = int(input("Enter the number of column : "))
n = int(input("Enter size of matrix : "))
arr = [[int(input())   for j in range(n)]   for i in range(n)]

for i in range(n):
	for j in range(n):
		print(arr[i][j], end=' ')
	print()
'''
def diagonalDifference(arr):
    # Write your code here
    d1s = 0
    d2s = 0
    for i in range(n):
        for j in range(n):
            if i==j :
                d1s += arr[i][j]
            if (i-j == n-1) or (j-i == n-1) :
                d2s += arr[i][j]
    return abs(d1s-d2s)'''