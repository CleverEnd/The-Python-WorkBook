prices = []
value = ''

value = float(input("Enter the price of an item: "))    
while value !="" :
    value = float(input("Enter the price of an item: "))    
    if value >= 0 :
        value%100
        value%5
        if value >= 0:
            round(value)
            prices.append(value)
        else :
         print("Enter a valid input!")
    else :
     print("Enter a valid input!")            
    print("The cost of the items are: ", prices)
