string = input("Enter String : ")
d = int(input("d = "))
print("Left Rotation : ",string[d:]+string[:d])
print("Right Rotation : ",string[-d:]+string[:-d])