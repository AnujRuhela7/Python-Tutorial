print("Gender of Employee (M/F) : ")
gender = input()
print("Salary of the Employee :")
salary = int(input())
if(gender=='M' or gender =='m'):
    salary += 0.05*salary
    print("Salary with Bonus = ",salary)
elif(gender=='F' or gender=='f'):
    salary += 0.1*salary
    print("Salary with Bonus = ",salary)
elif(gender=='M' or gender =='m' and salary<10000):
    salary += 0.07*salary
    print("Salary with Bonus = ",salary)
elif(gender=='F' or gender=='f' and salary<10000):
    salary += 0.12*salary
    print("Salary with Bonus = ",salary)
