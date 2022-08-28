from shop.data_generator import generate_order_elements
from shop.discount_policy import loyal_customer_policy, christmas_policy
from shop.order import Order

def run_homework():
    first_name = "Pawel"
    last_name = "Latocha"
    order_elements = generate_order_elements(1)
    normal_order = Order(first_name, last_name, order_elements)
    loyal_customer_order = Order(first_name, last_name, order_elements, discount_policy=loyal_customer_policy)
    christmas_order = Order(first_name, last_name, order_elements, discount_policy=christmas_policy)

    print(normal_order)
    print(loyal_customer_order)
    print(christmas_order)

if __name__ == '__main__':
    run_homework()



