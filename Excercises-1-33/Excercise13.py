cents = int(input("Enter the number of cents: "))

pennies = cents
nickels = int(cents/5)
dimes = int(cents/10)
quarters = int(cents/25)
loonies = int(cents/100)
toonies = int(cents/200)

print("The change using the smallest amount of change is: ")
print("{} toonies,{} loonies, {} quarters, {} dimes, {} nickles, {} pennies".format(toonies,loonies,quarters,dimes,nickels,pennies))

