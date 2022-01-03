foot = float(12)
inch = float(2.54)

footValue = float(input("Enter your height in foot: "))
inchValue = float(input("Enter your height in inches: "))


inchToCm = inch * inchValue
footToCm = (footValue * foot) * inch

heightInCm = inchToCm + footToCm

print("Your height in cm is: {} cm".format(heightInCm))