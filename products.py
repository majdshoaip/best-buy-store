class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def buy(self, quantity):
        if quantity > self.quantity:
            raise ValueError("Not enough items in stock")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return float(self.price * quantity)

    def __str__(self):
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"