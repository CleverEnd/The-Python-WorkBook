import math

height = float(input("Enter the height in meters: "))

acceleration = float(9.8)

initialSpeed = math.sqrt(0 + 2*(acceleration*height))

print("The object is traveling at: {} m/s".format(initialSpeed))
