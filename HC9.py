string = input()
string = string.replace(' ','')
pos = int(input()) - 1
N = int(input())
res =  N*(string[pos:]+string[:pos])
for i in res:
    if i != ' ':
        print(i,end=' ')
