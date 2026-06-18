class Product:
    """Represents a product in the store."""
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def __str__(self):
        """Returns a string representation of the product."""
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def get_quantity(self):
        """Returns the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """Sets the quantity and deactivates if zero."""
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """Returns True if the product is active."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def buy(self, quantity):
        """Processes the purchase of a product."""
        if quantity > self.quantity:
            raise ValueError("Not enough items in stock")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return float(self.price * quantity)