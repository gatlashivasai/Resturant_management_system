from data import menu

def add_food():
    name = input("Enter food name: ")
    price = int(input("Enter price: "))

    menu[name] = price

    print("Food item added successfully")