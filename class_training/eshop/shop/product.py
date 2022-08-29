class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return(f"Nazwa: {self.name} | Kategoria: {self.category} | Cena: {self.price}/szt")

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        else:
            return (self.name == other.name and \
                    self.category == other.category and
                    self.price == other.price)

class ProductExpiration(Product):

    def __init__(self, name, category, price, production_year, expiration_years):
        super().__init__(name, category, price)
        self.production_year = production_year
        self.expiration_years = expiration_years

    def does_expire(self, current_year):
        return current_year > self.production_year + self.expiration_years