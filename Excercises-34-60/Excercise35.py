age = float(input("Enter the dog's age: "))

if age <= 0:
    print("The age value is incorrect please enter a number bigger than 0 :)")

elif age <= 2:
    print("The equivalent in human years is: ", age*10.5)


else:
    print("The equivalent in human years is: ", ((age-2)*4)+21)
