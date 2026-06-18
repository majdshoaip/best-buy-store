import products
import store


def start(best_buy):
    while True:
        print("\nStore Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            products_list = best_buy.get_all_products()
            print("------")
            for i, product in enumerate(products_list, 1):
                print(f"{i}. {product}")
            print("------")

        elif choice == "2":
            total_quantity = best_buy.get_total_quantity()
            print(f"Total of {total_quantity} items in store")

        elif choice == "3":
            products_list = best_buy.get_all_products()
            print("------")
            for i, product in enumerate(products_list, 1):
                print(f"{i}. {product}")
            print("------")

            order_list = []
            while True:
                product_input = input("Which product # do you want? (Press Enter to finish): ")
                if product_input == "":
                    break

                quantity_input = input("What amount do you want?: ")

                try:
                    product_index = int(product_input) - 1
                    quantity = int(quantity_input)

                    if 0 <= product_index < len(products_list):
                        selected_product = products_list[product_index]
                        order_list.append((selected_product, quantity))
                        print("Product added to list!")
                    else:
                        print("Error: Invalid product number.")
                except ValueError:
                    print("Error: Please enter numbers only.")

            if order_list:
                try:
                    total_price = best_buy.order(order_list)
                    print(f"********\nOrder made! Total payment: ${total_price}\n********")
                except ValueError as e:
                    print(f"Error during order: {e}")

        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":

    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]


    best_buy = store.Store(product_list)


    start(best_buy)