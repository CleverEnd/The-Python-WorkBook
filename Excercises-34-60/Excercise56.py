minutes = int(input("Enter the number of minutes used: "))
text = int(input("Enter the number of messages used: "))

call_center = float(0.44)
tax = float(.05)
base_charge = int(15)
if minutes > 50:
    additional_minutes = (minutes - 50) * 0.25
    total_tax = base_charge * tax
    total = total_tax + base_charge + additional_minutes
    print("The base charge is: $%.2f " % base_charge, "Additional minutes charge: $%.2f " % additional_minutes)
    print("The 911 fee is: $%.2f " % call_center, "The tax is: $%.2f" % total_tax, "The total is: $%.2f " % total)

elif text > 50:
    additional_text = (text - 50) * 0.44
    total_tax = base_charge * tax
    total = total_tax + base_charge + additional_text
    print("The base charge is: $%.2f " % base_charge, "Additional messages charge: $%.2f " % additional_text)
    print("The 911 fee is: $%.2f " % call_center, "The tax is: $%.2f" % total_tax, "The total is: $%.2f " % total)

elif text > 50 and minutes > 50:
    additional_minutes = (minutes - 50) * 0.25
    additional_text =(text - 50) * 0.44
    total_tax = base_charge * tax
    total = total_tax + base_charge + additional_text + additional_minutes
    print("The base charge is: $%.2f " % base_charge, "Additional messages charge: $%.2f " % additional_text,
          "Additional minutes charge: $%.2f " % additional_minutes)
    print("The 911 fee is: $%.2f " % call_center, "The tax is: $%.2f" % total_tax, "The total is: $%.2f " % total)

else:
    total_tax = base_charge * tax
    total = total_tax + base_charge
    total = total_tax + base_charge
    print("The base charge is: $%.2f " % base_charge, "The 911 fee is: $%.2f " % call_center,
          "The tax is: $%.2f " % total_tax, "The total is: $%.2f " % total)
