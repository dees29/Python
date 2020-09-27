year= int(input("Enter the year: "))
def function(month, year):
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        max_days=31
    elif month==4 or month==6 or month==9 or month==11:
        max_days=30
    elif year%4 == 0 and year%100 != 0 or year%400 == 0:
        max_days=29
    else:
        max_days=28
    return max_days

for month in range(1, 13):
    max_day = function(month, year)
    for day in range(1, max_day+1):
        dd=str(day)
        mm=str(month)
        yyyy=str(year)
        if month<10:
            mm = "0"+mm
        if day<10:
            dd = "0"+dd
        
        given_date=         dd + mm + yyyy
        reverse_date=given_date[::-1]
        if given_date == reverse_date:
            print(day,"/",month,"/",year)
        else:
            print("No palindrome")
            break
    
