num=int(input("Enter the number of row:"))
for row in range(1,num+1):
    for col in range(1,num-row+1):
        print(end=" ")
    for col in range(row,0,-1):
        print(col,end="")
    for col in range(2,row+1):
        print(col,end="")
    print()
