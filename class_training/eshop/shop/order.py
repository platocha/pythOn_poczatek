from shop.discount_policy import default_policy

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

    @property
    def total_price(self):
        total_price = 0
        for element in self.__order_elements:
            total_price += element.calculate_price()
        return self.discount_policy(total_price)

    @property
    def order_elements(self):
        return self.__order_elements

    @order_elements.setter
    def order_elements(self, value):
        if len(value) < Order.MAX_ELEMENTS_NUMBER:
            self.order_elements = value
        else:
            print("Nie ma juz miejsca!")
            self.order_elements = value[:Order.MAX_ELEMENTS_NUMBER]

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
