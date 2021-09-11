def toh(source,destination,aux,n):
    
    if n>=1:
        toh(source,aux,destination,n-1)
        print("Move",source,"to",destination)
        toh(aux,destination,source,n-1)
n = int(input("n = "))
toh('A','B','C',n)