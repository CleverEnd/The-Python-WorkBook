
name = float(input("Enter the frequency for the note you want to know: "))

if 260.63 <= name <= 262.63:
    print("The note of the frequency is: C4 ")
elif 292.66 <= name <= 294.66:
    print("The note of the frequency is: D4")
elif 328.63 <= name <= 330.63:
    print("The note of the frequency is: E4")
elif 348.23 <= name <= 350.23:
    print("The note of the frequency is: F4")
elif 391.00 <= name <= 393.00:
    print("The note of the frequency is: G4")
elif 439.0 <= name <= 441.00:
    print("The note of the frequency is: A4")
elif 492.88 <= name <= 494.88:
    print("The note of the frequency is: B4")
else:
    print("The frequency you typed is not valid")

