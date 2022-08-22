class Potato:
    def __init__(self, species, size, price):
        self.species = species
        self.size = size
        self.price = price

    def calculate_total_price(self, quantity):
        return self.price * quantity

    def __repr__(self):
        return f"Gatunek: {self.species} | Rozmiar: {self.size} | Cena: {self.price}"