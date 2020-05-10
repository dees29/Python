def num(n):
    if n==1:
        return 1
    return n+num(n-1)

n=int(input("Enter the number of range"))
k = num(n)
for row in range(n):
    val=k-row
    dec=n-1
    for col in range(row+1):
        print(format(val,"<3"),end="")
        val=val-dec
        dec=dec-1
    print()
