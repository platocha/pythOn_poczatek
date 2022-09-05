from dataclasses import dataclass

@dataclass
class Product:
    name: str
    category: str
    price: float
    identifier: int

    def __str__(self):
        return(f"ID: {self.identifier} | Nazwa: {self.name} | Kategoria: {self.category} | Cena: {self.price}/szt")

@dataclass
class ProductExpiration(Product):
    production_year: int
    expiration_years: int

    def does_expire(self, current_year):
        return current_year > self.production_year + self.expiration_years