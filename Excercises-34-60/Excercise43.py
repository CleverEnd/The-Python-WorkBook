one_dollar = "George Washington"
two_dollar = "Thomas Jefferson"
five_dollar = "Abraham Lincoln"
ten_dollar = "Alexander Hamilton"
twenty_dollar = "Andrew Jackson"
fifty_dollar = "Ulysses S. Grant"
hundred_dollar = "Benjamin Franklin"

amount = int(input("Enter a US dollar bank note denomination: "))

if amount == 1:
    print(one_dollar, "appears in the", amount, "dollar note!")
elif amount == 2:
    print(two_dollar, "appears in the", amount, "dollar note!")
elif amount == 5:
    print(five_dollar, "appears in the", amount, "dollar note!")
elif amount == 10:
    print(ten_dollar, "appears in the", amount, "dollar note!")
elif amount == 20:
    print(twenty_dollar, "appears in the", amount, "dollar note!")
elif amount == 50:
    print(fifty_dollar, "appears in the", amount, "dollar note!")
elif amount == 100:
    print(hundred_dollar, "appears in the", amount, "dollar note!")
else:
    print("The note denomination you typed doesn't exist!")

