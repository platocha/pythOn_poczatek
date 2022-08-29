from shop.discount_policy import DiscountPolicy

class Order:

    MAX_ELEMENTS_NUMBER = 20
    def __init__(self, first_name, last_name, order_elements=None, discount_policy=None):
        self.first_name = first_name
        self.last_name = last_name

        if order_elements is None:
            order_elements = []

        if len(order_elements) > Order.MAX_ELEMENTS_NUMBER:
            order_elements = order_elements[:Order.MAX_ELEMENTS_NUMBER]
        self._order_elements = order_elements

        if discount_policy is None:
            discount_policy = DiscountPolicy()
        self.discount_policy = discount_policy

    @property
    def total_price(self):
        total_price = 0
        for element in self._order_elements:
            total_price += element.calculate_price()
        return self.discount_policy.apply_discount(total_price)

    @property
    def order_elements(self):
        return self._order_elements

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
        for element in self._order_elements:
            return_string += f"\t{element}"
        return_string += "\n" + "=" * 20 + "\n"
        return return_string

    def __len__(self):
        return len(self._order_elements)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        else:
            for element in self._order_elements:
                if element not in other.order_elements:
                    return False
            return (self.first_name == other.firstname and
                    self.last_name == other.last_name and
                    len(self._order_elements) == len(other.order_elements))

class ExpressOrder(Order):

    EXPRESS_DELIVERY_FEE = 10

    def __init__(self, first_name, last_name, order_date, order_elements=None, discount_policy=None):
        super().__init__(first_name, last_name, order_elements, discount_policy)
        self.order_date = order_date

    @property
    def total_price(self):
        total_price = 0
        for element in self._order_elements:
            total_price += element.calculate_price()
        return self.discount_policy.apply_discount(total_price) + ExpressOrder.EXPRESS_DELIVERY_FEE

    def __str__(self):
        return_string = "=" * 20 + "\n"
        return_string += f"Zamowienie zlozone przez: {self.first_name} {self.last_name}\n"
        return_string += f"O lacznej wartosci: {self.total_price} PLN (Dodatkowa oplata: {self.EXPRESS_DELIVERY_FEE} PLN)\n"
        return_string += f"Data dostawy: {self.order_date}\n"
        return_string += f"Zamowione produkty:\n"
        for element in self.order_elements:
            return_string += f"\t{element}"
        return_string += "\n" + "=" * 20 + "\n"
        return return_string
