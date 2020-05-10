num= int(input("Enter the number of rows : "))
for i in range(0,num):
    for j in range(1,num-i+1):
        print("*",end=" ")
    for j in range(i):
        print(end=" ")
    print()
        
