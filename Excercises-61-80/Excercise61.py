sum = 0
n = 0
shut = False


while not shut:
    value = int(input("Enter a value (type 0 to exit): "))
    if value != 0:
        sum += value
        n += 1
    else:
        shut = True

avg = sum / n

if shut:
    print("The average of the values you typed is: ", avg)
