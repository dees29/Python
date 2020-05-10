list1 = [5,48,6,87,0,2]
print("Input:",list1)
for j in range(len(list1)-1):
    for i in range(len(list1)-1-j):
        if list1[i]<list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]
            print(list1)
        else:
            print(list1)
    print()                 
print("Output:",list1)

