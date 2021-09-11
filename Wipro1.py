def minStep(str) -> int:
      # WRITE YOUR BRILLIANT CODE HERE
      charA = 'A'
      numB = 0
      minDel = 0
      for i in range(0, len(str)):
          if (charA == str[i]):
              minDel = min(numB, minDel + 1)
          else:
              numB = numB + 1
      return minDel

string = input("Enter your string : ")
print(minStep(string))