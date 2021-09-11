A = eval(input("Enter Array : "))
A = sorted(A)
flag = 0
length = len(A)
for i in range(len(A)) :
    if(A[i]>0):
        flag = 0
    else:
        flag = 1
if(flag == 1):
    print(1)
    exit()
elif(flag == 0):
    if (A[length - 1] == (A[length - 2] + 1)):
        print(A[length-1]+1)
    elif((A[length-2] < A[length-1]) and (A[length - 1] != (A[length - 2] + 1)) ):
        print(A[length-2]+1)

# [1,3,6,4,1,2]
# [1,2,3]
# [-1,-3]