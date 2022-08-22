from shop.apple import Apple
from shop.order import Order
from shop.potato import Potato

def run_homework():
    first_order = Order.generate_order(10)
    print(first_order)
    second_order = Order.generate_order(5)
    print(second_order)
    # old_potato = Potato(species="Old Potato", size="S", price=0.2)
    # print(old_potato)
    # red_apple = Apple(species="Red", size="M", price=2.5)
    # print(red_apple)
    # print(len(first_order))

if __name__ == '__main__':
    run_homework()



