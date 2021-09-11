# To check wether a string is pangram or not
import string
str1 = input("Enter String : ")
s1 = map(set,str1.split())
c1 = string.ascii_letters
