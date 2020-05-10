upper=int(input("Enter the max value:"))
for num in range(1, upper):
    result=0
    for i in range(1,num):
        if (num%i==0):
            result=result+i
    if (result==num):
        print(num)
