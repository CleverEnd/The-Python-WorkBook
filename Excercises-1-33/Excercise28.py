import math

ws = float(input("Enter the wind speed: "))
temp = float(input("Enter the temperature: "))

wCI = float(13.12) + (float(0.6215)*temp) + float(-11.37*math.pow(ws, 0.16) + float(0.3965*(temp*math.pow(ws, 0.16))))

print("The Wind Chill Index is : ", wCI)
