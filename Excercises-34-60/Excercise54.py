wavelength = float(input("Enter the wavelength: "))

if wavelength >= 380 and wavelength < 450:
    print("The color of that wavelength is Violet!")
elif wavelength >= 450 and wavelength < 495:
    print("The color of that wavelength is Blue!")
elif wavelength >= 495 and wavelength < 570:
    print("The color of that wavelength is Green!")
elif wavelength >= 570 and wavelength < 590:
    print("The color of that wavelength is Yellow!")
elif wavelength >= 590 and wavelength < 620:
    print("The color of that wavelength is Orange!")
elif wavelength >= 620 and wavelength < 750:
    print("The color of that wavelength is Red!")
else:
    print("Your input is invalid! ")