list1 = [5,5,87,2,48,6,87,0,2]
print("Input:",list1)
for i in range(len(list1)):
    max_ind = i
    for j in range(i+1,len(list1)):
        if list1[j]>list1[max_ind]:
            max_ind=j
    
    if list1[i]!= list1[max_ind]:
        list1[i],list1[max_ind] = list1[max_ind],list1[i]
print("Output:",list1)
