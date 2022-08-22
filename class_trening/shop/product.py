class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def print_self(self):
        print(f"Nazwa: {self.name} | Kategoria: {self.category} | Cena: {self.price}/szt")