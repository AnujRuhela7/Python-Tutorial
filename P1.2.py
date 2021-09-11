L = eval(input("Enter list items : "))
print(L)
length = len(L)
Product = 1
print("Length = ",length)
for i in range(length):
    Product = Product * L[i]
print("Product = ",Product)