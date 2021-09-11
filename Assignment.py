import random
import string
Letter = string.ascii_letters                       #All Uppercase & Lowercase Letters
Digits = string.digits                              #All digits from 0 - 9
S_Symbols = '@#$'                                   #Special Symbols included in Password
Complete_List = Letter + Digits + S_Symbols

Password = ""

length = int(input("Enter length of your password : "))

if (length < 8) :
    print("Minimum length of password should be 8 characters!!!")
else :
    for i in range(length) :
        Password = Password + random.choice(Complete_List)
        
if length >=8 :
    print("Password : ",Password)