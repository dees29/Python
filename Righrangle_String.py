string=input("Enter the String: ")
row=len(string)
for i in range(row):
    for j in range(i+1):
        print(string[j],end="")
    print()
