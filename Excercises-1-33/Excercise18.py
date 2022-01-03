import math

radius = float(input("Enter the radius of the Cylinder: "))
height = float(input("Enter the height of the Cylinder: "))

baseArea = math.pi * math.pow(radius, 2)
volume = baseArea * height

print("The volume of the Cylinder is: {} cubic cm".format(round(volume, 1)))