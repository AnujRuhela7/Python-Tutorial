print("Enter Your Choice")
choice = input("Join OR Split (J/S): ")

if choice == 'S' or choice == 's':
    str2 = input("Enter String : ").split()
    print(str2)
elif choice == 'J' or choice == 'j':
    str1 = eval(input("Enter String in form of list : "))
    s = '-'
    a = s.join(str1)
    print(str(a))