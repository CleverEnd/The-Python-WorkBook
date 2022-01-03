dc1 = float(.10)
dc2 = float(.25)

autoref1 = int(input("Enter how many bottles have less that 1 litre: "))
autoref2 = int(input("Enter how many bottles have more that 1 litre: "))

refund = dc1*autoref1 + dc2*autoref2

print("Your refund is $%.2f" % refund)