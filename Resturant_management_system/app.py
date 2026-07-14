from menu import display_menu
from order import place_order
from billing import generate_bill
from admin import add_food
from feedback import feedback
from discount import apply_discount

while True:

    print("\n===== RESTAURANT MANAGEMENT SYSTEM =====")
    print("1. View Menu")
    print("2. Place Order")
    print("3. Add Food Item")
    print("4. Feedback")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_menu()

    elif choice == "2":
      total = place_order()
      total = apply_discount(total)
      generate_bill(total)

    elif choice == "3":
        add_food()

    elif choice == "4":
        feedback()

    elif choice == "5":
        print("Thank You! Visit Again.")
        break

    else:
        print("Invalid Choice. Please try again.")