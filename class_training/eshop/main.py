from shop import data_generator
from shop.discount_policy import PercentageDiscount, AbsoluteDiscount
from shop.order import Order

def run_homework():
    order_elements = data_generator.generate_order_elements()
    my_order = Order("Bob", "Kowalski", order_elements=order_elements)
    print(my_order)


if __name__ == '__main__':
    run_homework()



