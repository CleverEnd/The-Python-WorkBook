letter = input("Enter the letter grade: ").upper()

if letter == "A+" or letter == "A":
    print("The grade point equivalent is 4.0")
elif letter == "A-":
    print("The grade point equivalent is 3.7")
elif letter == "B+":
    print("The grade point equivalent is 3.3")
elif letter == "B":
    print("The grade point equivalent is 3.0")
elif letter == "B-":
    print("The grade point equivalent is 2.7")
elif letter == "C+":
    print("The grade point equivalent is 2.3")
elif letter == "C":
    print("The grade point equivalent is 2.0")
elif letter == "C-":
    print("The grade point equivalent is 1.7")
elif letter == "D+":
    print("The grade point equivalent is 1.3")
elif letter == "F":
    print("The grade point equivalent is 1.0")
elif letter == "F":
    print("The grade point equivalent is 0")
else:
    print("Your input is invalid!")