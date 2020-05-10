num = int(input("Enter the num:"))
msg=input("Enter the msg:")
l=len(msg)
n = num // 2
for row in range(n):
    for col in range(n - row - 1):
        print(" ", end="")
    for col in range(row + 1):
        print("* ", end="")
    if num % 2 == 0:
        for col in range(2 * (n - row - 1)):
            print(" ", end="")
    else:
        for col in range(2 * (n - row - 1)+1):
            print(" ", end="")
    for col in range(row + 1):
        print("* ", end="")

    print()
if num%2==0:
    if l%2==0:
        print("* "*((num-l)//2)," ".join(msg)," *"*(((num-l)//2)-1))
    else:
        print("* "*((num-l)//2)," ".join(msg)," *"*((num-l)//2))
else:
    if l%2==0:
        print("* "*((num-l)//2)," ".join(msg)," *"*((num-l)//2))
    else:
        print("* "*((num-l)//2)," ".join(msg)," *"*(((num-l)//2)-1))


for row in range(num, 0, -1):
    for col in range(num - row):
        print(" ", end="")
    for colj in range(row):
        print("* ", end="")
    print()
