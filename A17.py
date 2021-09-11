A = eval(input("Enter List or Tuple : "))
if( type(A) == list ):
    print("Original List : ",A)
    B = eval(input("Enter Tuple : "))
    A.append(B)
    print("List + Tuple = ",A)
elif( type(A) == tuple ):
    print("Original Tuple : ",A)
    B = eval(input("Enter List : "))
    A += (B,)
    print("List + Tuple = ",A)

