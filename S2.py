#Prime Number Program
S1 = set()
for num in range(1,10) :
    if num > 1 :
        for i in range(2,num) :
            if (num % i) == 0 :
                break
        else :
            S1.add(num)
print(sorted(S1))

print("----------------------------------------------------")
print("----------------------------------------------------")
'''
#Armstrong Number
S2 = set()
for num in range(100,1000) :
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
       S2.add(num)
print(sorted(S2))'''