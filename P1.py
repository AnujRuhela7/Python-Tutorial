n = int(input("Enter the number of lines you want to print : "))
for i in range(1,n+1) :
    for j in range(i) :
        print('* ',end='')
    print(' ')

'''
    *
    * *
    * * *
    * * * *
    * * * * *
    * * * * * *
    * * * * * * *    
'''
