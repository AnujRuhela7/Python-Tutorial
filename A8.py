import string
s = input("Enter a string : ")
lc = {'a','e','i','o','u'}
s = s.lower()
s1 = set()
for c in s:
    if c in lc:
        s1.add(c)
    else:
        pass
if(len(s1)==len(lc)):
    print("Accepted")
else:
    print("Not Accepted")