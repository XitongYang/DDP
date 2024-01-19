inventory={}
def add_item(item,quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

def view_inventory():
    for item,quantity in inventory.items():
        print(f"{item}:{quantity}")


def update_item(item, quantity):
    if item in inventory:
        inventory[item] = quantity
        print(f"updated {item} quantity to {quantity}")
    else:
        print(f"{item} not found in inventory.")

def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice= input("Enter choice (1/2/3/4): ")

        if choice == "1":
            item = input("enter item:")
            try:
                quantity = int(input("enter quantity:"))
            except:
                print("Error detected:please use number")
            add_item(item,quantity)
        elif choice == "2":
            view_inventory()
        elif choice == '3':
            item = input("Enter item name: ")
            quantity = int(input("Enter new quantity: "))
            update_item(item, quantity)
        elif choice == "4":
            print("Exiting Inventory Management System.")
            break
        else:
            print("Invalid chouce. Please choose again.")

manage_inventory()


