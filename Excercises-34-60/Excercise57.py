year = int(input("Enter a year to know if it's a Leap Year: "))

if year % 400 == 0:
    print("The year ", year, "is a Leap Year!")
elif year % 100 == 0:
    print("The year", year, "is not a Leap Year!")
elif year % 4 == 0:
    print("The year", year, "is a Leap Year!")
else:
    print("The year", year, "is not a Leap Year!")