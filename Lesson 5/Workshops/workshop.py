print("Enter a month:")
month = int(input())

if month > 0 and month < 13:
    print("Enter a day:")
    day = int(input())
    if month == 12:
        if day > 0 and day <= 31:
            season = "Winter"
            month = "December"
            print(f"{season} {month} {day}")
        else:
            print("Please enter a valid day")
    elif month == 1:
        if day > 0 and day <= 31:
            season = "Winter"
            month = "January"
            print(f"{season} {month} {day}")
        else:
            print("Please enter a valid day")
    elif month == 2:
        if day > 0 and day <= 28:
            season = "Winter"
            month = "February"
            print(f"{season} {month} {day}")
        else:
            print("Please enter a valid day")
    elif month == 3:
        if day > 0 and day <= 31:
            season = "Spring"
            month = "March"
            print(f"{season} {month} {day}")
        else:
            print("Please enter a valid day")
    elif month == 4:
        if day > 0 and day <= 30:
            season = "Spring"
            month = "April"
            print(f"{season} {month} {day}")
        else:
            print("Please enter a valid day")
    elif month == 5:
        if day > 0 and day <= 31:
            season = "Spring"
            month = "May"
            print(f"{season} {month} {day}")
        else:
            print("Please enter a valid day")
    elif month == 6:
        if day > 0 and day <= 30:
            season = "Summer"
            month = "June"
            print(f"{season} {month} {day}")
        else:
            print("Please enter a valid day")
    elif month == 7:
        if day > 0 and day <= 31:
            season = "Summer"
            month = "July"
            print(f"{season} {month} {day}")
        else:
            print("Please enter a valid day")
    elif month == 8:
        if day > 0 and day <= 31:
            season = "Summer"
            month = "August"
            print(f"{season} {month} {day}")
        else:
            print("Please enter a valid day")
    elif month == 9:
        if day > 0 and day <= 30:
            season = "Autumn"
            month = "September"
            print(f"{season} {month} {day}")
        else:
            print("Please enter a valid day")
    elif month == 10:
        if day > 0 and day <= 31:
            season = "Autumn"
            month = "October"
            print(f"{season} {month} {day}")
        else:
            print("Please enter a valid day")
    elif month == 11:
        if day > 0 and day <= 30:
            season = "Autumn"
            month = "November"
            print(f"{season} {month} {day}")
        else:
            print("Please enter a valid day")
else:
    print("Please enter a valid month")


# Implementaion a bit long but code is working :)
