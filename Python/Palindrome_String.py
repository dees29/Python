N=input("Enter a String: ")
string=N.lower()
result=string[::-1]
if (string==result):
    print("Entered string is palindrome")
else:
    print("Entered string is not a palindrome")
