def apply_discount(total):
    coupon = input("Enter Coupon Code (or press Enter to skip): ")

    if coupon == "SAVE10":
        total = total - (total * 0.10)
        print("10% Discount Applied!")
    elif coupon == "SAVE20":
        total = total - (total * 0.20)
        print("20% Discount Applied!")
    else:
        print("No Discount Applied")

    return total