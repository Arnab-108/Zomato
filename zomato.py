import json

#menu
def load_menu():
    with open("menu.json", "r") as menu_file:
        menu_data = json.load(menu_file)
    return menu_data

def save_menu(menu):
    with open("menu.json" , "w") as menu_file:
        json.dump(menu, menu_file, indent=4)

#order
def load_orders():
    try:
        with open("orders.json", "r") as orders_file:
            orders_data = json.load(orders_file)
        return orders_data
    except FileNotFoundError:
        return {}

def save_orders(orders):
    with open("orders.json", "w") as orders_file:
        json.dump(orders, orders_file, indent=4)

def print_menu(menu):
    print("Menu:")
    for dish_id, dish_info in menu.items():
        print(f"{dish_id}. {dish_info['name']} - ${dish_info['price']:.2f} ({'Available' if dish_info['availability'] else 'Not Available'})")



def main():
    print("Welcome to Zomato Chronicles: The Great Food Fiasco!")

    menu = load_menu()
    orders = load_orders()
    print_menu(menu)

    while True:
        print("\nMain Menu:")
        print("1. Add Dish to Menu")
        print("2. Remove Dish from Menu")
        print("3. Update Dish Availability")
        print("4. Take New Order")
        print("5. Review Orders")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            new_dish_id = max(map(int, menu.keys())) + 1
            new_dish_name = input("Enter the name of the new dish: ")
            new_dish_price = float(input("Enter the price of the new dish: ").replace('$', ''))
            new_dish_availability = input("Is the new dish available? (yes/no): ").lower() == "yes"

            new_dish = {
                "name": new_dish_name,
                "price": new_dish_price,
                "availability": new_dish_availability
            }

            menu[new_dish_id] = new_dish
            save_menu(menu)
            print("New dish added to the menu:")
            print_menu({new_dish_id: new_dish})
        
        elif choice == "2":
            print_menu(menu)
            remove_id = input("Enter the id that you want to remove: ")

            if remove_id in menu:
                removed_dish = menu.pop(remove_id)
                save_menu(menu)
                print(f"Dish '{removed_dish['name']}' has been removed from the menu.")
            else:
                print("Dish not found in the menu!")
        
        elif choice == "3":
            print_menu(menu)  # Display the menu before updating
            dish_to_update = input("Enter the dish ID to update availability: ")

            if dish_to_update in menu:
                new_availability = input("Is the dish now available? (yes/no): ").lower() == "yes"
                menu[dish_to_update]["availability"] = new_availability
                save_menu(menu)
                print(f"Availability of '{menu[dish_to_update]['name']}' has been updated.")
            else:
                print("Dish not found in the menu.")
        
        elif choice == "4":
            print_menu(menu)
            customer_name = input("Enter customer's name: ")
            dish_ids = input("Enter the dish IDs (separated by spaces) to order: ").split()

            order_dishes = []
            invalid_dishes = []

            for dish_id in dish_ids:
                if dish_id in menu and menu[dish_id]["availability"]:
                    order_dishes.append(menu[dish_id]["name"])
                else:
                    invalid_dishes.append(dish_id)

            if invalid_dishes:
                print(f"The following dishes are invalid or not available: {', '.join(invalid_dishes)}")
            else:
                # Process the order
                order_id = len(orders) + 1  # Assigning a simple unique order ID
                order_status = "received"
                new_order = {
                    "order_id": order_id,
                    "customer_name": customer_name,
                    "ordered_dishes": order_dishes,
                    "order_status": order_status
                }
                orders[order_id] = new_order
                save_orders(orders)

                print(f"Order #{order_id} for {customer_name} has been received.")
                print(f"Ordered Dishes: {', '.join(order_dishes)}")
            total_price = sum(menu[(dish_id)]["price"] for dish_id in dish_ids if menu[dish_id]["availability"])
            print(f"Total Price: ${total_price:.2f}")
        elif choice == "5":
            print("\nReviewing Orders:")
            for order_id, order_info in orders.items():
                print("-" * 40)
                print(f"Order ID: {order_id}")
                print(f"Customer Name: {order_info['customer_name']}")
                print(f"Ordered Dishes: {', '.join(order_info['ordered_dishes'])}")
                print(f"Order Status: {order_info['order_status']}")
            print("-" * 40)
        
        elif choice == "6":
            print("Great doing business with you. Have a great day!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")


    #facing some issue with updating the order
    # print("Available Order IDs:")
    # for order_id in orders:
    #     print(order_id)

    # try:
    #     order_id_to_update = int(input("Enter the order ID to update status: "))
    #     print(f"You entered: {order_id_to_update}")
    # except ValueError:
    #     print("Invalid input. Please enter a valid order ID.")

    

                        #------***-------
    

if __name__ == "__main__":
    main()