def shell_sort(list1):
    gap=len(list1)//2
    while gap>0:
        for index in range(gap,len(list1)):
            current_element=list1[index]
            pos=index
            while pos>=gap and current_element<list1[pos-gap]:
                list1[pos]=list1[pos-gap]
                pos=pos-gap
            list1[pos]=current_element
        gap=gap//2
        
    
num=int(input("Enter the number of elements you want in list1:"))
list1=[int(input()) for x in range(num)]
shell_sort(list1)
print("sorted list is",list1)
