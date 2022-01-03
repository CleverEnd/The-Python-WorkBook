month = input("Enter a month: ")
day = int(input("Enter a day: "))

if month == "January" and day == 1:
    print("It's New year's day!")
elif month == "July" and day == 1:
    print("It's Canada day!")
elif month == "December" and day == 25:
    print("It's Christmas day!")
else:
    print("The entered month and day do not correspond to a fixed-date holiday")