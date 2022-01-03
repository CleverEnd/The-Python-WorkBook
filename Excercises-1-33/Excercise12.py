from math import radians
import math

earthRadius = float(6371.01)

t1 = float(input("Enter latitude 1: "))
g1 = float(input("Enter longitude 1: "))
t2 = float(input("Enter latitude 2: "))
g2 = float(input("Enter longitude 2: "))

t1 = radians(t1)
g1 = radians(g1)
t2 = radians(t2)
g2 = radians(g2)

distance = earthRadius * math.acos(math.sin(t1)) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1-g2)

print("The distance between the two points is: {} km " .format(distance))

