num = int(input("Enter the row: "))
count=1
for row in range(1, num+1):
    for col in range(1, row + 1):
        print(count, end=" ")
        count = count + 1
    print()
