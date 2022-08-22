from shop.apple import Apple
from shop.order import generate_order
from shop.potato import Potato

def run_homework():
    first_order = generate_order()
    print(first_order)
    second_order = generate_order()
    print(second_order)
    # old_potato = Potato(species="Old Potato", size="S", price=0.2)
    # print(old_potato)
    # red_apple = Apple(species="Red", size="M", price=2.5)
    # print(red_apple)
    # print(len(first_order))

if __name__ == '__main__':
    run_homework()



