import products
import store


def handle_order(best_buy, products_list):
    """Handles the product ordering process."""
    order_list = []
    while True:
        p_input = input("Which product # do you want? (Enter to finish): ")
        if p_input == "":
            break
        q_input = input("What amount?: ")
        try:
            idx = int(p_input) - 1
            qty = int(q_input)
            if 0 <= idx < len(products_list):
                order_list.append((products_list[idx], qty))
            else:
                print("Invalid product.")
        except ValueError:
            print("Please enter numbers.")

    if order_list:
        try:
            price = best_buy.order(order_list)
            print(f"Order made! Total: ${price}")
        except ValueError as error:
            print(f"Error: {error}")


def start(best_buy):
    """Starts the store user interface."""
    while True:
        print("\nStore Menu\n----------")
        print("1. List all products in store\n2. Show total amount in store")
        print("3. Make an order\n4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            products_list = best_buy.get_all_products()
            for i, product in enumerate(products_list, 1):
                print(f"{i}. {product}")
        elif choice == "2":
            print(f"Total of {best_buy.get_total_quantity()} items in store")
        elif choice == "3":
            products_list = best_buy.get_all_products()
            for i, product in enumerate(products_list, 1):
                print(f"{i}. {product}")
            handle_order(best_buy, products_list)
        elif choice == "4":
            break


if __name__ == "__main__":
    product_list = [
        products.Product("MacBook Air M2", 1450, 100),
        products.Product("Bose QuietComfort Earbuds", 250, 500),
        products.Product("Google Pixel 7", 500, 250)
    ]
    best_buy = store.Store(product_list)
    start(best_buy)