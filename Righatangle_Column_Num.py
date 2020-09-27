num = int(input("Enter the row: "))
for row in range(num):
    for col in range(1, row + 1):
        print(col, end="")
    print()
