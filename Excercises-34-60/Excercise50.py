import math

a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
c = int(input("Enter the value for c: "))

number_of_roots = (b**2) - (4*a*c)
square_root = math.sqrt(number_of_roots)
root_one = (-b + square_root) / 2*a
root_two = (-b - square_root) / 2*a

if number_of_roots == 0:
    print("The equation has only 1 root")
    print(root_one)
elif number_of_roots < 0:
    print("The equation doesnt have any real roots")
elif number_of_roots > 0:
    print("The equation has two real roots")
    print("The root using a plus sign is: ", root_one)
    print("The root using a minus sign is: ", root_two)
else:
    print("You didn't type a valid input!")