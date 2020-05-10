def reverse(string):
    reversed_string=""
    for i in string:
        reversed_string=i+reversed_string
    print("Reversed_string is: ",reversed_string)
string=input("Enter the string: ")
print("Entered String", string)
reverse(string)
