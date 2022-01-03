from fractions import Fraction

temp = float(input("Enter a temperature value in Celsius: "))

farenheit = (temp * Fraction(9, 5) + 32)
kelvin = temp + 273.15

print("Conversion from Celsius to Farenheit: ", farenheit)
print("Conversion from Celsius to Kelvin: ", kelvin)
