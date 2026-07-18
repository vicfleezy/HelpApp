def print_menu():
    print("Taco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos")
    print("4. Soft Drink")
    print("5. Quit")

def get_price(selection):
    if selection == 1:
        return 4.00
    elif selection == 2:
        return 3.25
    elif selection == 3:
        return 2.50
    elif selection == 4:
        return 3.45
    return 0.0


print("Welcome to Taco Palace! Please view the menu below and make a selection")
print()

ordered_items = []
total_price = 0.0

while True:
    print_menu()

    try:
        selection = int(input("Enter choice (1-5):\n"))
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        continue

    if selection == 5:
        break
    elif selection == 1:
        item_name = "Taco"
    elif selection == 2:
        item_name = "Burrito"
    elif selection == 3:
        item_name = "Nachos"
    elif selection == 4:
        item_name = "Soft Drink"
    else:
        print("Invalid selection. Please try again.\n")
        continue

    if item_name == "Soft Drink":
        print("You selected a Drink")
    else:
        print(f"You selected a {item_name}")
    print()

    price = get_price(selection)
    total_price += price
    ordered_items.append(item_name)

print()
if ordered_items:
    if len(ordered_items) == 1:
        items_string = ordered_items[0]
    else:
        items_string = ", ".join(ordered_items[:-1]) + " and " + ordered_items[-1]

    items_string = items_string.replace("Soft Drink", "Drink")

    print(f"You ordered a {items_string}. Your total is ${total_price:.2f}")
else:
    print("You didn't order anything. Your total is $0.00")