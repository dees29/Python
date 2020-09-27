list1 = [5,48,6,87,0,2]
print("Input:",list1)
for i in range(len(list1)):
    max_val = max(list1[i:])
    max_ind=list1.index(max_val)
    list1[i],list1[max_ind] = list1[max_ind],list1[i]
print("Output:",list1)
