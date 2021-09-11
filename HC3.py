TL = int(input())
ML = int(input())
a = TL
for i in range(TL):
    for k in range(a-i-1):
        print(' ',end='')
    print('*',end='')
    for j in range(2*(i-1)+1):
        if (i != ML - 1) :
            print(" ",end='')
        else:
            print("*",end='')
            
    if(i>0):
        print('*')
    else:
        print()