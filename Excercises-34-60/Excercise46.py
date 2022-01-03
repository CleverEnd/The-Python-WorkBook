month = input("Please enter the name of a month: ").lower()
day = int(input("Please enter a day from that month: "))

spring = False
summer = False
fall = False
winter = False

if month == "march" or month == "april" or month == "may" or month == "june":
    if month == "march" and day >= 20:
        spring = True
    elif month == "april" or month == "may":
        spring = True
    elif month == "june" and day <= 21:
        spring = True

if month == "june" or month == "july" or month == "august" or month == "september":
    if month == "june" and day >= 21:
        summer = True
    elif month == "july" or month == "august":
        summer = True
    elif month == "september" and day <= 22:
        summer = True
if month == "september" or month == "october" or month == "november" or month == "december":
    if month == "september" and day >= 22:
        fall = True
    elif month == "october" or month == "november":
        fall = True
    elif month == "december" and day <= 21:
        fall = True
if month == "december" or month == "january" or month == "february" or month == "march":
    if month == "december" and day >= 21:
        winter = True
    elif month == "january" or month == "february":
        winter = True
    elif month == "march" and day <= 20:
        winter = True

if spring:
    print("This date is on Spring season!")
elif summer:
    print("This date is on Summer season!")
elif fall:
    print("This date is on Fall season!")
elif winter:
    print("This date is on Winter season!")