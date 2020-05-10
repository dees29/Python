num=int(input("Enter the number of rows: "))
for rows in range(num):
    for cols in range(num):
        if  (rows+cols)==2 or  (cols-rows)==2 or (rows-cols)==2 or (rows+cols)==6:
            print("*",end="")
        else:
            print(" ",end="")
    print()
                    
