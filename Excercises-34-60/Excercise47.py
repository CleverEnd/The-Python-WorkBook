month = input("Enter your month of birth: ").lower()
day = int(input("Enter your day of birth: "))

capricorn = False
aquarius = False
pisces = False
aries = False
taurus = False
gemini = False
cancer = False
leo = False
virgo = False
libra = False
scorpio = False
sagittarius = False

if month == "december" or month == "january":
    if month == "december" and day in range(22, 31):
        capricorn = True
    elif month == "january" and day in range(1, 19):
        capricorn = True
if month == "january" or month == "february":
    if month == "january" and day in range(20, 31):
        aquarius = True
    elif month == "february" and day in range(1, 18):
        aquarius = True
if month == "february" or month == "march":
    if month == "february" and day in range(19, 29):
        pisces = True
    elif month == "march" and day in range(1, 20):
        pisces = True
if month == "march" or month == "april":
    if month == "march" and day in range(21, 31):
        aries = True
    elif month == "april" and day in range(1, 19):
        aries = True
if month == "april" or month == "may":
    if month == "april" and day in range(20, 31):
        taurus = True
    elif month == "may" and day in range(1, 20):
        taurus = True
if month == "may" or month == "june":
    if month == "may" and day in range(21, 31):
        gemini = True
    elif month == "june" and day in range(1, 20):
        gemini = True
if month == "june" or month == "july":
    if month == "june" and day in range(21, 31):
        cancer = True
    elif month == "july" and day in range(1, 22):
        cancer = True
if month == "july" or month == "august":
    if month == "july" and day in range(23, 31):
        leo = True
    elif month == "august" and day in range(1, 22):
        leo = True
if month == "august" or month == "september":
    if month == "august" and day in range(23, 31):
        virgo = True
    elif month == "september" and day in range(1, 22):
        virgo = True
if month == "september" or month == "october":
    if month == "september" and day in range(23, 31):
        libra = True
    elif month == "october" and day in range(1, 22):
        libra = True
if month == "october" or month == "november":
    if month == "october" and day in range(23, 31):
        scorpio = True
    elif month == "november" and day in range(1, 22):
        scorpio = True
if month == "november" or month == "december":
    if month == "november" and day in range(22, 31):
        sagittarius = True
    elif month == "december" and day in range(1, 21):
        sagittarius = True

if capricorn:
    print("Your zodiac sign is Capricorn!")
elif aquarius:
    print("Your zodiac sign is Aquarius!")
elif pisces:
    print("Your zodiac sign is Pisces!")
elif aries:
    print("Your zodiac sign is Aries!")
elif taurus:
    print("Your zodiac sign is Taurus!")
elif gemini:
    print("Your zodiac sign is Gemini!")
elif cancer:
    print("Your zodiac sign is Cancer!")
elif leo:
    print("Your zodiac sign is Leo!")
elif virgo:
    print("Your zodiac sign is Virgo!")
elif libra:
    print("Your zodiac sign is libra!")
elif scorpio:
    print("Your zodiac sign is Scorpio!")
elif sagittarius:
    print("Your zodiac sign is Sagittarius!")
else:
    print("Your input is invalid! :(")