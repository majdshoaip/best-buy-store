class Store:
    """Manages a collection of products."""
    def __init__(self, products_list):
        self.products = products_list

    def add_product(self, product):
        """Adds a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Removes a product from the store."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        """Returns the total number of items in the store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        """Returns a list of all active products."""
        return [product for product in self.products if product.is_active()]

    @staticmethod
    def order(shopping_list):
        """Processes an order of multiple products."""
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price