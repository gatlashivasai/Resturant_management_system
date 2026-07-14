from data import menu

def display_menu():
    print("\n----- MENU -----")
    for item, price in menu.items():
        print(f"{item} : ₹{price}")