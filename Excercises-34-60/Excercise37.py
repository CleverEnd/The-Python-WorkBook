numberOfSides = int(input("Enter the number of sides: "))

if numberOfSides < 3 or numberOfSides > 10:
    print("The number of sides is not valid please enter a number between 3 and 10")
elif numberOfSides == 3:
    print("Your shape is a triangle!")
elif numberOfSides == 4:
    print("Your shape is a square!")
elif numberOfSides == 5:
    print("Your shape is a pentagon!")
elif numberOfSides == 6:
    print("Your shape is a hexagon!")
elif numberOfSides == 7:
    print("Your shape is a heptagon!")
elif numberOfSides == 8:
    print("Your shape is a octagon!")
elif numberOfSides == 9:
    print("Your shape is a eneagon!")
elif numberOfSides == 10:
    print("Your shape is a decagon!")
else:
    print("You didn't type a valid input")