d = int(input("Enter the number of days: "))
h = int(input("Enter the number of hours: "))
m = int(input("Enter the number of minutes: "))
s = int(input("Enter the number of seconds: "))

sM = m * int(60)
sH = h * int(3600)
sD = d * int(86400)

print("The total number of seconds are: ", sM + sH + sD + s, "seconds")