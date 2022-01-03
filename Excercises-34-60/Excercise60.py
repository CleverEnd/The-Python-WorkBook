import random

space = random.randint(0,37)

red = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)
black = (2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35,)

if space == 0:
    if random.randint(0, 2) == 0:
        print("Pay 00")
    else:
        print("Pay 0")
else:
    print("The spin resulted in {}...".format(space))

    print("Pay {}".format(space))

    if space in red:
        print("Pay red")
    else:
        print("Pay black")
    if space > 0:
        if space % 2 == 0:
            print("Pay even")
        else:
            print("Pay odd")
    if space >=1 and space <= 18:
        print("Pay 1 to 18")
    elif space >= 19 and space <36:
        print("Pay 19 to 36")
