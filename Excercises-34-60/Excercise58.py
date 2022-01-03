year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

thirty_one_days = (1, 3, 5, 7, 8, 10)
december = 12
thirty_days = (4, 6, 9, 11)
february = 2
leap_year = year % 400 == 0 and year % 4 == 0
no_leap_year = year % 100 == 0 or not leap_year


if month in thirty_days and day >= 1 and day <= 29:
    day += 1
    print("The next day is:", year, "-", month, "-", day)
elif month in thirty_days and day == 30:
    month += 1
    day = 1
    print("The next day is:", year, "-", month, "-", day)
elif month in thirty_one_days and day >= 1 and day <= 30:
    day += 1
    print(year, "-", month, "-", day)
elif month in thirty_one_days and day == 31:
    month +=1
    day = 1
    print("The next day is:", year, "-", month, "-", day)
elif month == december and day >=1 and day <= 30:
    day += 1
    print("The next day is:", year, "-", month, "-", day)
elif month == december and day == 31:
    year += 1
    month = 1
    day = 1
    print("The next day is:", year, "-", month, "-", day)
elif month == february and leap_year and day >=1 and day <= 28:
    day +=1
    print("The next day is:", year, "-", month, "-", day)
elif month == february and leap_year and day == 29:
    month += 1
    day =1
    print("The next day is:", year, "-", month, "-", day)
elif month == february and no_leap_year and day >=1 and day <= 27:
    day += 1
    print("The next day is:", year, "-", month, "-", day)
elif month == february and no_leap_year and day == 28:
    month +=1
    day =1
    print("The next day is:", year, "-", month, "-", day)
else:
    print("That's not a valid date!")

