interestPercent = float(.04)

moneyDe = float(input("Enter the amount of money you will deposit: "))

oneYear = (moneyDe * interestPercent) + moneyDe
twoYears = (oneYear * interestPercent) + oneYear
threeYears = (twoYears * interestPercent) + twoYears

print("One year savings : $%.2f " % oneYear)
print("Two year savings : $%.2f " % twoYears)
print("Three year savings : $%.2f " % threeYears)