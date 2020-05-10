def insertion_sort(list1):
    for index in range(1,len(list1)):
        current_element=list1[index]
        pos=index
        while current_element<list1[pos-1] and pos>0:
            list1[pos]=list1[pos-1]
            pos=pos-1
        list1[pos]=current_element
            
        
    
num=int(input("Enter the number of elements you want in list1:"))
list1=[int(input()) for x in range(num)]
insertion_sort(list1)
print("sorted list is",list1)
