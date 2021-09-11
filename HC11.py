P1 = input()
P2 = input()
D1 = input()
D2 = input()

if D1=='Rock' and D2=='Paper':
    print(D2," Win")
elif D1=='Rock' and D2=='Scissors':
    print(D1," Win")
elif D1=='Paper' and D2=='Scissors':
    print(D2," Win")
elif D1=='Paper' and D2=='Rock':
    print(D1," Win")
elif D1=='Scissors' and D2=='Paper':
    print(D1," Win")
elif D1=='Scissors' and D2=='Rock':
    print(D2," Win")
elif D2=='Rock' and D1=='Paper':
    print(D1," Win")
elif D2=='Rock' and D1=='Scissors':
    print(D2," Win")
elif D2=='Paper' and D1=='Scissors':
    print(D1," Win")
elif D2=='Paper' and D1=='Rock':
    print(D2," Win")
elif D2=='Scissors' and D1=='Paper':
    print(D2," Win")
elif D2=='Scissors' and D1=='Rock':
    print(D1," Win")

