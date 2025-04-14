def inventory_management_system():
    """
    This function simulates a simple inventory management system for a store.
    The inventory is stored in a dictionary named 'Inventory'.
    The user can add, remove, view, and update items in the inventory.
    The program exits once a chosen function is done.
    """
    Inventory = {}

    while True:
        print("\nPlease choose an option:")
        print("1. Add item to inventory")
        print("2. Remove item from inventory")
        print("3. View inventory")
        print("4. Update item in inventory")
        print("5. Exit program")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            Inventory[name] = {'quantity': quantity, 'price': price}
            print(f"{name} added to inventory.")

        elif choice == '2':
            print("How would you like to remove an item?")
            print("1. By name")
            print("2. By quantity")
            remove_choice = input("Enter your choice (1-2): ")

            if remove_choice == '1':
                name = input("Enter item name: ")
                if name in Inventory:
                    del Inventory[name]
                    print(f"{name} removed from inventory.")
                else:
                    print(f"{name} not found in inventory.")

            elif remove_choice == '2':
                name = input("Enter item name: ")
                if name in Inventory:
                    quantity = int(input("Enter quantity to remove: "))
                    if quantity <= Inventory[name]['quantity']:
                        Inventory[name]['quantity'] -= quantity
                        print(f"{quantity} {name} removed from inventory.")
                    else:
                        print(f"Not enough {name} in inventory.")
                else:
                    print(f"{name} not found in inventory.")

        elif choice == '3':
            if Inventory:
                print("\nInventory:")
                print("{:<15} {:<15} {:<15}".format('Item', 'Quantity', 'Price'))
                for item, details in Inventory.items():
                    print("{:<15} {:<15} {:<15}".format(item, details['quantity'], details['price']))
            else:
                print("Inventory is empty.")

        elif choice == '4':
            name = input("Enter item name: ")
            if name in Inventory:
                quantity = int(input("Enter new quantity: "))
                price = float(input("Enter new price: "))
                Inventory[name]['quantity'] = quantity
                Inventory[name]['price'] = price
                print(f"{name} updated in inventory.")
            else:
                print(f"{name} not found in inventory.")

        elif choice == '5':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")
