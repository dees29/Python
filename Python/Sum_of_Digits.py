num=int(input("Enter a positive digit: "))
result=0
while num>0:
    temp=num%10
    result=result+temp
    num=num//10
print(result)
