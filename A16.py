tup = eval(input("Enter Tuple : "))
print("The original tuple is : ",tup)
k = int(input("k = "))
A = []
tup = list(tup)
temp = sorted(tup)
for i,val in enumerate(temp):
    if i<k or i>=len(temp) - k:
        A.append(val)
A = tuple(A)
print("Output : ",A)