row = int(input("Enter number of rows : "))
mid = int(input("Mid Line : "))
k = 0
for i in range(1,row+1):
    print(" "*(row - i), end="")
    while k!=2*i-1:
        if k==0 or k==2*i-1 or i==mid or i+k==2*i-1:
            print("*", end='')
        else:
            print(end='')
        k += 1
    k = 0
    print()

'''
bbbbb*bbbbb   00 01 02 03 04 05 06 07 08 09 010
bbbb*b*bbbb   10 11 12 13 14 15 16 17 18 19 110 
bbb*bbb*bbb   20 21 22 23 24 25 26 27 28 29 210
bb*******bb   30 31 32 33 34 35 36 37 38 39 310
b*bbbbbbb*b   40 41 42 43 44 45 46 47 48 49 410
*bbbbbbbbb*   50 51 52 53 54 55 56 57 58 59 510
'''