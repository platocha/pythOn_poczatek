import random

from shop.discount_policy import default_policy
from shop.order_element import OrderElement
from shop.product import Product

class Order:

    MAX_ELEMENTS_NUMBER = 20
    def __init__(self, first_name, last_name, order_elements=None, discount_policy=None):
        self.first_name = first_name
        self.last_name = last_name

        if order_elements is None:
            order_elements = []

        if len(order_elements) > Order.MAX_ELEMENTS_NUMBER:
            order_elements = order_elements[:Order.MAX_ELEMENTS_NUMBER]
        self.__order_elements = order_elements

        if discount_policy is None:
            discount_policy = default_policy
        self.discount_policy = discount_policy
        self.total_price = self.__calculate_total_price()

    def __calculate_total_price(self):
        total_price = 0
        for element in self.__order_elements:
            total_price += element.calculate_price()
        return self.discount_policy(total_price)

    def add_to_order(self, product, quantity):
        if len(self.__order_elements) < Order.MAX_ELEMENTS_NUMBER:
            new_element = OrderElement(product, quantity)
            self.__order_elements.append(new_element)
            self.total_price = self.__calculate_total_price()
        else:
            print("Osiagnieto limit pozycji w zamowieniu.")

    def __str__(self):
        return_string = "="*20+"\n"
        return_string += f"Zamowienie zlozone przez: {self.first_name} {self.last_name}\n"
        return_string += f"O lacznej wartosci: {self.total_price} PLN\n"
        return_string += f"Zamowione produkty:\n"
        for element in self.__order_elements:
            return_string += f"\t{element}"
        return_string += "\n" + "=" * 20 + "\n"
        return return_string

    def __len__(self):
        return len(self.__order_elements)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        else:
            for element in self.__order_elements:
                if element not in other.order_elements:
                    return False
            return (self.first_name == other.firstname and
                    self.last_name == other.last_name and
                    len(self.__order_elements) == len(other.order_elements))
