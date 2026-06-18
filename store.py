from product import Product

class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        for i, product in enumerate(self.products, 1):
            print(f"{i}. {product}")

    def get_total_quantity(self):
        total = 0
        for product in self.products:
            total += product.quantity
        return total