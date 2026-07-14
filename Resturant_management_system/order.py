from data import menu

def place_order():
    total = 0

    while True:
        item = input("Enter item name: ")

        if item in menu:
            qty = int(input("Enter quantity: "))
            total += menu[item] * qty
        else:
            print("Item not found")

        ch = input("Add more items (yes/no): ")

        if ch.lower() != "yes":
            break

    return total