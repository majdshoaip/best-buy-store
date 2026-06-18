import products

class Store:
    def __init__(self, products_list):
        self.products = products_list

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):

        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        total_price = 0.0
        for item in shopping_list:
            product, quantity = item
            total_price += product.buy(quantity)
        return total_price