def binary(list1,Key):
    low=0
    high=len(list1)-1
    mid=(low+high)//2
    found=False
    while low<=high and not found:
        if Key==list1[mid]:
            found=True
        elif Key>list1[mid]:
            low=mid+1
        else:
            high=mid-1
    if found==True:
        print("Key is found")
    else:
        print("Key is not found")
    
    
list1=[4,6,2,7,2,1,9,1,4,1]
list1.sort()
print(list1)
Key=int(input("Enter the key value:"))
binary(list1,Key)
