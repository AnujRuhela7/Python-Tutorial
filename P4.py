n = int(input("Enter the number of lines you want to print :"))
for i in range(1,n) :
    for j in range(n-i) :
        print('  ',end='')
    for k in range(2*i-1) :
        print("* ",end='')
    print()
    
for a in range(n,0,-1) :
    for b in range(n-a) :
        print('  ',end='')
    for c in range(2*a-1) :
        print("* ",end='')        
    print()

'''
            * 
          * * * 
        * * * * *         
      * * * * * * *       
    * * * * * * * * *     
  * * * * * * * * * * *   
* * * * * * * * * * * * * 
  * * * * * * * * * * *   
    * * * * * * * * *     
      * * * * * * *       
        * * * * *         
          * * * 
            * 
'''