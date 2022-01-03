#Ideal Gas Law
#Ask for user input on pressure,volume and temperature first

pressure = float(input("Enter the pressure in Pascals: "))
volume = float(input("Enter the volume in Liters: "))
temperature = float(input("Enter the temperature in Celsius: "))

celsiusToKelvin = temperature + float(273.15)
pascalToAtm = pressure/float(101325)
gasConstant = float(.082)

number_of_moles = (pascalToAtm * volume) / (gasConstant * celsiusToKelvin)

print("The number of moles is : {} mol ".format(number_of_moles))

