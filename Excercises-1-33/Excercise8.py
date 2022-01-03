widget_weight = int(75)
gizmo_weight = int(112)

widget_amount = int(input("Enter the number of widgets you are buying: "))
gizmo_amount = int(input("Enter the number of gizmos you are buying: "))

order_weight = widget_weight*widget_amount + gizmo_weight*gizmo_amount

print("The weight of the order is: {} grams ".format(order_weight))