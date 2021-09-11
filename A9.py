import string
s = input("Enter a string : ")
special = string.punctuation
for c in s:
    if c in special:
        print("String is Not Accepted")
        exit()
    else:
        pass
print("String is Accepted")
