L = eval(input("Enter List : "))
print("List Sorted by Price : ")
print(sorted(L, key = lambda i : i['Price']))
print("\r")
print("List Sorted by Price & Dish : ")
print(sorted(L, key=lambda i : (i['Price'], i['Dish'])))
print("\r")
print("List sorted by Price in Descending Order : ")
print(sorted(L, key=lambda i : i['Price'],reverse=True))