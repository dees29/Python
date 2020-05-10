sentence=input("Enter the integer: ")
string=sentence.lower()
list=["a","e","i","o","u"]
count=0
for char in sentence:
    if char in list:
        count+=1
print("count: ",count)
