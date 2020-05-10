from math import gcd
num1=int(input("Enter the first number"))
lower=int(input("Enter the lower limit"))
upper=int(input("Enter the first number"))
for i in range(lower,upper+1):
    if gcd(num1,i)==1:
        print(i)

