'''n = int(input())
for i in range(n+1) :
        for k in range(n-i) :
            print(' ',end='')
        for j in range(i) :
            print('#',end='')
        print()'''
'''
candles = eval(input())

def birthdayCakeCandles(candles):
    # Write your code here
    count = 0
    m = max(candles)
    for i in candles:
        if candles[i] == m:
            count += 1
    return count

birthdayCakeCandles(candles)'''
print(ord('h') - ord('z'))