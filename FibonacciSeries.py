a = 0
b = 1
sum = 0
num = int(input("Enter the value of n : "))
for num in range(0,num):
    a = b
    b = sum
    sum = a + b
    print(sum)
