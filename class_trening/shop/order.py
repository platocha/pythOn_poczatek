import random

from product import Product, print_product

class Order:
    def __init__(self, first_name, last_name, product_list=None):
        self.first_name = first_name
        self.last_name = last_name
        if product_list is None:
            product_list = []
        self.product_list = product_list
        total_price = 0
        for product in product_list:
            total_price += product.price
        self.total_price = total_price

def print_order(order):
    print("="*20)
    print(f"Zamowienie zlozone przez: {order.first_name} {order.last_name}")
    print(f"O lacznej wartosci: {order.total_price} PLN")
    print(f"Zamowione produkty:")
    for product in order.product_list:
        print("\t", end="")
        print_product(product)
    print("="*20)
    print()

def generate_order():
    number_of_products = random.randint(1,10)
    products = []
    for product_number in range(number_of_products):
        product_name = f"Product-{product_number}"
        category_name = "Inne"
        unit_price = random.randint(1,30)
        product = Product(product_name, category_name, unit_price)
        products.append(product)

    order = Order(first_name="Pawel", last_name="Latocha", product_list=products)
    return order