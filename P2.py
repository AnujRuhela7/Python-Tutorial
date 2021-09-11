n = int(input("Enter the number of lines you want to print : "))
for i in range(n) :
    for k in range(n-i) :
        print('  ',end='')
    for j in range(i) :
        print('* ',end='')
    print('')
'''
                  *
                * *
              * * *
            * * * *
          * * * * *
        * * * * * *
      * * * * * * *
    * * * * * * * *
'''