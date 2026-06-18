from product import Product
from store import Store


def main():

    best_buy = Store()
    best_buy.add_product(Product("MacBook Air M2", 1450, 100))
    best_buy.add_product(Product("Bose QuietComfort Earbuds", 250, 500))
    best_buy.add_product(Product("Google Pixel 7", 500, 250))

    while True:
        print("\nStore Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            best_buy.list_products()
        elif choice == "2":
            total = best_buy.get_total_quantity()
            print(f"Total of {total} items in store")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()