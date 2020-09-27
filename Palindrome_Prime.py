num=int(input("Enter the integer: "))
result=int(str(num)[::-1])
print("result: ",result)
if (num==result):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                print("Entered number is a palindrimic but not a prime number")
                break
        else:
            print("Entered number is a palindrimic prime number")
else:
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                print("Entered number is not a palindrimic and not a prime number")
                break
        else:
            print("Entered number is not a palindrimic but is a prime number")
