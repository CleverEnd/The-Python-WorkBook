
fTI= float(12)
fTY = float(0.333333)
ftM = float(0.000189394)


heightFeet = float(input("Enter your height in feet: "))

feetToInches = heightFeet * fTI
feetToYards = heightFeet * fTY
feetToMiles = heightFeet * ftM

print("Your height in inches is : {} in ".format(feetToInches))
print("Your height in yards is : {} yd ".format(feetToYards))
print("Your height in miles is : {} mi ".format(feetToMiles))

