import math
from fractions import Fraction

radius = float(input("Enter the radius of the circle: "))
volume = float(input("Enter the radius of the sphere: "))

areaCircle = math.pi * math.pow(radius, 2)
volumeSphere = Fraction(4, 3) * math.pi * math.pow(volume, 3)

print("The area of the circle is: {} square cm ".format(areaCircle))
print("The volume of the sphere is: {} cube cm ".format(volumeSphere))
