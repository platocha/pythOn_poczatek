from dataclasses import dataclass

@dataclass
class OrderElement:
    product: str
    quantity: int

    def calculate_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product}\t\t x {self.quantity}\n"
