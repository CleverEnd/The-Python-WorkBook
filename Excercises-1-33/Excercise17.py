import math
mass = float(input("Type the water mass in grams: "))
temperature1 = float(input("Type the initial temperature: "))
temperature2 = float(input("Type the final temperature: "))

specificHeat = float(4.186)
temperatureDelta = temperature2 - temperature1
heatEnergy = mass * specificHeat * temperatureDelta

joulesKW = heatEnergy/float(3600000)

electricityCost = float(8.9) * joulesKW

print("The energy value is : {} Joules".format(heatEnergy))
print("The electricity cost is: ${} ".format(electricityCost))



