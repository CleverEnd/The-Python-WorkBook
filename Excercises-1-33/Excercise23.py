import math


s = float(input("Enter the leght of a side of the polygon: "))
n = float(input("Enter the number of sides of the polygon: "))

area = (n * math.pow(s, 2)) / (4 * math.tan(math.pi/n))

print("The area of the polygon is: {} square cm".format(area))


