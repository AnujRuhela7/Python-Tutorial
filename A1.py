a = 0
b = 1
n = int(input("Enter Number : "))
c = a + b
if((n==a) or (n==b)):
    print("Fibonacci")
    exit()
while(c < n):
    a = b
    b = c
    c = a + b
if(c==n):
    print("Fibonacci")
else:
    print("Not Fibonacci")