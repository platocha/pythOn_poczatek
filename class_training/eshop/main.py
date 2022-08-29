from shop import data_generator
from shop.discount_policy import PercentageDiscount, AbsoluteDiscount
from shop.order import Order

def run_homework():
    order_elements = data_generator.generate_order_elements()
    ten_percent_discount = PercentageDiscount(percentage=10)
    houndred_pln_discount = AbsoluteDiscount(discount_value=100)

    no_discount_order = Order(
        first_name = "M",
        last_name = "L",
        order_elements = order_elements
    )

    order_with_percentage_discount = Order(
        first_name="M",
        last_name="L",
        order_elements=order_elements,
        discount_policy=ten_percent_discount
    )

    order_with_absolute_discount = Order(
        first_name="M",
        last_name="L",
        order_elements=order_elements,
        discount_policy=houndred_pln_discount
    )

    print(no_discount_order)
    print(order_with_percentage_discount)
    print(order_with_absolute_discount)


if __name__ == '__main__':
    run_homework()



