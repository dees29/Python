num=int(input("Enter the number of rows: "))
for rows in range(1,5):
    for cols in range(1,8):
        if rows==(num-1) or (rows+cols)==5 or  (cols-rows)==3:
            print("*",end="")
        else:
            print(" ",end="")
    print()
        
