def pattern(n):
    for i in range(1,n+1):
        if(i % 2 != 0):
            k = i + 1
        else:
            k = i
        for j in range(k,n):
            if(j>=k):
                print(end=' ')
        for x in range(0,k):
            if (x == k - 1):
                print("*")
            else:
                print("*",end=' ')
n = int(input("n = "))
pattern(n)
