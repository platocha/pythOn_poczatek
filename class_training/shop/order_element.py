class OrderElement:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product}\t\t x {self.quantity}\n"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        else:
            return (self.product == other.product and
                    self.quantity == other.quantity)