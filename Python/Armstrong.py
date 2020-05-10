num=int(input("Enter the number:"))
result=0
n=len(str(num))
i=num
while(i!=0):
    digit=i%10
    result=result+digit**n
    i=i//10
if num==result:
    print("Number is an amstrong number")
else:
    print("Number is an amstrong number")
        
