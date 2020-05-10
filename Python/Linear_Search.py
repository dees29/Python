def search(list1,Key):
    list2=[]
    flag=False
    for i in range(0,len(list1)):
        if Key==list1[i]:
            flag=True
            list2.append(i)

    if flag==True:
        print("Key is found at index:")
        for i in list2:
            print(i)
    else:
        print("Key not found")

list1=[4,6,2,7,2,1,9,1,4,1]
print(list1)
Key=int(input("Enter the key value:"))
search(list1,Key)
