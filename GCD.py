def ComputeGCD(a,b):
    if b==0:
        return a
    else:
        return ComputeGCD(b,a%b)

num1=int(input("Enter the first number"))
num2=int(input("Enter the first number"))
print(ComputeGCD(num1,num2))
