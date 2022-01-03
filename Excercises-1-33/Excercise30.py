pressure = float(input("Enter a pressure in KiloPascals: "))

pounds_per_square_inch = pressure*float(0.145038)
mmHg = pressure*float(7.50062)
atm = pressure*float(0.00986923)

print("The conversion of the pressure in pounds per square inch is: {} psi".format(pounds_per_square_inch))
print("The conversion of the pressure in milliliters of mercury is: {} mmHg".format(mmHg) )
print("The conversion of the pressure in atmospheres is: {} atm ".format(atm))

