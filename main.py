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
            for i, product in enumerate(products_list, 1):
                print(f"{i}. {product}")

        elif choice == "2":
            print(f"Total of {best_buy.get_total_quantity()} items in store")

        elif choice == "3":

            products_list = best_buy.get_all_products()
            for i, product in enumerate(products_list, 1):
                print(f"{i}. {product}")

            print("------")

            product_index = int(input("Which product # do you want? ")) - 1
            quantity = int(input("What amount do you want? "))

            selected_product = products_list[product_index]
            order_list = [(selected_product, quantity)]

            total_price = best_buy.order(order_list)
            print(f"Product(s) added to list! Order cost: {total_price} dollars.")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


def main():
    # setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = store.Store(product_list)


    start(best_buy)


if __name__ == "__main__":
    main()