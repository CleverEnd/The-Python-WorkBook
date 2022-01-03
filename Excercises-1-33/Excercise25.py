s = int(input("Enter the number of seconds: "))

sM = s / int(60)
sH = s / int(3600)
sD = s / int(86400)

print("%d:%02d:%02d:%02d ." % (sD, sH, sM, s))