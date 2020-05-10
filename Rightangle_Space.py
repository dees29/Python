num=int(input("Enter the number of rows: "))
for rows in range(num):
    for cols in range(num):
        if rows==(num-1) or cols==0 or rows==cols:
            print("*",end="")
        else:
            print(" ",end="")
    print()
        
