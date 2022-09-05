from dataclasses import dataclass
from enum import Enum


class ProductCategory(Enum):
    FOOD="Jedzenie"
    OTHER="Inne"
    TOOLS="Narzedzia"

@dataclass
class Product:
    name: str
    category: ProductCategory
    price: float
    identifier: int

    def __str__(self):
        return(f"ID: {self.identifier} | Nazwa: {self.name} | Kategoria: {self.category.value} | Cena: {self.price}/szt")

@dataclass
class ProductExpiration(Product):
    production_year: int
    expiration_years: int

    def does_expire(self, current_year):
        return current_year > self.production_year + self.expiration_years