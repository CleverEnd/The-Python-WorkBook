month = input("Enter a month: ")

if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or \
        month == "October" or month == "December":
    print(month, "has 31 days")
elif month == "April" or month == "June" or month == "September" or month == "November":
    print(month, "has 30 days")
elif month == "February":
    print(month, "has 28 or 29 days")
else:
    print("You typed and incorrect value!")
