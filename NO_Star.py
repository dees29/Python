num=int(input("Enter the number of rows: "))
str1="NO"
print_N=[[" " for i in range(num)] for j in range(num)]
print_O=[[" " for j in range(num)] for j in range(num)]

for rows in range(num):
    for cols in range(num):
        if cols==0 or cols==num-1 or rows==cols:
            print_N[rows][cols]="*"
                    
for rows in range(num):
    for cols in range(num):
        if (cols==0 or cols==num-1) and (rows!=0 and rows!=num-1) or (rows==0 or rows==num-1) and (cols!=0 and cols!=num-1):
            print_O[rows][cols]="*"

for i in range(num):
    for j in range(num):
        print(print_N[i][j],end=" ")
    print(end=" ")
    for j in range(num):
        print(print_O[i][j],end=" ")
    print()
