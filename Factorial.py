num=int(input("Enter the number:"))
result=1
if num==0:
    print("Factorial is 1")
else:
    for i in range(num,0,-1):
        result=result*i
    print("Factorial of a number is", result)
    
