num=int(input("Enter the number of rows: "))
for rows in range(num):
    for cols in range(num):
        if rows==0 or cols==(num-1) or rows==cols:
            print("*",end="")
        else:
            print(" ",end="")
    print()
        
