for item in range(5):
    original = 5 * item + 4.95
    discounted = original * 0.6
    final_price = original - discounted

    print("Original: ${} | Discounted: ${} | Final Price: ${}".format(round(original, 2), round(discounted, 2), round(final_price, 2)))