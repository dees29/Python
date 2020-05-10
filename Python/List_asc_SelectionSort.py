list1 = [5,48,6,87,0,2]
print("Input:",list1)
for i in range(len(list1)):
    min_val = min(list1[i:])
    min_ind=list1.index(min_val)
    list1[i],list1[min_ind] = list1[min_ind],list1[i]
print("Output:",list1)
