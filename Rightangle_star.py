num= int(input("Enter the number of rows : "))
k=0
for i in range(0,num+1):
    for j in range(0,i+1):
        print("*",end="")
        k=k+2
    print()
        
