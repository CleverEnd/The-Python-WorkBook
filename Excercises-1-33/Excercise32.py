
int1 = int(input("Please type the first integer: "))
int2 = int(input("Please type the second integer: "))
int3 = int(input("Please type the third integer: "))

min1 = min(int1, int2, int3)
max1 = max(int1, int2, int3)
middle = int1 + int2 + int3 - min1 - max1

print("The smallest integer is: {} ".format(min1))
print("The middle integers is: {} ".format(middle))
print("The largest integer is: {} ".format(max1))