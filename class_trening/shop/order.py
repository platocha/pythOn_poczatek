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

    def print_self(self):
        print("="*20)
        print(f"Zamowienie zlozone przez: {self.first_name} {self.last_name}")
        print(f"O lacznej wartosci: {self.total_price} PLN")
        print(f"Zamowione produkty:")
        for element in self.order_elements:
            print("\t", end="")
            element.print_self()
        print("="*20)
        print()

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