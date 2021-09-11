n = int(input("Enter the number of lines you want to print : "))
for i in range(1,n+1) :
    for j in range(n-i) :
        print('  ',end="")
    for k in range(i) :
        print(i,end=" ")
    print()

'''

            1 
          2 2 
        3 3 3 
      4 4 4 4 
    5 5 5 5 5 
  6 6 6 6 6 6 
7 7 7 7 7 7 7

'''