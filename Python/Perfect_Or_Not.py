num=int(input("Enter the number:"))
result=0
for i in range(1,num):
    if num%i==0:
        result=result+i
if result==num:
    print("The number is perfect")
else:
    print("The number is not perfect")
