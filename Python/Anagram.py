str1=input("string1:")
str2=input("string2:")
sorted_str1=sorted(str1)
sorted_str2=sorted(str2)

if len(str1)==len(str2):
    if sorted(str1)==sorted(str2):
        print("given strings are anagram")
    else:
        print("Not an anagram")
else:
    print("Not an anagram")
