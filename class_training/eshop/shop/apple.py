from dataclasses import dataclass


@dataclass
class Apple:
    species: str
    size: str
    price: float

    def calculate_total_price(self, quantity):
        return self.price * quantity
