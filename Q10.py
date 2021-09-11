a1 = int(input("Enter 1st side of triangle (a1) = "))
a2 = int(input("Enter 2nd side of triangle (a2) = "))
a3 = int(input("Enter 3rd side of triangle (a3) = "))
flag = 0
if (a1 + a2 > a3) or (a2 + a3 > a1) or (a1 + a3 > a2) :
    print("Triangle is Valid!!!")
    flag = 1 
else :
    print("Traingle isn't valid!!!")
    flag = 0
s = (a1+a2+a3)/2
Area = (s*(s-a1)*(s-a2)*(s-a3))**0.5
if flag == 1 :
    print("Area of Triangle = ",int(Area))

