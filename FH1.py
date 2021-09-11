fp = open("Prime.txt","w")
for num in range(1,100):
   if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            fp.write(num)
fp.close()
fp = open("Prime.txt","r")
p_num = fp.read()
print(p_num)
fp.close()