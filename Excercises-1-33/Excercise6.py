mealCost = float(input("Enter the cost of the meal: "))
tax = float(.16)
taxCost = mealCost*tax
tip = float(.18)
tipCost = mealCost*tip
totalPrice = mealCost+taxCost+tipCost
print("The tax for the meal is: $%.2f " % taxCost)
print("The tip for the meal is: $%.2f " % tipCost)
print("The total price is: $%.2f " % totalPrice)
