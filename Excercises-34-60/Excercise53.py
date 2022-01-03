

value = float(input("Enter the Rating Value: "))


if value == 0.0:
    print("Your had an unacceptable performance! ")
    print("Your raise is: ", 2400 * value)
elif value == 0.4:
    print("Your had an acceptable performance! ")
    print("Your raise is: ", 2400 * value)
elif value >= 0.6 :
    print("Your had a meritorious performance! ")
    print("Your raise is: ", 2400 * value)
else:
    print("Your input is invalid!")