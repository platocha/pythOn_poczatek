import random

from order_element import OrderElement
from product import Product

class Order:
    def __init__(self, first_name, last_name, order_elements=None):
        self.first_name = first_name
        self.last_name = last_name
        if order_elements is None:
            order_elements = []
        self.order_elements = order_elements
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        total_price = 0
        for element in self.order_elements:
            total_price += element.calculate_price()
        return total_price

    def __str__(self):
        return_string = "="*20+"\n"
        return_string += f"Zamowienie zlozone przez: {self.first_name} {self.last_name}\n"
        return_string += f"O lacznej wartosci: {self.total_price} PLN\n"
        return_string += f"Zamowione produkty:\n"
        for element in self.order_elements:
            return_string += f"\t{element}"
        return_string += "\n" + "=" * 20 + "\n"
        return return_string

    def __len__(self):
        return len(self.order_elements)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        else:
            for element in self.order_elements:
                if element not in other.order_elements:
                    return False
            return (self.first_name == other.firstname and
                    self.last_name == other.last_name and
                    len(self.order_elements) == len(other.order_elements))

def generate_order():
    number_of_products = random.randint(1,10)
    order_elements = []
    for product_number in range(number_of_products):
        product_name = f"Product-{product_number}"
        category_name = "Inne"
        unit_price = random.randint(1,30)
        product = Product(product_name, category_name, unit_price)
        quantity = random.randint(1,10)
        order_elements.append(OrderElement(product, quantity))

    order = Order(first_name="Pawel", last_name="Latocha", order_elements=order_elements)
    return order