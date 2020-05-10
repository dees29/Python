day = int(input("enter day:"))
month = int(input("enter month:"))
year = int(input("enter year:"))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    max_days=31
elif month==4 or month==6 or month==9 or month==1:
    max_days=31

elif year%4==0 and year%100==0 or year%4==0:
    max_days=29
else:
    max_days=28

if month<1 or month>12:
    print("entered date is invalid")
    print("check the range of the month")
elif day<1 or day>max_days:
    print("entered date is invalid")
    print("check the range of the day")
else:
    print("Entered date is valid")
    
