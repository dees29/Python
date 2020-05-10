num = int(input("Enter the number of rows : "))
for i in range(0,(num//2)+1):
    for j in range(1,num-i+1):
        print(end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range((num//2)+1,num+1):
    for j in range(i):
        print(end=" ")
    for j in range(1,num-i+1):
        print("*",end=" ")
    print()

        
