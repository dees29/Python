num=int(input("Enter the number of row:"))
for row in range(num):
    for col in range(row + 1):
        x=0
        for k in range(col):
            x=x+num-k
        if col%2==0:
            print(x+row+1-col, end=" ")
        else:
            print(x+num-row,end=" ")
    print()
