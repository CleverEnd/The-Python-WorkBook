discounted_loaves = float(input("Enter the quantity of day old loaves you will buy: "))

normal_price = float(3.49)
discount = float(0.6)
regular_price = normal_price * discounted_loaves
discount_price = normal_price * discount
total = (normal_price*discount) * discounted_loaves
discount_total = regular_price - total


print("The normal price of a loaf is: $%.2f" % normal_price)
print("The normal price of the product is: $%.2f" % regular_price)
print("Your discount is : $%.2f" % discount_total)
print("The total price is: $%.2f" % total)
