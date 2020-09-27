from math import gcd
num1=int(input("Enter the first number"))
num2=int(input("Enter the first number"))

if gcd(num1,num2)==1:
    print(num1,"and",num2, "are co prime")
else:
    print(num1,"and",num2, "are not co prime")

