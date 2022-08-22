from shop.apple import Apple
from shop.order import print_order, generate_order
from shop.potato import Potato

def run_homework():
    green_apple = Apple(species="Green", size="M", price=3.5)
    red_apple = Apple(species="Red", size="S", price=2.8)
    print(green_apple.species, green_apple)
    print(red_apple.species, red_apple.price)

    old_potato = Potato(species="Potato Old", size="S", price=0.8)
    print(old_potato.species, old_potato.price)

    first_order = generate_order()
    first_order.print_self
    second_order = generate_order()
    second_order.print_self

    print(old_potato.calculate_total_price(10))
    print(red_apple.calculate_total_price(20))

if __name__ == '__main__':
    run_homework()



